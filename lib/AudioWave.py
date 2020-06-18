import wave

import pyaudio
import os
import struct
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sys, traceback
import threading
from tkinter import TclError


class AudioWave():

    def __init__(self, parent, row, column, task):

        self.parent = parent
        self.task = task
        self.fig, self.ax = plt.subplots(1, figsize=(7, 4))

        self.canvas = FigureCanvasTkAgg(self.fig, master=parent)
        self.canvas.get_tk_widget().grid(row=row, column=column)

        self.CHUNK = 1024 * 2
        # variable for plotting
        x = np.arange(0, 2 * self.CHUNK, 2)

        # create a line object with random data
        self.line, = self.ax.plot(x, np.random.rand(self.CHUNK), '-', lw=1)

        # basic formatting for the axes
        # ax.set_title('AUDIO WAVEFORM')
        # ax.set_xlabel('samples')
        # ax.set_ylabel('volume')
        self.ax.set_ylim(0, 255)
        self.ax.set_xlim(0, 2 * self.CHUNK)

        plt.setp(self.ax, xticks=[0, self.CHUNK, 2 * self.CHUNK], yticks=[0, 128, 255])

    def play(self, wav_file):
        try:
            p = pyaudio.PyAudio()
            wf = wave.open(wav_file, 'rb')
            stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                            channels=wf.getnchannels(),
                            rate=wf.getframerate(),
                            output=True)

            data = wf.readframes(self.CHUNK)
            is_end_of_file = False
            while not is_end_of_file:

                # binary data
                # data = stream.read(CHUNK)
                stream.write(data)
                data = wf.readframes(self.CHUNK)

                if data.__sizeof__() < self.CHUNK * 2:
                    data_np = np.zeros(data_np.shape) + 128
                    is_end_of_file = True

                else:
                    # convert data to integers, make np array, then offset it by 127
                    data_int = struct.unpack(str(2 * self.CHUNK) + 'B', data)

                    # create np array and offset by 128
                    data_np = np.array(data_int, dtype='b')[::2] + 128

                self.line.set_ydata(data_np)

                # update figure canvas
                try:

                   # lock = threading.Lock()
                  #  lock.acquire(blocking=True)
                    #threading.main_thread()
                    self.parent.after(1, lambda: self.task(self.fig))

                   # self.fig.canvas.draw()
                  #  self.fig.canvas.flush_events()

                 #   lock.acquire(blocking=False)
                 #   lock.release()
                except:
                    print("Exception in user code:")
                    print('-' * 60)
                    traceback.print_exc(file=sys.stdout)
                    print('-' * 60)

            # stop stream

            stream.stop_stream()
            stream.close()

            # close PyAudio
            p.terminate()
            print("audio finished")
        except:
            print("Exception in user code:")
            print('-' * 60)
            traceback.print_exc(file=sys.stdout)
            print('-' * 60)
