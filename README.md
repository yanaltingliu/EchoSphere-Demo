# EchoSphere-Demo

**EchoSphere** is a Creativity Support Tool (CST) prototype designed for interactive storytelling and collaborative archiving. It integrates touch-based interactions, audio playback, and image displays to explore the concept of dynamic, participatory story preservation.

## Features
- **Interactive Storytelling**: Play audio stories and display associated images via touch sensor input.
- **Visual Feedback**: RGB LEDs indicate status updates such as new story contributions or archive creation.
- **Museum Display**: Simulated interactions for immersive storytelling in exhibitions.

## Setup Instructions
1. **Hardware Requirements**:
   - Arduino Uno (or compatible microcontroller)
   - Touch sensors (2)
   - RGB LED and standard LED
   - USB connection for the Arduino

2. **Software Requirements**:
   - Python 3.7+
   - Required libraries:
     - `pygame`
     - `tkinter` (built-in with Python)
     - `Pillow` (for image processing)
   - Arduino IDE for uploading the microcontroller code

3. **Install Dependencies**:
   Use the following command to install Python libraries:
   ```bash
   pip install pygame pillow

4. **Run the Python Code**:
   Ensure the Arduino is connected and the correct COM port is configured in the Python code.
   Run the Python script:
   python script_name.py

5. **Upload Arduino Code**:
   Open the Arduino IDE, upload the corresponding .ino file to the microcontroller.
