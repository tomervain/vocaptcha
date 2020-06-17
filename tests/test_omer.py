import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
import os

# TigerhawkT3

project_path = os.path.dirname(os.path.dirname(os.path.abspath(" ")))
mic_on_path = project_path + '\\resources\\mic_on.gif'
audio_wave_path = project_path + '\\resources\\audio_wave.gif'


class AnimateGif:
    def __init__(self, parent, row, column):
        self.parent = parent
        self.canvas = tk.Canvas(parent, width=400, height=400)
        self.canvas.grid(row=row, column=column)

        self.image_mic_on = [ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(Image.open(mic_on_path))]
        self.image_audio_wave = [ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(Image.open(audio_wave_path))]

        self.image_gif = self.image_audio_wave.copy()
        self.delay_time = 50

        self.image = self.canvas.create_image(200, 200, image=self.image_gif[0])
        self.animate(1)

    def animate(self, counter):
        self.canvas.itemconfig(self.image, image=self.image_gif[counter])
        self.parent.after(self.delay_time, lambda: self.animate((counter + 1) % len(self.image_gif)))

    def set_mic_on(self):
        self.image_gif = self.image_mic_on.copy()
        self.delay_time = 250

    def set_audio_wave(self):
        self.image_gif = self.image_audio_wave.copy()
        self.delay_time = 50


root = tk.Tk()
app = AnimateGif(root, 0, 0)

start_btn = tk.Button(root, text="Begin Test", command=app.set_mic_on)
start_btn.grid(row=1, column=1)



root.mainloop()
