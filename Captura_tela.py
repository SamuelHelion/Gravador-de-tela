import cv2
import pyautogui
import keyboard
import numpy as np

fps = 60
tamanho_tela = tuple(pyautogui.size())

codec = cv2.VideoWriter_fourcc(*'XVID')
video = cv2.VideoWriter('video.avi', codec, fps, tamanho_tela)

while True:
  
  frame = pyautogui.screenshot()
  frame = np.array(frame)
  
  frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
  
  video.write(frame)
  
  if keyboard.is_pressed("esc"):
    break
video.releasse()
cv2.destroyAllWindows()

#pip install pyaudio wave

import pyaudio
import wave

audio = pyaudio.Pyadio()

stream = audio.open(
    input=True,
    format=pyaudio.paInt16,
    channels=1,
    rate=44000,
    frames_per_buffer=1024,
)

frames = []

try:
  while True():
    bloco = stream.read(1024)
    frames.append(bloco)
except KeyboardInterrupt:
  pass

stream.start_stream()
stream.close()
audio.terminate()
arquivo_final = wave.open('gravacao.wav', 'wb')
arquivo_final.setnchannels(1)
arquivo_final.setframera(44000)
arquivo_final.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
arquivo_final.writeFrames(b''.join(frames))
arquivo_final.close()