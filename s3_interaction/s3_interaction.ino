const int touchSensor1 = 2;  // Touch sensor for story 1
const int touchSensor2 = 3;  // Touch sensor for story 2
const int projectorLED = 12; // LED to simulate a projector

void setup() {
  pinMode(touchSensor1, INPUT);
  pinMode(touchSensor2, INPUT);
  pinMode(projectorLED, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (digitalRead(touchSensor1) == HIGH) {
    Serial.println("STORY_1_TRIGGERED");
    digitalWrite(projectorLED, HIGH);
    delay(50000);  // Simulate story playback
    digitalWrite(projectorLED, LOW);
  }

  if (digitalRead(touchSensor2) == HIGH) {
    Serial.println("STORY_2_TRIGGERED");
    digitalWrite(projectorLED, HIGH);
    delay(50000);  // Simulate story playback
    digitalWrite(projectorLED, LOW);
  }
}
