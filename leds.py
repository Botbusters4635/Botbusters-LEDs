import time
import board
import adafruit_dotstar as dotstar
from ectoleds import breathe
from ectoleds import random_blink
from ectoleds import shooting_dot
from ectoleds import dotstar_segment
from networktables import NetworkTables
from ectoleds import fire
from adafruit_fancyled.adafruit_fancyled import CRGB

NetworkTables.initialize(server="10.46.35.2")
table = NetworkTables.getTable("LedsManager")

num_leds = 90
dots = dotstar.DotStar(board.SCK, board.MOSI, num_leds, brightness=1.0, auto_write=False)
dots.fill((0,0,0))

outer_left = dotstar_segment.DotstarSegment(dots, 0, 24)
inner_left = dotstar_segment.DotstarSegment(dots, 25, 44, True)
inner_right = dotstar_segment.DotstarSegment(dots, 45, 64)
outer_right = dotstar_segment.DotstarSegment(dots, 65, 89, True)


breatheEffect = breathe.Breathe(ledAmount=num_leds, breatheColor=(0, 255, 0))
randomBlinkEffect = random_blink.RandomBlink(ledAmount=num_leds, blinkColor=(0, 255, 0), minBreatheRate=20,
                                             maxBreatheRate=30)
shootingDotEffectOuterL = shooting_dot.Shooting(ledAmount=outer_left.length, shootingColor=(255, 0, 0))
shootingDotEffectInnerL = shooting_dot.Shooting(ledAmount=inner_left.length, shootingColor=(255, 0, 0))
shootingDotEffectInnerR = shooting_dot.Shooting(ledAmount=inner_right.length, shootingColor=(255, 0, 0))
shootingDotEffectOuterR = shooting_dot.Shooting(ledAmount=outer_right.length, shootingColor=(255, 0, 0))


# RED
firePalleteRed = [
    CRGB(0, 0, 0),
    CRGB(255, 0, 0),  
    CRGB(255, 150, 0)]

#  Blue
firePalleteBlue = [
    CRGB(0, 0, 0),
    CRGB(0, 0, 255),  
    CRGB(0, 255, 255),     
    CRGB(255, 255, 255)]

fireEffectOL = fire.FireEffect(led_amount=outer_left.length, palette=firePalleteRed)
fireEffectIL = fire.FireEffect(led_amount=inner_left.length, palette=firePalleteBlue)
fireEffectIR = fire.FireEffect(led_amount=inner_right.length, palette=firePalleteBlue)
fireEffectOR = fire.FireEffect(led_amount=outer_right.length, palette=firePalleteRed)

table.putNumber("EffectNumber", 0)
table.putNumber("Breathe/R", 0)
table.putNumber("Breathe/G", 255)
table.putNumber("Breathe/B", 255)
table.putNumber("Blink/R", 0)
table.putNumber("Blink/G", 255)
table.putNumber("Blink/B", 0)
table.putNumber("BreatheRate", 0.5)

while True:
    targetEffect = table.getNumber("EffectNumber", 0)
    targetEffect = 4
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
    elif targetEffect == 4:
        fireEffectOL.apply(outer_left)
        fireEffectIL.apply(inner_left)
        fireEffectIR.apply(inner_right)
        fireEffectOR.apply(outer_right)

    else:
        dots.fill = 0

    dots.show()

    time.sleep(0.01)
