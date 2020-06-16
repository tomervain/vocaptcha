from lib.tts_module import text_to_speech
from lib.asr_module import transcribe_streaming
from lib.speach_rec import record_to_file
from lib.asr_module import sample_recognize
from lib.asr_module import stt
import soundfile as sf

import argparse





#data, samplerate = sf.read('Dennis saw a monkey.mp3')
#sf.write('demo.wav', data, samplerate)

#text_to_speech("Austin got a beautiful garden")
#text_to_speech("What does Austin got that is beautiful?")
print("please speak a word into the microphone")
record_to_file('demo.wav')


ob = sf.SoundFile("demo.wav")
print("rate = ", ob.samplerate)
print("channels = ", ob.channels)
print("subtype = ", ob.subtype)


text = transcribe_streaming('demo.wav')
print("text=", text)
#stt('demo.wav')
#sample_recognize("Dennis saw a monkey.wav")