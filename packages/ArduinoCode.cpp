#include <SoftwareSerial.h>

#define trigPin 5 // Trigger pin of HC-SR04
#define echoPin 4 // Echo pin of HC-SR04
#define led1Pin 6 
#define led2Pin 7 

#define cooldownTime 10000 // 10 seconds cooldown time in milliseconds
#define timeExceededThreshold 10000 // 10 seconds threshold for time exceeded

unsigned long previousMillis = 0; // Variable to store the previous timestamp
unsigned long cooldownStart = 0; // Variable to store the start time of cooldown
bool cooldownActive = false; // Flag to indicate if cooldown is active

SoftwareSerial BTserial(2, 3); // RX | TX

void setup() {
  Serial.begin(9600);
  BTserial.begin(9600); // HC-05 default baud rate
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}

void loop() {
  unsigned long currentMillis = millis(); // Get current timestamp
  unsigned long elapsedTime = currentMillis - previousMillis;

  if (!cooldownActive) {
    // Trigger a new distance measurement
    digitalWrite(trigPin, LOW);
    delayMicroseconds(2);
    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);

    // Read the pulse from the echo pin
    long duration = pulseIn(echoPin, HIGH);

    // Calculate distance in cm
    int distance = duration * 0.034 / 2;

    // Check if the distance is less than 30 cm
    if (distance < 30) {
      if (elapsedTime >= timeExceededThreshold) {
        Serial.println("Time Exceeded");
        BTserial.println("Time Exceeded");
        delay(2000); // Delay 1 second
        cooldownStart = currentMillis; // Start cooldown timer
        cooldownActive = true; // Set cooldown active flag
        digitalWrite(led1Pin, HIGH);
        delay(10000);
        digitalWrite(led1Pin, LOW);
      }

      // Check if the distance is less than 15 cm
      if (distance < 15) {
        Serial.println("Too Close");
        BTserial.println("Too Close");
        Serial.println(distance);
        digitalWrite(led2Pin, HIGH);
        delay(500);
        digitalWrite(led2Pin, LOW);
        delay(2000); // Delay 1 second
      }
    }
  } else {
    // Check if cooldown timer is still running
    if (currentMillis - cooldownStart < cooldownTime) {
      Serial.println("Cooldown not complete");
      BTserial.println("Cooldown not complete");
      delay(2000); // Delay 1 second
    } else {
      cooldownActive = false; // Cooldown completed, reset flag
      previousMillis = currentMillis; // Reset timestamp for next measurement
    }
  }
}




