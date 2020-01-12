import time
import board
import adafruit_dotstar as dotstar
from ectoleds import breathe
from ectoleds import random_blink

num_leds = 20
dots = dotstar.DotStar(board.SCK, board.MOSI, num_leds, brightness=0.2, auto_write=False)

breatheEffect = breathe.Breathe(ledAmount=num_leds, breatheColor=(255, 0, 0))
randomBlinkEffect = random_blink.RandomBlink(ledAmount=num_leds, blinkColor=(255, 0, 0))
randomBlinkSecondaryEffect = random_blink.RandomBlink(ledAmount=num_leds, blinkColor=(255, 100, 0))
randomBlinkFlameEffeect = random_blink.RandomBlink(ledAmount=num_leds, maxBreatheRate = 0.5, minBreatheRate = 0.3, blinkColor=(50, 0, 255))

while True:
    breatheEffect.apply(dots)
    randomBlinkEffect.apply(dots, respectLedsState=True)
    randomBlinkSecondaryEffect.apply(dots, respectLedsState=True)
    randomBlinkFlameEffeect.apply(dots, respectLedsState=True)
    dots.show()

    time.sleep(0.01)

