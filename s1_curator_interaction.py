import serial
import time
from tkinter import Tk, Label

# Serial setup
ser = serial.Serial('COM3', 9600)
time.sleep(2)

# GUI setup
root = Tk()
root.title("EchoSphere Archive Notifications")
root.geometry("600x300")

status_label = Label(root, text="Waiting for Archive Creation...", font=("Helvetica", 16))
status_label.pack(pady=50)

def listen_for_archive_creation():
    if ser.in_waiting > 0:
        message = ser.readline().decode('utf-8').strip()
        if message == "ARCHIVE_CREATED":
            status_label.config(text="New Archive Created! Notification Sent.")
    root.after(100, listen_for_archive_creation)

root.after(100, listen_for_archive_creation)
root.mainloop()

