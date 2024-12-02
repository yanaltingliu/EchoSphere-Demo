// Pin assignments for the RGB LED
const int redPin = 9;    // Red pin of RGB LED
const int greenPin = 10; // Green pin of RGB LED
const int bluePin = 11;  // Blue pin of RGB LED

bool newUpdate = true; // Flag to indicate new story updates

void setup() {
  // Set all RGB pins as outputs
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);

  Serial.begin(9600); // Start serial communication with the laptop
}

void loop() {
  // Flash red continuously if there's a new update
  if (newUpdate) {
    setColor(255, 0, 0);  // Turn on red
    delay(500);           // Wait 500ms
    setColor(0, 0, 0);    // Turn off LED
    delay(500);           // Wait 500ms
  }

  // Check for commands from Python
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n');

    if (command == "STOP_FLASHING") {
      newUpdate = false;    // Stop flashing
      setColor(0, 0, 0);    // Turn off the LED
    } else if (command == "CATEGORIZE") {
      Serial.println("Story categorized as Local Business.");
    } else if (command == "EDIT_STORY") {
      Serial.println("Editing the story. Please make your changes.");
    }
  }
}

// Function to set RGB LED color
void setColor(int red, int green, int blue) {
  analogWrite(redPin, red);
  analogWrite(greenPin, green);
  analogWrite(bluePin, blue);
}
