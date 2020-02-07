import time
import board
import adafruit_dotstar as dotstar
from ectoleds import breathe
from ectoleds import random_blink
from ectoleds import shooting_dot
from networktables import NetworkTables

NetworkTables.initialize(server="10.46.35.2")
table = NetworkTables.getTable("LedsManager")


num_leds = 90
dots = dotstar.DotStar(board.SCK, board.MOSI, num_leds, brightness=1.0, auto_write=False)
breatheEffect = breathe.Breathe(ledAmount=num_leds, breatheColor=(0, 255, 0))
randomBlinkEffect = random_blink.RandomBlink(ledAmount=num_leds, blinkColor=(0, 255, 0), minBreatheRate= 10, maxBreatheRate= 15)

while True:
    targetEffect = table.getNumber("EffectNumber",0)
    rColorBreathe = table.getNumber("Breathe/R", 0)
    gColorBreathe = table.getNumber("Breathe/G", 255)
    bColorBreathe = table.getNumber("Breathe/B", 0)
    rColorRandom = table.getNumber("Blink/R", 0)
    gColorRandom = table.getNumber("Blink/G", 255)
    bColorRandom = table.getNumber("Blink/B", 0)
    breathColor = (rColorBreathe, gColorBreathe, bColorBreathe)
    blinkColor = (rColorRandom,gColorRandom, bColorRandom)
    breatheEffect.breatheColor = breathColor
    randomBlinkEffect.blinkColor = blinkColor
    breatheEffect.breatheHelper.breatheRate = table.getNumber("BreatheRate", 0.5)


    if targetEffect == 0:
        breatheEffect.apply(dots)
    elif targetEffect == 1:
        randomBlinkEffect.apply(dots)
    elif targetEffect == 2:
        breatheEffect.apply(dots)
        randomBlinkEffect.apply(dots, respectLedsState=True)
    else:
        dots.fill = 0


    dots.show()

    time.sleep(0.01)
