import pygame
from tkinter import Tk, Label, Button
from PIL import Image, ImageTk
import serial
import time
from threading import Timer

# Serial setup 
ser = serial.Serial('COM3', 9600)  
time.sleep(2)  # Wait for serial connection to initialize

# Audio and image setup
pygame.mixer.init()
story_audio = "audio\COVID_19_Small_Business_Story_Waterford_Wellness_and_Spa.mp3"  
story_image = "images\small_business_story.png"  

# GUI setup
root = Tk()
root.title("EchoSphere Scenario 2: Reviewing Contributions")
root.geometry("800x600")

status_label = Label(root, text="Welcome to the EchoSphere!", font=("Helvetica", 26))
status_label.pack(pady=20)

image_label = Label(root)  # Label to display the story image
image_label.pack(pady=20)

# Function to display the image
def display_image(image_path):
    img = Image.open(image_path)
    img = img.resize((1600, 800))  # Resize image to fit the GUI
    img_tk = ImageTk.PhotoImage(img)
    image_label.config(image=img_tk)
    image_label.image = img_tk  # Keep reference to avoid garbage collection

# Function to stop playback and reset the GUI
def stop_playback():
    pygame.mixer.music.stop()  # Stop the audio playback
    status_label.config(text="Welcome to the EchoSphere!")  # Reset the status label
    image_label.config(image="")  # Clear the displayed image

# Subscenario 2.1: Play the story
def play_story():
    ser.write(b"STOP_FLASHING\n")  # Stop the red LED from flashing
    status_label.config(text="Playing latest story: Small Business Story")
    pygame.mixer.music.load(story_audio)  # Play the audio story
    pygame.mixer.music.play()
    display_image(story_image)  # Display the associated image

    # Stop playback and reset GUI after 12 seconds
    Timer(12, stop_playback).start()

# Subscenario 2.2: Categorize the story
def categorize_story():
    ser.write(b"CATEGORIZE\n")
    status_label.config(text="Story categorized as Local Business.")

# Subscenario 2.3: Edit the story
def edit_story():
    ser.write(b"EDIT_STORY\n")
    status_label.config(text="Editing the story. Please make your changes.")

# Buttons for each subscenario
btn_play_story = Button(root, text="Play Latest Story", command=play_story, font=("Helvetica", 16))
btn_play_story.pack(pady=10)

btn_categorize = Button(root, text="Categorize Story", command=categorize_story, font=("Helvetica", 16))
btn_categorize.pack(pady=10)

btn_edit_story = Button(root, text="Edit Story", command=edit_story, font=("Helvetica", 16))
btn_edit_story.pack(pady=10)

# Start flashing the LED to indicate a new story
ser.write(b"START_FLASHING\n")

# Start GUI event loop
root.mainloop()
