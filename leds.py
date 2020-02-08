import time
import board
import adafruit_dotstar as dotstar
from ectoleds import breathe
from ectoleds import random_blink
from ectoleds import shooting_dot
from ectoleds import dotstar_segment
from networktables import NetworkTables

NetworkTables.initialize(server="10.46.35.2")
table = NetworkTables.getTable("LedsManager")

num_leds = 90
dots = dotstar.DotStar(board.SCK, board.MOSI, num_leds, brightness=1.0, auto_write=False)
outer_left = dotstar_segment.DotstarSegment(dots, 0, 24)
inner_left = dotstar_segment.DotstarSegment(dots, 25, 45, True)
inner_right = dotstar_segment.DotstarSegment(dots, 45, 65)
outer_right = dotstar_segment.DotstarSegment(dots, 65, 90, True)


breatheEffect = breathe.Breathe(ledAmount=num_leds, breatheColor=(0, 255, 0))
randomBlinkEffect = random_blink.RandomBlink(ledAmount=num_leds, blinkColor=(0, 255, 0), minBreatheRate=10,
                                             maxBreatheRate=15)
shootingDotEffectOuterL = shooting_dot.Shooting(ledAmount=outer_left.length, shootingColor=(255, 0, 0))
shootingDotEffectInnerL = shooting_dot.Shooting(ledAmount=inner_left.length, shootingColor=(255, 0, 0))
shootingDotEffectInnerR = shooting_dot.Shooting(ledAmount=inner_right.length, shootingColor=(255, 0, 0))
shootingDotEffectOuterR = shooting_dot.Shooting(ledAmount=outer_right.length, shootingColor=(255, 0, 0))

while True:
    targetEffect = table.getNumber("EffectNumber", 0)
    rColorBreathe = table.getNumber("Breathe/R", 0)
    gColorBreathe = table.getNumber("Breathe/G", 255)
    bColorBreathe = table.getNumber("Breathe/B", 0)
    rColorRandom = table.getNumber("Blink/R", 0)
    gColorRandom = table.getNumber("Blink/G", 255)
    bColorRandom = table.getNumber("Blink/B", 0)
    breathColor = (rColorBreathe, gColorBreathe, bColorBreathe)
    blinkColor = (rColorRandom, gColorRandom, bColorRandom)
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
    elif targetEffect == 3:
        shootingDotEffectOuterL.apply(outer_left)
        shootingDotEffectInnerL.apply(inner_left)
        shootingDotEffectInnerR.apply(inner_right)
        shootingDotEffectOuterR.apply(outer_right)
    else:
        dots.fill = 0

    dots.show()

    time.sleep(0.01)
