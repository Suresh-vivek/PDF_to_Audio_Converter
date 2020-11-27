from pydub import AudioSegment
from tkinter import Tk
from tkinter.filedialog import askopenfilename


Tk().withdraw()
filename=askopenfilename()
print(filename)

src=filename
dst="final.mp3"
sound = AudioSegment.from_wav(src)
sound.export(dst, format="mp3")
