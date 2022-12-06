
#include <Servo.h>
Servo motor1;

const int ledPin = 13; // the pin that the LED is attached to
const int buzzer = 9;
int incomingByte;      // a variable to read incoming serial data into

void setup() {
  // initialize serial communication:
  Serial.begin(9600);
  // initialize the LED pin as an output:
  pinMode(ledPin, OUTPUT);
  pinMode(buzzer, OUTPUT);

  motor1.attach(12);
}

void loop() {
  // see if there's incoming serial data:
  if (Serial.available() > 0) {
    // read the oldest byte in the serial buffer:
    incomingByte = Serial.read();
    // if it's a capital H (ASCII 72), turn on the LED:
    if (incomingByte == 'H') {
      digitalWrite(ledPin, LOW);
      motor1.write(0);
      tone(buzzer, 2000); //noTone(buzzer);

      //motor
      
      
    }
    // if it's an L (ASCII 76) turn off the LED:
    if (incomingByte == 'L') {
      //buzzer
      digitalWrite(ledPin, HIGH);
      motor1.write(180);//180
      noTone(buzzer); //tone(buzzer, 2000); // Send 1KHz sound signal...
      //delay(1000);        // ...for 1 sec
      //noTone(buzzer);     // Stop sound...
      //delay(1000)
      //

      //motor
      //motor1.write(0);
      //delay(400);
      //motor1.write(180);
      //delay(400);
      
    }
  }
}