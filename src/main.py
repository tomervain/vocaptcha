import os
import sys
import threading
import time
import spacy
import tkinter as tk
from fuzzywuzzy import fuzz
from random import sample, shuffle
import ctypes

sys.path.append('..')

import lib.AnimateGif as AG
from lib.AudioWave import AudioWave
from lib.asr_module import transcribe_streaming as asr
from lib.qa_generator import generate_qa
from lib.sentence_generator import generate
from lib.speech_rec import record_to_file as rec
from lib.tts_module import text_to_speech as tts

nlp = spacy.load('en_core_web_sm')

def draw_fig(fig):
    fig.canvas.draw()
    fig.canvas.flush_events()

def thread_test(ag, intro):
    start_test_thread = threading.Thread(target=lambda: start_test(ag, intro))
    start_test_thread.setDaemon(True)
    start_test_thread.start()

def preprocess(s):
    s = s.lower()
    doc = nlp(s)
    words = [t.text for t in doc if not t.is_stop]
    return ' '.join(words)


def start_test(aw, intro):

    aw.play(f'../resources/{intro}.wav')

    sentences = generate()
    qa_pairs = []
    for sentence in sentences:
        qa_pairs += generate_qa(sentence)
    shuffle(qa_pairs)
    pairs = sample(qa_pairs, k=3)

    for s in sentences:
        text_label.config(text=text_label.cget("text") + "\n" + s.sentence_str)
        tts(s.sentence_str, aw)
        time.sleep(2)

    for qa in pairs:
        tts(qa[0], aw)

        is_result_ok = False
        tries = 0
        while not is_result_ok and tries < 3:
            print("please speak a word into the microphone")
            speak_indicator.config(bg="green")
            rec("user_voice.wav")
            speak_indicator.config(bg="red")

            result, confidence = asr("user_voice.wav")
            print('Confidence:', confidence)
            if len(result) == 0:
                aw.play(f'../resources/bad_result.wav')
            elif confidence < 0.8:
                aw.play(f'../resources/bad_result.wav')
            else:
                is_result_ok = True
            tries += 1

        print('before preprocess:', result[0], " == ", qa[1])
        res = preprocess(result[0])
        ans = preprocess(qa[1])
        print('after preprocess:', res, " == ", ans)
        if fuzz.ratio(res, ans) >= 90:
            aw.play(f'../resources/correct.wav')
        elif tries < 3:
            aw.play(f'../resources/wrong.wav')

    text_label.config(text="")
    print("test finished")


if __name__ == "__main__":
    global speak_indicator, text_label

    user32 = ctypes.windll.user32
    screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

    window = tk.Tk()
    window.title("VoCAPTCHA")
    window.iconbitmap('../resources/vocapcha_icon.ico')

    window.minsize(width=int(screensize[0] / 2), height=int(screensize[1] / 2))
    # window.tk.call('tk', 'scaling', screensize[0]/1000)
    user = os.getenv('username')
    if user == 'tomer':
        window.tk.call('tk', 'scaling', 4.0)

    ag = AudioWave(window, draw_fig)
    text_label = tk.Label(text="", relief="solid")
    text_label.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    # flat, groove, raised, ridge, solid, or sunken
    speak_indicator = tk.Label(text="Indicator", font="bold", bg="red", relief="solid")
    speak_indicator.pack(side=tk.RIGHT, fill=tk.BOTH, expand=1)

    start_btn = tk.Button(window, text="Begin Test",
                          command=lambda: thread_test(ag, 'long_intro'))
    start_btn.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    start_btn_short = tk.Button(
        window, text="Quick start", command=lambda: thread_test(ag, 'short_intro'))
    start_btn_short.pack(fill=tk.BOTH, expand=1)

    quit_btn = tk.Button(window, text="Quit", command=window.quit)
    quit_btn.pack(side=tk.RIGHT, fill=tk.BOTH, expand=1)

    window.mainloop()