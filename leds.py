import time
import board
import adafruit_dotstar as dotstar
from ectoleds import breathe
from ectoleds import random_blink
from ectoleds import shooting_dot
from networktables import NetworkTables
from ectoleds import shooting_Star_Reverse

NetworkTables.initialize(server="192.168.1.104")
table = NetworkTables.getTable("Leds")


num_leds = 13
dots = dotstar.DotStar(board.SCK, board.MOSI, num_leds, brightness=0.5, auto_write=False)

breatheEffectB = breathe.Breathe(ledAmount=num_leds, breatheColor=(0, 0, 255))
breatheEffectR = breathe.Breathe(ledAmount=num_leds, breatheColor=(255, 0, 0))
breatheEffectG = breathe.Breathe(ledAmount=num_leds, breatheColor=(0, 255, 0))
breatheEffectY = breathe.Breathe(ledAmount=num_leds, breatheColor=(255, 255, 0))
breatheEffectW = breathe.Breathe(ledAmount=num_leds, breatheColor=(255, 255, 255))
randomBlinkEffectR = random_blink.RandomBlink(ledAmount=num_leds, blinkColor=(150, 150, 0), minBreatheRate= 10, maxBreatheRate= 15)
randomBlinkEffectG = random_blink.RandomBlink(ledAmount=num_leds, blinkColor=(0, 255, 0))
randomBlinkEffectB = random_blink.RandomBlink(ledAmount=num_leds, blinkColor=(0, 0, 255))
randomBlinkEffectY = random_blink.RandomBlink(ledAmount=num_leds, blinkColor=(255, 255, 0))
randomBlinkEffectW = random_blink.RandomBlink(ledAmount=num_leds, blinkColor=(255, 255, 255))
shooting_Star_ReverseR = shooting_Star_Reverse.ShootingReverse(ledAmount=num_leds, blinkColor=(255, 0, 0))
shooting_Star_ReverseG = shooting_Star_Reverse.ShootingReverse(ledAmount=num_leds, blinkColor=(0, 255, 0))
shooting_Star_ReverseB = shooting_Star_Reverse.ShootingReverse(ledAmount=num_leds, blinkColor=(0, 0, 255))



while True:
    targetEffect = table.getNumber("EffectNumber",0)
    if targetEffect == 0:
        breatheEffectR.apply(dots)
        randomBlinkEffectR.apply(dots, respectLedsState=True)
    elif targetEffect == 1:
        breatheEffectB.apply(dots)
        randomBlinkEffectB.apply(dots, respectLedsState=True)
    elif targetEffect == 2:
        breatheEffectG.apply(dots)
        randomBlinkEffectG.apply(dots, respectLedsState=True)
    elif targetEffect == 3:
        breatheEffectY.apply(dots)
        randomBlinkEffectY.apply(dots, respectLedsState=True)

    else:
        dots.fill = 0


    dots.show()

    time.sleep(0.01)
