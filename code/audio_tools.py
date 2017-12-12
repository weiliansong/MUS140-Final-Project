import tensorflow as tf
import wave
import random
import pyaudio
import numpy as np

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44199
RECORD_SECONDS = 10

d = 400000 # number of audio samples for learning

def process_wav(fname):
    fid = wave.open(fname, "rb")
    raw = fid.readframes(fid.getnframes())
    y = np.fromstring(raw,dtype=np.int16).astype(np.float32)
    y = y / 32768.

    return y

def record(fname):
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print 'Started Recording!'
    
    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print 'Finished Recording!'

    stream.stop_stream()
    stream.close()

    p.terminate()
    
    wf = wave.open(fname, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

def play(fname):
    wf = wave.open(fname, 'rb')

    p = pyaudio.PyAudio()

    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    data = wf.readframes(CHUNK)

    while data != '':
        stream.write(data)
        data = wf.readframes(CHUNK)

    stream.stop_stream()
    stream.close()

    p.terminate()
