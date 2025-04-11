import tkinter as tk
from tkinter import filedialog
import pygame

pygame.mixer.init()

def submit():
    name = name_var.get()
    greet.config(text=f"Hello, {name}! Let's enjoy the music 🎶")
    entry.pack_forget()
    btn_submit.pack_forget()
    btn_load.pack(pady=10)
    btn_play.pack()
    btn_stop.pack()

def load():
    file = filedialog.askopenfilename(filetypes=[("MP3", "*.mp3")])
    if file:
        pygame.mixer.music.load(file)
        song.set(f"Now Playing: {file.split('/')[-1]}")

def play(): pygame.mixer.music.play()
def stop(): pygame.mixer.music.stop()

root = tk.Tk()
root.title("🎧 Koding Next Music Player")
root.geometry("360x350")
root.config(bg="#1e1e2f")

name_var = tk.StringVar()
song = tk.StringVar(value="🎵 No song loaded")

tk.Label(root, text="🎼 Simple Music Player", font=("Helvetica", 14, "bold"), fg="white", bg="#1e1e2f").pack(pady=10)

greet = tk.Label(root, text="", fg="lightgreen", bg="#1e1e2f", font=("Arial", 11))
greet.pack()

entry = tk.Entry(root, textvariable=name_var, font=("Arial", 11))
entry.pack(pady=8)

btn_submit = tk.Button(root, text="Submit Name", command=submit, bg="#61afef", fg="white")
btn_submit.pack()

tk.Label(root, textvariable=song, bg="#1e1e2f", fg="skyblue").pack(pady=10)

btn_load = tk.Button(root, text="🎵 Load Music", command=load, bg="#4CAF50", fg="white", width=20)
btn_play = tk.Button(root, text="▶️ Play", command=play, bg="#2196F3", fg="white", width=20)
btn_stop = tk.Button(root, text="⏹ Stop", command=stop, bg="#f44336", fg="white", width=20)

root.mainloop()