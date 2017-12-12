import audio_tools
import matplotlib.pyplot as plt

while True:
  fname = raw_input('Save as: ')

  audio_tools.record('./raw/' + fname) 
  y = audio_tools.process_wav('./raw/' + fname)
  plt.plot(y)
  plt.show()
