import serial
import time
from tkinter import Tk, Label, Button

# Serial setup
ser = serial.Serial('COM3', 9600)
time.sleep(2)

# GUI setup
root = Tk()
root.title("EchoSphere Scenario 1: Create Archive")
root.geometry("600x300")

status_label = Label(root, text="Welcome to the EchoSphere!", font=("Helvetica", 26))
status_label.pack(pady=50)

# Subscenario 1: Archive creation confirmation
def create_archive():
    ser.write(b"CREATE_ARCHIVE\n")
    status_label.config(text="Archive creation confirmed!")

# Subscenario 2: Asking for details
def ask_details():
    ser.write(b"ASK_DETAILS\n")
    status_label.config(text="System: Please provide archive details.")

# Subscenario 3: Notification sent
def send_notification():
    ser.write(b"NOTIFICATION_SENT\n")
    status_label.config(text="Notification sent to the community!")

# Buttons for each subscenario
btn_create = Button(root, text="Create Archive", command=create_archive, font=("Helvetica", 16))
btn_create.pack(pady=10)

btn_details = Button(root, text="Ask for Details", command=ask_details, font=("Helvetica", 16))
btn_details.pack(pady=10)

btn_notify = Button(root, text="Send Notification", command=send_notification, font=("Helvetica", 16))
btn_notify.pack(pady=10)

# Start GUI event loop
root.mainloop()

