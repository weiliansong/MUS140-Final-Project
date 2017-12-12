import audio_tools
import numpy as np
import matplotlib.pyplot as plt

while True:
  fname = raw_input('Save as: ')

  audio_tools.record('./raw/' + fname) 
  y = audio_tools.process_wav('./raw/' + fname)

  offset = len(y) / 4
  middle = len(y) / 2
  cropped_y = y[middle-offset:middle+offset]
  cropped_y = [x for x in cropped_y if x >= 0]
  print("Average: %f" % np.average(cropped_y))

  plt.plot(y)
  plt.savefig('./figs/' + fname + '.png')
  plt.clf()
