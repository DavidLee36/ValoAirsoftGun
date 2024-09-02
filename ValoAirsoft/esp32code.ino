//This example code is in the Public Domain (or CC0 licensed, at your option.)
//By Evandro Copercini - 2018
//
//This example creates a bridge between Serial and Classical Bluetooth (SPP)
//and also demonstrate that SerialBT have the same functionalities of a normal Serial
 
#include "BluetoothSerial.h"
 
#if !defined(CONFIG_BT_ENABLED) || !defined(CONFIG_BLUEDROID_ENABLED)
#error Bluetooth is not enabled! Please run `make menuconfig` to and enable it
#endif
 
BluetoothSerial SerialBT;
const int relayPin = 4;
const int relayPower = 2;
String message = "";
char incomingChar;

void setup() {
  pinMode(relayPin, OUTPUT);
  pinMode(relayPower, OUTPUT);
  digitalWrite(relayPower, HIGH);
  Serial.begin(115200);
  SerialBT.begin("AirsoftGun"); //Bluetooth device name
  Serial.println("The device started, now you can pair it with bluetooth!");
}
 
void loop() {
  /*if (Serial.available()) {
    SerialBT.write(Serial.read());
  }*/
  
  if (SerialBT.available()) {
    incomingChar = SerialBT.read();
    if(incomingChar != '\n') {
      message += String(incomingChar);
    }else {
      message = "";
    }
    Serial.write(incomingChar);
  }
  if(message == "hit") {
    digitalWrite(relayPin, HIGH);
    delay(1000);
    digitalWrite(relayPin, LOW);
  }
  delay(20);
}
