import os
import sys
import threading
import time
import spacy
import tkinter as tk
from fuzzywuzzy import fuzz
from random import sample, shuffle
from playsound import playsound as ps

sys.path.append('..')

import lib.AnimateGif as AG
from lib.asr_module import transcribe_streaming as asr
from lib.qa_generator import generate_qa
from lib.sentence_generator import generate
from lib.speach_rec import record_to_file as rec
from lib.tts_module import text_to_speech as tts

nlp = spacy.load('en_core_web_sm')


def thread_test(ag, intro):
    start_test_thread = threading.Thread(target=lambda: start_test(ag, intro))
    start_test_thread.setDaemon(True)
    start_test_thread.start()

def preprocess(s):
    s = s.lower()
    doc = nlp(s)
    words = [t.text for t in doc if not t.is_stop]
    return ' '.join(words)


def start_test(ag, intro):

    ps(f'../resources/{intro}.mp3')

    sentences = generate()
    qa_pairs = []
    for sentence in sentences:
        qa_pairs += generate_qa(sentence)
    shuffle(qa_pairs)
    pairs = sample(qa_pairs, k=3)

    for s in sentences:
        tts(s.sentence_str)
        time.sleep(2)

    for qa in pairs:
        ag.set_audio_wave()
        tts(qa[0])
        ag.set_mic_on()
        print("please speak a word into the microphone")
        rec("user_voice.wav")
        result = asr("user_voice.wav")
        ag.set_audio_wave()
        if result is None:
            tts("Sorry but i dont understand")
        else:
            print('before preprocess:', result[0], " == ", qa[1])
            res = preprocess(result[0])
            ans = preprocess(qa[1])
            print('after preprocess:', res, " == ", ans)
            if fuzz.ratio(res, ans) >= 90:
                tts("that is correct!")
            else:
                tts("that is wrong!")

    print("test finished")


if __name__ == "__main__":
    window = tk.Tk()
    window.title("VoCAPTCHA")
    window.iconbitmap('../resources/vocapcha_icon.ico')

    ag = AG.AnimateGif(window, 0, 1)
    greeting = tk.Label(text="Hello, Tkinter", width=60, height=10)
    greeting.grid(row=0, column=0)

    start_btn = tk.Button(window, text="Begin Test",
                          command=lambda: thread_test(ag, 'long_intro'))
    start_btn.grid(row=1, column=0)

    start_btn_short = tk.Button(
        window, text="Quick start", command=lambda: thread_test(ag, 'short_intro'))
    start_btn_short.grid(row=1, column=1)

    quit_btn = tk.Button(window, text="Quit", command=window.quit)
    quit_btn.grid(row=1, column=2)

    window.mainloop()
