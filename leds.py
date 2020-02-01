import time
import board
import adafruit_dotstar as dotstar
from ectoleds import breathe
from ectoleds import random_blink
from ectoleds import shooting_dot
from ectoleds import  shooting_Star_Reverse

num_leds = 13
dots = dotstar.DotStar(board.SCK, board.MOSI, num_leds, brightness=0.5, auto_write=False)

breatheEffect = breathe.Breathe(ledAmount=num_leds, breatheColor=(255, 0, 0))
randomBlinkEffect = random_blink.RandomBlink(ledAmount=num_leds, blinkColor=(255, 0, 0))
shootingdotEffect = shooting_dot.Shooting(ledAmount=num_leds, shootingColor=(0, 0, 50))
shootingDotReverseEffect = shooting_Star_Reverse.ShootingReverse(ledAmount=num_leds, ledColor=(0, 0, 255))

while True:
    # breatheEffect.apply(dots)
    # randomBlinkEffect.apply(dots, respectLedsState=True)
    #shootingdotEffect.apply(dots)
    shootingDotReverseEffect.apply(dots)

    dots.show()

    time.sleep(0.01)
