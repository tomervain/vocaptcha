import tkinter as tk
import time
import sys

sys.path.append('..')
from lib.sentence_generator import generate
from lib.qa_generator import generate_qa
from lib.tts_module import text_to_speech as tts
from lib.asr_module import transcribe_streaming as asr
from lib.speach_rec import record_to_file as rec
from playsound import playsound as ps

import lib.AnimateGif as AG
import threading

from random import shuffle, sample
import os

project_path = os.path.dirname(os.path.dirname(os.path.abspath(" ")))

def thread_test(ag, intro):

    start_test_thread = threading.Thread(target=lambda:start_test(ag, intro))
    start_test_thread.setDaemon(True)
    start_test_thread.start()

def start_test(ag, intro):

    ps(project_path + "\\resources\\" + intro + ".mp3")

    sentences = generate()
    qa_pairs = []
    for sentence in sentences:
        qa_pairs += generate_qa(sentence)
    shuffle(qa_pairs)
    pairs = sample(qa_pairs, k=3)

    for s in sentences:
        tts(s.sentence_str)
        time.sleep(1.5)

    for qa in pairs:
        ag.set_audio_wave()
        tts(qa[0])
        ag.set_mic_on()
        print("please speak a word into the microphone")
        rec("user_voice.wav")
        result = asr("user_voice.wav")
        ag.set_audio_wave()
        if result is None:
            ps(project_path + "\\resources\\bad_results.mp3")
        else:
            print(result[0], " == ", qa[1])
            if ''.join(result).lower() == qa[1].lower():
                ps(project_path + "\\resources\\correct.mp3")

            else:
                ps(project_path + "\\resources\\wrong.mp3")

    print("test finished")


if __name__ == "__main__":
    window = tk.Tk(screenName='VoCAPTCHA Demo')
    window.title("VoCAPTCHA")

    window.iconbitmap(project_path + '\\resources\\vocapcha_icon.ico')

    ag = AG.AnimateGif(window, 0, 1)
    greeting = tk.Label(text="Hello, Tkinter", width=60, height=10)
    greeting.grid(row=0, column=0)

    start_btn_long = tk.Button(window, text="Begin Test", command=lambda: thread_test(ag, 'long_intro'))
    start_btn_long.grid(row=1, column=0)

    start_btn_short = tk.Button(window, text="Quick start", command=lambda: thread_test(ag, 'short_intro'))
    start_btn_short.grid(row=1, column=1)

    quit_btn = tk.Button(window, text="Quit", command=window.quit)
    quit_btn.grid(row=1, column=2)


    window.mainloop()
