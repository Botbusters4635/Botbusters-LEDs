import time
import board
import adafruit_dotstar as dotstar
from ectoleds import breathe

num_leds = 20
dots = dotstar.DotStar(board.SCK, board.MOSI, num_leds, brightness=0.2, auto_write=False)

breatheEffect = breathe.Breathe(ledAmount=num_leds, breatheColor=(0, 0, 255))

while True:
    breatheEffect.apply(dots)
    dots.show()

    time.sleep(0.01)

