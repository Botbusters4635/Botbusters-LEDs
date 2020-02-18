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

outer_left = dotstar_segment.DotstarSegment(dots, 0, 23)
inner_left = dotstar_segment.DotstarSegment(dots, 24, 43, True)
inner_right = dotstar_segment.DotstarSegment(dots, 44, 63)
outer_right = dotstar_segment.DotstarSegment(dots, 64, 88, True)


breatheEffect = breathe.Breathe(ledAmount=num_leds, breatheColor=(0, 255, 0))
randomBlinkEffect = random_blink.RandomBlink(ledAmount=num_leds, blinkColor=(0, 255, 0), minBreatheRate=20,
                                             maxBreatheRate=30)
shootingDotEffect = shooting_dot.Shooting(ledAmount=num_leds, shootingColor=(0, 255, 0))
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
    CRGB(0, 255, 255)]

# Green
firePalleteGreen = [
    CRGB(0, 0, 0),
    CRGB(0, 255, 0),  
    CRGB(150, 255, 0)]

fireEffectOL = fire.FireEffect(led_amount=outer_left.length, palette=firePalleteGreen)
fireEffectIL = fire.FireEffect(led_amount=inner_left.length, palette=firePalleteGreen)
fireEffectIR = fire.FireEffect(led_amount=inner_right.length, palette=firePalleteGreen)
fireEffectOR = fire.FireEffect(led_amount=outer_right.length, palette=firePalleteGreen)

table.putNumber("EffectNumber", 0)
table.putNumber("BreatheRate", 0.5)
table.putNumber("FirePallete", 0)
table.putBoolean("RespectedLetsState", False)
table.putString("First/Effect", "breathe")
table.putString("Second/Effect", "randomBlink")
table.putNumber("First/R", 0)
table.putNumber("First/G", 0)
table.putNumber("First/B", 0)
table.putNumber("Second/R", 0)
table.putNumber("Second/G", 0)
table.putNumber("Second/B", 0)

firstEffect = breatheEffect
secondEffect = randomBlinkEffect


while True:
    targetEffect = table.getNumber("EffectNumber", 4)
    firePalleteNumber = table.getNumber("FirePallete", 0)
    breatheEffect.breatheHelper.breatheRate = table.getNumber("BreatheRate", 0.5)

    firstEffect = table.getString("First/Effect", "breathe")
    secondEffect = table.getString("Second/Effect", "randomBlink")
    respectedState = table.getBoolean("RespectedLedsState", False)
    rColorFirst = table.getNumber("First/R", 0)
    gColorFirst = table.getNumber("First/G", 0)
    bColorFirst = table.getNumber("First/B", 0)
    rColorSecond = table.getNumber("Second/R", 0)
    gColorSecond = table.getNumber("Second/G", 0)
    bColorSecond = table.getNumber("Second/B", 0)

    if firstEffect == "breathe":
        firstEffect = breatheEffect
    elif firstEffect == "randomBlink":
        firstEffect = randomBlinkEffect
    elif firstEffect == "shootingDot":
        firstEffect = shootingDotEffect
    else:
        firstEffect = None

    if secondEffect == "breathe":
        secondEffect = breatheEffect
    elif secondEffect == "randomBlink":
        secondEffect = randomBlinkEffect
    elif secondEffect == "shootingDot":
        secondEffect = shootingDotEffect
    else:
        secondEffect = None

    if firePalleteNumber == 0:
        fireEffectOL.palette = firePalleteGreen 
        fireEffectIL.palette = firePalleteGreen 
        fireEffectIR.palette = firePalleteGreen 
        fireEffectOR.palette = firePalleteGreen 
    elif firePalleteNumber == 1:
        fireEffectOL.palette = firePalleteRed 
        fireEffectIL.palette = firePalleteRed 
        fireEffectIR.palette = firePalleteRed 
        fireEffectOR.palette = firePalleteRed 
    elif firePalleteNumber == 2:
        fireEffectOL.palette = firePalleteBlue 
        fireEffectIL.palette = firePalleteBlue 
        fireEffectIR.palette = firePalleteBlue 
        fireEffectOR.palette = firePalleteBlue
    else:
        fireEffectOL.palette = firePalleteGreen 
        fireEffectIL.palette = firePalleteGreen 
        fireEffectIR.palette = firePalleteGreen 
        fireEffectOR.palette = firePalleteGreen

    if targetEffect == 0:
        fireEffectOL.apply(outer_left)
        fireEffectIL.apply(inner_left)
        fireEffectIR.apply(inner_right)
        fireEffectOR.apply(outer_right)
    elif targetEffect == 1:
        if firstEffect is not None:
            firstEffect.color = (rColorFirst, gColorFirst, bColorFirst)
            firstEffect.apply(dots)
        if secondEffect is not None:
            secondEffect.color = (rColorSecond, gColorSecond, bColorSecond)
            secondEffect.apply(dots, respectLedsState= respectedState)
    else:
        dots.fill = 0

    dots.show()

    time.sleep(0.01)
