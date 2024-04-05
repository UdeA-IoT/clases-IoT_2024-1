# Ejemplo 4

Realizar una implementación sencilla que permita el encedido y apagado de un led mediante el protocolo MQTT. En la siguiente figura se muestra la aplicación:

<p align = "center">
<img src = "mqtt_ejemplo4.png">
</p>


## Thing - ESP32

### Configuración de la cosa

1. **Hardware**:
   
   * **Lista de componentes**:
  

     |#| Elemento| Cantidad|
     |---|---|---|
     |1|ESP32| 1|
     |1|Resistencia $220 \Omega$| 1|
     |1|Led| 1|

   * **Esquematico**:
  
    <p align = "center">
    <img src = "mqtt_ej4_sch.png">
    </p>

   * **Conexión**:
  
    <p align = "center">
    <img src = "mqtt_ej4_bb.png">
    </p>

2. **Librerias**:
   
   |#|Libreria|Observaciones|
   |---|---|---|
   |1|PubSubClient|Libreria que implementa el protocolo MQTT|

3. **Parametros WiFi**:

   |Parametro|	Valor|
   |---|---|
   |SSID|`"IoT"`|
   |PASSWORD|`"1245678h"`|

4. **Parametros MQTT**:

   |Parametro|	Valor|
   |---|---|
   |BROKER|`"test.mosquitto.org"`|
   |ID|`"thing-001"`|

5. **Topicos**

   |#|Topico|Mensaje|Descripción|Rol (S/P)|
   |---|---|---|---|---|
   |1|`light_outbound`|`cmd`|`cmd` corresponde al comando recibido para encender (`"ON"`) o apagar  la lampara `"OFF"`.|S|
   |2|`light_inbound`|`cmd`|`cmd` corresponde al comando enviado indicar el estado de la lampara.  Encendida(`"ON"`) o apagada `"OFF"`.|P|
   

6. **Código**:
   
   * **Archivo de configuración**: [platformio.ini](ESP32-code/platformio.ini)
  
        ```ini
        [env:upesy_wroom]
        platform = espressif32
        board = upesy_wroom
        framework = arduino
        lib_deps = knolleary/PubSubClient@^2.8
        ```
    
    * **Header**: [config.h](ESP32-code/src/config.h)
          
        ```h
        #pragma once
        #include <string>
        
        using namespace std;
        
        // ESP32 I/O config
        #define LIGHT_PIN 5
        
        // WiFi credentials
        const char *SSID = "SSID";
        const char *PASSWORD = "PASSWORD";
        
        // MQTT settings
        const string ID = "thing-001";
        
        const string BROKER = "IP_BROKER"; // const string BROKER = "test.mosquito.org";
        const string CLIENT_NAME = ID + "lamp_client";
        
        const string TOPIC1 = "light_outbound";
        const string TOPIC2 = "light_inbound";
        ```
        
    * **Archivo main**: [main.cpp](ESP32-code/src/main.cpp) 

        ```cpp
        #include <Arduino.h>
        #include <WiFi.h>
        #include <PubSubClient.h>
        
        #include "config.h"
        
        WiFiClient espClient;
        PubSubClient client(espClient); // Setup MQTT client
        
        
        // --- ESP32
        
        void setup_ports() {
          pinMode(LIGHT_PIN, OUTPUT); // Configure LIGHT_PIN as an output
        }
        
        
        // ---- Wifi
        
        void connectWiFi() {
          Serial.print("Connecting to ");
          Serial.print(SSID);
          while (WiFi.status() != WL_CONNECTED) {   
            Serial.print(".");
            WiFi.begin(SSID, PASSWORD);
            delay(500);
          }
          Serial.println();
          Serial.print(ID.c_str());
          Serial.println(" connected!");
          Serial.print("IP address: ");
          Serial.println(WiFi.localIP());
        }
        
        // ---- MQTT
        
        
        // Handle incomming messages from the broker
        void clientCallback(char* topic, byte* payload, unsigned int length) {
          String response;
        
          for (int i = 0; i < length; i++) {
            response += (char)payload[i];
          }
          Serial.print("Message arrived [");
          Serial.print(TOPIC1.c_str());
          Serial.print("] ");
          Serial.println(response);
          if(response == "ON")  // Turn the light on
          {
            digitalWrite(LIGHT_PIN, HIGH);
          }
          else if(response == "OFF")  // Turn the light off
          {
            digitalWrite(LIGHT_PIN, LOW);
          }
          // Publish message
          client.publish(TOPIC2.c_str(), response.c_str());
        }
        
        void reconnectMQTTClient() {
          while (!client.connected()) {
            Serial.println("Attempting MQTT connection...");
            if (client.connect(CLIENT_NAME.c_str())) {
              Serial.print("connected to Broker: ");
              Serial.println(BROKER.c_str());
              // Topic(s) subscription
              client.subscribe(TOPIC1.c_str());
            }
            else {
              Serial.print("Retying in 5 seconds - failed, rc=");
              Serial.println(client.state());
              delay(5000);
            }
          }
        }
        
        void createMQTTClient() {
          client.setServer(BROKER.c_str(), 1883);
          client.setCallback(clientCallback);
          reconnectMQTTClient();
        }
        
        void setup() {
          // Setup ports
          setup_ports();
          // Serial setup
          Serial.begin(9600);
          while (!Serial)
            ; // Wait for Serial to be ready
          delay(1000);
          connectWiFi();
          createMQTTClient();
        }
        
        void loop() {
          reconnectMQTTClient();
          client.loop();
          delay(1000);
        }
        ```

###  Prueba mqtt ESP32

<p align = "center">
<img src = "ejemplo4-ESP32_debug.png">
</p>

La siguiente tabla muestran los comandos aplicados al cliente para encender y apagar la lampara:

|Acción	|Comando mosquitto_pub|
|----|----|
|Encender el led|`mosquitto_pub -h test.mosquitto.org -t light_outbound -m ON`|
|Apagar el led|	`mosquitto_pub -h test.mosquitto.org -tlight_outbound -m OFF`|


Ahora, vamos a mostrar los mensajes enviados desde la ESP32, para indicar el estado del led, usando el mosquito_sub:

```
mosquitto_sub -h test.mosquitto.org -t light_inbound
```


## Controlando el encendido y apagado del led desde la interfaz kivy

El código de la interfaz se encuentra en el directorio ([link](ejemplo-kivy-iot/)). Esta interfaz envia comandos MQTT para encender y apagar la lampara:

* **Interfaz con el bombillo apagado**:
  
  <p align = "center">
  <img src = "lamp_off.png">
  </p>

* **Interfaz con el bombillo encendido**:

  <p align = "center">
  <img src = "lamp_on.png">
  </p>


### Prueba MQTT aplicación kivy

<p align = "center">
<img src = "ejemplo4-app_kivy_debug.png">
</p>