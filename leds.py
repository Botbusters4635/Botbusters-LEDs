import time
import board
import adafruit_dotstar as dotstar
from ectoleds import breathe
from ectoleds import random_blink

num_leds = 20
dots = dotstar.DotStar(board.SCK, board.MOSI, num_leds, brightness=0.2, auto_write=False)

breatheEffect = breathe.Breathe(ledAmount=num_leds, breatheColor=(0, 0, 255))
randomBlinkEffect = random_blink.RandomBlink(ledAmount=num_leds, blinkColor=(255, 0, 0))
randomBlinkSecondaryEffect = random_blink.RandomBlink(ledAmount=num_leds, blinkColor=(255, 100, 0))

while True:
    randomBlinkEffect.apply(dots)
    randomBlinkSecondaryEffect.apply(dots)
    dots.show()

    time.sleep(0.01)

