import os
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import pygame

# Initialize Pygame
pygame.mixer.init()

# Function to upload a music file
def upload_music():
    global filename
    filename = filedialog.askopenfilename(initialdir="/", title="Select A File", filetype=(("mp3 files", "*.mp3"), ("all files", "*.*")))
    music_list.insert(END, filename)
    messagebox.showinfo("Success", "Music file uploaded successfully!")

# Function to play selected music file
def play_music():
    selected_music = music_list.get(ACTIVE)
    if selected_music:
        pygame.mixer.music.load(selected_music)
        pygame.mixer.music.play()
        now_playing_label.config(text=f"Now Playing: {os.path.basename(selected_music)}")
    else:
        messagebox.showerror("Error", "Please select a music file to play")

# Function to stop music
def stop_music():
    pygame.mixer.music.stop()
    now_playing_label.config(text="")

# Function to share music (dummy implementation)
def share_music():
    selected_music = music_list.get(ACTIVE)
    if selected_music:
        messagebox.showinfo("Share", f"Sharing {os.path.basename(selected_music)}")
    else:
        messagebox.showerror("Error", "Please select a music file to share")

# Create the main window
root = Tk()
root.title("Music Sharing App")

# Create and place widgets
upload_button = Button(root, text="Upload Music", command=upload_music)
upload_button.pack()

play_button = Button(root, text="Play Music", command=play_music)
play_button.pack()

stop_button = Button(root, text="Stop Music", command=stop_music)
stop_button.pack()

share_button = Button(root, text="Share Music", command=share_music)
share_button.pack()

music_list = Listbox(root, selectmode=SINGLE, width=50)
music_list.pack()

now_playing_label = Label(root, text="", wraplength=300)
now_playing_label.pack()

# Run the main event loop
root.mainloop()
