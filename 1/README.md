# Componentes basicos de un Sistema IoT


## Objetivos

>* Repasar los componentes básicos de un sistema IoT}
>* Explorar los componentes básicos que conforman el concepto de cosa.
>* Hacer las primeras pruebas con la placa de desarrollo ESP32
>* Investigar sobre los sistemas de desarrollo disponibles en el laboratorio.

## Referencias principales

1. Lección 2 **A deeper dive into IoT** ([link](https://github.com/microsoft/IoT-For-Beginners/blob/main/1-getting-started/lessons/2-deeper-dive/README.md)) del curso de Microsoft **IoT for Beginners** [[link](https://github.com/microsoft/IoT-For-Beginners)]

## Conceptos abordados

En la sesión de clase se abordaran los siguientes conceptos:
1. Componentes basicos de un Sistema IoT [[link]](https://udea-iot.github.io/UdeA_IoT-page/docs/sesiones/percepcion/sesion1)
2. Elementos de laboratorio [[link]](https://udea-iot.github.io/UdeA_IoT-page/docs/sesiones/percepcion/sesion2)
3. Arduino Framework [[link]](https://udea-iot.github.io/UdeA_IoT-page/docs/sesiones/percepcion/sesion3)
4. Comunicación serial [[link]](https://udea-iot.github.io/UdeA_IoT-page/docs/sesiones/percepcion/sesion4)

## Trabajo previo

### Aplicaciones locales

Antes de empezar asegurese de tene instalado en su computador el siguiente software:
- [x] Arduino IDE (https://www.arduino.cc/)
- [x] Visual Studio Code (https://code.visualstudio.com/)
- [x] Platformio (Complemento de Visual Studio Code: https://platformio.org/)
- [x] Fritzing (https://fritzing.org/)
- [x] draw.io (https://www.drawio.com/)
- [ ] Mosquitto (https://mosquitto.org/)
- [ ] Mqtt explorer (http://mqtt-explorer.com/)
- [x] Node-red (https://nodered.org/)

> **Nota**: Los programas que no se encuentran seleccinados no son necesarios instalarlos por el momento. Para mas información puede consultar el siguiente [link](https://udea-iot.gitbook.io/introduccion-al-iot/pasos-previos/herramientas-necesarias/software)

### Aplicaciones online

La siguiente es una lista de aplicaciones que se usaran para propositos de simulación. Para usarlas basta con tener una cuenta de correo como la de google poe ejemplo:
- [ ] Tinkercad (https://www.tinkercad.com/)
- [ ] Wokwi (https://wokwi.com/)

## Trabajo de clase

### 1. Ejemplo de un sistema IoT

A continuación se muestra el diagrama de un sistema de control en tiempo real para jugar con un laberinto hecho en la universidad de Curtin (https://www.curtin.edu.au/):

![IoT-example](IoT-example.png)

En el siguiente video se puede observar el funcionamiento de dicho sistema:

[![IOT3x - IoT Networks and Protocols](https://img.youtube.com/vi/ErS2W58StIs/0.jpg)](https://www.youtube.com/watch?v=ErS2W58StIs)


### 2. Sistemas de desarrollo

El corazón de los sistemas IoT son las cosas. Estas, son las encargadas de permitir la interacción del sistema con el medio ambiente mediante la recolección, el procesamiento de los datos y las acciones de control sobre este. 

Para realizar labores de prototipado, se disponen de los elementos listados a continuación:

|Tipo|Ejemplos|
|---|---|
|Single-board Computer|<li> Raspberry Pi <li> BeagleBoard <li> Orange Pi <li> Intel Galileo |
|Development boards|<li> Arduino UNO <li> ESP8266 <li> ESP32 <li>ARDUINO NANO 33 BLE Sense Lite|

> Para conocer mas sobre estos elementos disponibles en el laboratorio consulte el siguiente [link](https://udea-iot.github.io/UdeA_IoT-page/docs/sesiones/percepcion/sesion2)

### 3. Sensores y actuadores

Mediante los sensores y los actuadores es como la cosa interactua con el entorno (ambiente). Existen numerosos kits de iniciación en el mercado. En el laboratorio se disponen de los siguientes modulos:
* Grove - Starter Kit v3
  
  ![kit_groove](Grove-Starter_Kit_v2.jpg)

* 37 Sensor Kit - Elegoo
  
  ![sensores_elegoo](sensores_elegoo.jpg)

* Landzo 37 In 1 Sensors Kit For Arduino
  
  ![sensores_ladzo](sensores_ladzo.png)

> Para conocer mas sobre los sensores [link](https://udea-iot.github.io/UdeA_IoT-page/docs/sensores-actuadores/inventario-lab)

### 4. Trabajando con las placas de desarrollo a estudiar

Cuando se trabaja con un sistema de desarrollo, lo primero que hay que hacer es conocerlo. Para ello es necesario consultar la documentación de la cual este dispone como manual de usuario, datasheet, ejemplos y el diagrama de pines.

Este último es sumamente importante pues nos indicará los nombres, numeros y funciones que tendran los pines que se conectaran a los elementos externos (sensores, actuadores y/o otros sistemas de desarrollo) a los sistemas de desarrollo. 

El conocimiento de los pines es ademas importante por que constituye el punto de partida para la configuración de los puertos y modulos de software que serán empleados en la aplicación IoT en cuestión.

A continuación se muestra el diagrama de pines para el Arduino UNO y el ESP32.

* **Mapa de pines Arduino UNO**
  
  ![arduino_uno_pinout](arduino_uno-pinout.png)

* **Mapa de pines ESP32**

  ![esp32_pinout](nodemcu-esp_32s-pines.jpg)

> Para profundizar mas consulte la información relacionada con los sistemas de desarrollo anteriores en el siguiente [link](https://udea-iot.github.io/UdeA_IoT-page/docs/sesiones/percepcion/sesion2)

### 5. Prototipado básico

Fritzing es una plataforma para plataforma permitira prototipar hardware en su computador y verificar su funcionamiento antes de hacer el montaje en fisico.

![fritzing](Fritzing_breadboard_view.jpg)

> Consulte la sección **Prototipado básico usando fritzing** en el siguiente [link](https://udea-iot.github.io/UdeA_IoT-page/docs/sesiones/percepcion/sesion2)

Poner un ejercicio por equipo de usar fritzing para...

### 6. Arduino Framework

Colocar información basica sobre el framework de arduino...

### 7. Sensores básicos

Analogos y digitales y colocar algunos ejemplos...

## Lista de avance

- [ ] 1. Ejemplo de un sistema IoT
- [ ] 2. Sistemas de desarrollo
- [ ] 3. Sensores y actuadores
- [ ] 4. Trabajando con las placas de desarrollo a estudiar
- [ ] https://udea-iot.github.io/UdeA_IoT-page/docs/sensores-actuadores/sensores/intro


