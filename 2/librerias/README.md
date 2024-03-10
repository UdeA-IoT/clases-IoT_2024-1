# Ejemplos

1. Simulacion con LCD: https://wokwi.com/projects/391941764165031937

```C++
#include <Arduino.h>
#include <LiquidCrystal.h>

// initialize the library by associating any needed LCD interface pin
// with the arduino pin number it is connected to
const int rs = 22, en = 23, d4 = 4, d5 = 0, d6 = 2, d7 = 15;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

int counter = 0;

void setup() {
  Serial.begin(9600);
  Serial.println(F("LCD test!"));

  // set up the LCD's number of columns and rows:
  lcd.begin(16, 2);
  // Print a message to the LCD.
  lcd.print("LCD Ready!");
  lcd.setCursor(0, 1);
  delay(2000);  
  lcd.print("Counter: ");
}

void loop() {
  Serial.print("Counter: ");   
  Serial.println(counter);    
  lcd.print(counter,DEC);
  delay(1000);
  counter++;
  lcd.setCursor(9, 1);
}
```

2. Simulación Key pad con sonido de beep: https://wokwi.com/projects/391981965608341505


```C++
#include <Keypad.h>

// ---------------- Entradas ---------------- //

// ---- Keypad ----
const byte ROWS = 4; // Four rows
const byte COLS = 4; // Three columns
    
// Define the Keymap
char keys[ROWS][COLS] = {
  {'1','2','3','A'},
  {'4','5','6','B'},
  {'7','8','9','C'},
  {'#','0','*','D'}
};
    
// Conections ESP32 - Keypad
#define ROW1 9
#define ROW2 13
#define ROW3 12
#define ROW4 14
#define COL1 27
#define COL2 26
#define COL3 25
#define COL4 33
    
// Connect keypad ROW1, ROW2, ROW3 and ROW4 to these Arduino pins.
byte rowPins[ROWS] = { ROW1, ROW2, ROW3, ROW4 };
// Connect keypad COL0, COL1, COL2 and COL3 to these Arduino pins.
byte colPins[COLS] = { COL1, COL2, COL3, COL4 }; 
    
// Create the Keypad
Keypad kpd = Keypad( makeKeymap(keys), rowPins, colPins, ROWS, COLS );

// ---------------- Salidas ---------------- //
// Led
const int ledpin = 21;  
// buzzer
const int buzzerPin = 16;   
int buzzerState = LOW;        // the current state of the output pin
int freq = 2000;
int channel = 0;
int resolution = 8;

void setup() {
  pinMode(ledpin,OUTPUT);
  digitalWrite(ledpin, HIGH);

  // Init pwm (buzzer)
  ledcSetup(channel, freq, resolution);
  ledcAttachPin(buzzerPin, channel);
  // Init serial

  Serial.begin(9600);
  Serial.println("System Ok...");
}
    
void loop() {
  char key = kpd.getKey();
  if(key) { 
    // Check for a valid key.
    switch (key) {
      case '*':
        digitalWrite(ledpin, LOW);
        break;
      case '#':
        digitalWrite(ledpin, HIGH);
        break;
      default:
        Serial.println(key);
    }
    ledcWriteTone(channel, 1500);
    delay(100);
    ledcWriteTone(channel, 0);
  }
}
```

3. Simulación Key pad con sonido de beep y LCD:

