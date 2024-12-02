import pygame
from tkinter import Tk, Label
from PIL import Image, ImageTk
import serial

# Setup
pygame.mixer.init()
story_1_audio = "audio\COVID_19_Small_Business_Story_Waterford_Wellness_and_Spa.mp3" 
story_2_audio = "audio\A_Story_of_Survival_-_COVID-19_Testimony.mp3"  
story_1_image = "images\small_business_story.png"  
story_2_image = "images\survival_story.png"  
ser = serial.Serial('COM3', 9600)  

# GUI setup
root = Tk()
root.title("EchoSphere Museum Interaction")
root.geometry("1600x1000")  # Adjusted size to fit the image and text

# Status label for text
status_label = Label(root, text="Touch the EchoSphere to Play a Story.", font=("Helvetica", 26))
status_label.pack(pady=10)

# Label to display the image
image_label = Label(root)
image_label.pack(pady=20)

# Function to update the image display
def display_image(image_path):
    # Open the image using PIL
    img = Image.open(image_path)

    # Resize the image to fit the window (maintain aspect ratio)
    img = img.resize((1600, 800))  

    # Convert the image to PhotoImage for Tkinter
    img_tk = ImageTk.PhotoImage(img)
    image_label.config(image=img_tk)
    image_label.image = img_tk  # Keep a reference to avoid garbage collection

# Function to listen for touch events and trigger appropriate actions
def listen_for_touch():
    if ser.in_waiting > 0:
        message = ser.readline().decode('utf-8').strip()
        if message == "STORY_1_TRIGGERED":
            pygame.mixer.music.load(story_1_audio)
            pygame.mixer.music.play()
            status_label.config(text="Playing Story 1...")
            display_image(story_1_image)
        elif message == "STORY_2_TRIGGERED":
            pygame.mixer.music.load(story_2_audio)
            pygame.mixer.music.play()
            status_label.config(text="Playing Story 2...")
            display_image(story_2_image)
    root.after(100, listen_for_touch)

# Start listening for events
root.after(100, listen_for_touch)
root.mainloop()
