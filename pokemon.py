import keyboard
import PIL

from pyboy import PyBoy
pyboy = PyBoy("Pokemon Red.gb")
with open("hackclub.state","rb") as e:
    pyboy.load_state(e)
pyboy.set_emulation_speed(60)
pyboy.tick(240)
a = pyboy.screen.ndarray
d = PIL.Image.fromarray(a)
d.save("a.png")
while True:
    pyboy.tick()