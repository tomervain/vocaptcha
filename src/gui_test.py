import tkinter as tk
from lib.sentence_generator import generate
from lib.qa_generator import generate_qa
from lib.tts_module import text_to_speech as tts
from lib.asr_module import transcribe_streaming as asr
from lib.speach_rec import record_to_file as rec
import os

def start_test():
    sentences = generate()
    qa_pairs = []
    for sentence in sentences:
        qa_pairs += generate_qa(sentence)

    for sentence, qa in zip(sentences, qa_pairs):
        tts(sentence.sentence_str)
        tts(qa[0])

        print("please speak a word into the microphone")
        rec("user_voice.wav")
        result = asr("user_voice.wav")

        print(*result, " == ", qa[1])
        if ''.join(result) == qa[1]:
            tts("good boy")
        else:
            tts("very bad")



if __name__ == "__main__":
    window = tk.Tk(screenName='VoCAPTCHA Demo')
    window.title("VoCAPTCHA")

    project_path = os.path.dirname(os.path.dirname(os.path.abspath(" ")))
    window.iconbitmap(project_path + '\\resources\\vocapcha_icon.ico')

    greeting = tk.Label(text="Hello, Tkinter", width=60, height=10)
    greeting.grid(row=0, column=0)

    start_btn = tk.Button(window, text="Begin Test", command=start_test)
    start_btn.grid(row=1, column=0)

    quit_btn = tk.Button(window, text="Quit", command=window.quit)
    quit_btn.grid(row=1, column=1)

    window.mainloop()