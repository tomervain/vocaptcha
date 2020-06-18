import os
import sys
import threading
import time
import tkinter as tk
from random import sample, shuffle

sys.path.append('..')

import lib.AnimateGif as AG
from lib.asr_module import transcribe_streaming as asr
from lib.qa_generator import generate_qa
from lib.sentence_generator import generate
from lib.speech_rec import record_to_file as rec
from lib.tts_module import text_to_speech as tts
import lib.AudioWave as AW
from playsound import playsound as ps

def draw_fig(fig):
    fig.canvas.draw()
    fig.canvas.flush_events()

project_path = os.path.dirname(os.path.dirname(os.path.abspath(" ")))

def thread_test(aw, intro):

    start_test_thread = threading.Thread(target=lambda:start_test(aw, intro))
    start_test_thread.setDaemon(True)
    start_test_thread.start()

def start_test(aw, intro):

   # ps(project_path + "\\resources\\" + intro + ".mp3")
    aw.play(project_path + "\\resources\\" + intro +".wav")
    sentences = generate()
    qa_pairs = []
    for sentence in sentences:
        qa_pairs += generate_qa(sentence)
    shuffle(qa_pairs)
    pairs = sample(qa_pairs, k=3)

    for s in sentences:
        tts(s.sentence_str, aw)
        time.sleep(1.5)

    for qa in pairs:
        tts(qa[0], aw)
        print("please speak a word into the microphone")
        speak_indicator.config(bg="green")
        rec("user_voice.wav")
        speak_indicator.config(bg="red")
        result = asr("user_voice.wav")
        if result is None:
            aw.play(project_path + "\\resources\\bad_results.wav")
            #ps(project_path + "\\resources\\bad_results.mp3")
        else:
            print(result[0], " == ", qa[1])
            if ''.join(result).lower() == qa[1].lower():
                aw.play(project_path + "\\resources\\correct.wav")
                #ps(project_path + "\\resources\\correct.mp3")

            else:
                aw.play(project_path + "\\resources\\wrong.wav")
              #  ps(project_path + "\\resources\\wrong.mp3")

    print("test finished")


if __name__ == "__main__":
    global speak_indicator

    window = tk.Tk(screenName='VoCAPTCHA Demo')
    window.title("VoCAPTCHA")

    window.iconbitmap(project_path + '\\resources\\vocapcha_icon.ico')

    aw = AW.AudioWave(window, 0, 1, draw_fig)
   # ag = AG.AnimateGif(window, 0, 1)
    greeting = tk.Label(text="Hello, Tkinter", width=60, height=10)
    greeting.grid(row=0, column=0)

# flat, groove, raised, ridge, solid, or sunken
    speak_indicator = tk.Label(text=" ", bg="red", width=60, height=10, relief="solid")
    speak_indicator.grid(row=1, column=1)


    start_btn_long = tk.Button(window, text="Begin Test", command=lambda: thread_test(aw, 'long_intro'))
    start_btn_long.grid(row=2, column=0)

    start_btn_short = tk.Button(window, text="Quick start", command=lambda: thread_test(aw, 'short_intro'))
    start_btn_short.grid(row=2, column=1)

    quit_btn = tk.Button(window, text="Quit", command=window.quit)
    quit_btn.grid(row=2, column=2)


    window.mainloop()
