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
  // Simulate curator interaction to create an archive
  delay(5000);                 // Simulate a time gap
  setColor(0, 255, 0);         // Set RGB LED to green
  Serial.println("ARCHIVE_CREATED"); // Notify the laptop
  delay(3000);                 // Keep the LED on for 3 seconds
  setColor(0, 0, 0);           // Turn off the RGB LED
  delay(10000);                // Wait before the next simulated interaction
}

// Function to set the RGB LED color
void setColor(int red, int green, int blue) {
  analogWrite(redPin, red);    // Adjust red brightness
  analogWrite(greenPin, green); // Adjust green brightness
  analogWrite(bluePin, blue);   // Adjust blue brightness
}
