import tkinter as tk
import time
import sys

sys.path.append('..')
from lib.sentence_generator import generate
from lib.qa_generator import generate_qa
from lib.tts_module import text_to_speech as tts
from lib.asr_module import transcribe_streaming as asr
from lib.speech_rec import record_to_file as rec

from random import shuffle, sample
import os
import threading


def start_test():
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
        tts(qa[0])
        print("please speak a word into the microphone")
        rec("user_voice.wav")
        result = asr("user_voice.wav")
        

        if result is None:
            tts("Sorry but i dont understand")
        else:
            print(result[0], " == ", qa[1])
            if ''.join(result).lower() == qa[1].lower():
                tts("that is correct!")
            else:
                tts("that is wrong!")



if __name__ == "__main__":
    window = tk.Tk(screenName='VoCAPTCHA Demo')
    window.title("VoCAPTCHA")

    project_path = os.path.dirname(os.path.dirname(os.path.abspath(" ")))
    window.iconbitmap(project_path + '\\resources\\vocapcha_icon.ico')

    greeting = tk.Label(text="Hello, Tkinter", width=60, height=10)
    greeting.grid(row=0, column=0)

    start_test_thread = threading.Thread(target=start_test)
    start_test_thread.setDaemon(True)
    start_btn = tk.Button(window, text="Begin Test", command=start_test_thread.start)
    start_btn.grid(row=1, column=0)

    quit_btn = tk.Button(window, text="Quit", command=window.quit)
    quit_btn.grid(row=1, column=1)

    window.mainloop()
