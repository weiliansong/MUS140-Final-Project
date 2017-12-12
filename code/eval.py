import numpy as np
import audio_tools

def process_folder(folder):
  print(folder)

  files = ['ambient.mp3', '500.mp3', '2000.mp3', '4000.mp3']

  for f in files:
    path = folder + f

    y = audio_tools.process_wav(path)
    y = [x for x in y if x >= 0]

    print('\t%11s: %f' % (f, np.average(y)))

process_folder('./raw/medium/')
process_folder('./raw/large/')
