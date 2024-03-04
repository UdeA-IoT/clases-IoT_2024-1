
* https://github.com/UdeA-IoT/clases-IoT_capa-percepcion_2023-2/tree/main/dia3/esp32


Variando el color

* https://esp32io.com/tutorials/esp32-rgb-led
* https://learn.sparkfun.com/tutorials/tinker-kit-circuit-guide/circuit-4-rgb-night-light
* https://learn.adafruit.com/all-about-leds
* https://learn.sparkfun.com/tutorials/light-emitting-diodes-leds?_ga=2.14738416.7348529.1709345755-1122723610.1691641161&_gl=1*1ebgs86*_ga*MTEyMjcyMzYxMC4xNjkxNjQxMTYx*_ga_T369JS7J9N*MTcwOTM0NTc1Ni4yMC4xLjE3MDkzNDU4NDIuMzcuMC4w#leds-without-math
* https://learn.adafruit.com/adafruit-arduino-lesson-3-rgb-leds/overview
* https://learn.adafruit.com/adafruit-arduino-lesson-3-rgb-leds/using-internet-colors
* https://htmlcolorcodes.com/color-names/
* https://learn.sparkfun.com/tutorials/experiment-guide-for-the-sparkfun-tinker-kit/experiment-4-driving-multiple-leds
* https://www.luisllamas.es/referencia-lenguaje-arduino/

Link: https://wokwi.com/projects/391210532094486529

Parte del ejemplo base:

https://docs.arduino.cc/built-in-examples/digital/Debounce/


```C++
int redPin = 19;
int greenPin = 18;
int bluePin = 5;

//uncomment this line if using a Common Anode LED
//#define COMMON_ANODE

void setup()
{
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);  
}

void loop()
{
  setColor(255, 0, 0);  // red
  delay(1000);
  setColor(0, 255, 0);  // green
  delay(1000);
  setColor(0, 0, 255);  // blue
  delay(1000);
  setColor(255, 255, 0);  // yellow
  delay(1000);  
  setColor(80, 0, 80);  // purple
  delay(1000);
  setColor(0, 255, 255);  // aqua
  delay(1000);
}

void setColor(int red, int green, int blue)
{
  #ifdef COMMON_ANODE
    red = 255 - red;
    green = 255 - green;
    blue = 255 - blue;
  #endif
  analogWrite(redPin, red);
  analogWrite(greenPin, green);
  analogWrite(bluePin, blue);  
}
```

Poniendo un boton

Codigo OK: https://wokwi.com/projects/391211218645463041
Codigo debug: https://wokwi.com/projects/391344633629636609


Poniendo un sensor de distancia o PIR


* https://github.com/UdeA-IoT/ejemplos-mqtt/tree/main/ejemplo_2/thing_02


* https://arts.recursos.uoc.edu/programacio-disseny-arts/es/maxmsp-pure-data/
* 