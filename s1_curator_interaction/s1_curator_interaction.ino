// Pin assignments for the RGB LED
const int redPin = 9;    // Red pin of RGB LED
const int greenPin = 10; // Green pin of RGB LED
const int bluePin = 11;  // Blue pin of RGB LED

void setup() {
  // Set all RGB pins as outputs
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);

  Serial.begin(9600); // Start serial communication with the laptop
}

void loop() {
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n');

    if (command == "CREATE_ARCHIVE") {
      // Subscenario 1: Confirmation message and green light
      setColor(0, 255, 0); // Green
      Serial.println("Archive creation confirmed!");
      delay(3000);
      setColor(0, 0, 0); // Turn off LED
    } else if (command == "ASK_DETAILS") {
      // Subscenario 2: Asking for details
      Serial.println("Please provide the archive theme and requirements.");
      delay(3000);
      setColor(0, 0, 0); // Turn off LED
    } else if (command == "NOTIFICATION_SENT") {
      // Subscenario 3: Notification sent and orange light
      setColor(255, 165, 0); // Orange
      Serial.println("Notification sent to the community.");
      delay(10000);
      setColor(0, 0, 0); // Turn off LED
    }
  }
}

// Function to set the RGB LED color
void setColor(int red, int green, int blue) {
  analogWrite(redPin, red);    
  analogWrite(greenPin, green); 
  analogWrite(bluePin, blue);   
}
