import time
import board
import adafruit_dotstar as dotstar
from ectoleds import breathe
from ectoleds import random_blink
from ectoleds import shooting_dot
from ectoleds import dotstar_segment
from ectoleds import fill_stripe
from ectoleds import fire
from ectoleds import mario_star
from ectoleds import circles
from networktables import NetworkTables
from adafruit_fancyled.adafruit_fancyled import CRGB

NetworkTables.initialize(server="10.46.35.2")
table = NetworkTables.getTable("LedsManager")

num_leds = 90
dots = dotstar.DotStar(board.SCK, board.MOSI, num_leds, brightness=1.0, auto_write=False)
dots.fill((0, 0, 0))

outer_left = dotstar_segment.DotstarSegment(dots, 0, 23)
inner_left = dotstar_segment.DotstarSegment(dots, 24, 43, True)
inner_right = dotstar_segment.DotstarSegment(dots, 44, 63)
outer_right = dotstar_segment.DotstarSegment(dots, 64, 88, True)

inverse_outer_left = dotstar_segment.DotstarSegment(dots, 0, 23, True)
inverse_inner_left = dotstar_segment.DotstarSegment(dots, 24, 43)
inverse_inner_right = dotstar_segment.DotstarSegment(dots, 44, 63, True)
inverse_outer_right = dotstar_segment.DotstarSegment(dots, 64, 88)

left_circle = dotstar_segment.DotstarSegment(dots, 0, 43, inverted=False)
right_circle = dotstar_segment.DotstarSegment(dots, 44, 88, inverted=True)

breatheEffect = breathe.Breathe(ledAmount=num_leds, breatheColor=(0, 255, 0))
randomBlinkEffect = random_blink.RandomBlink(ledAmount=num_leds, blinkColor=(0, 255, 0), minBreatheRate=20,
                                             maxBreatheRate=30)

fill_stripe_effect_outer_left = fill_stripe.FillStripe(ledAmount=outer_left.length, Background_Color=(0, 255, 255),
                                                       dotColor=(255, 30, 0))
fill_stripe_effect_inner_left = fill_stripe.FillStripe(ledAmount=inner_left.length, Background_Color=(0, 255, 255),
                                                       dotColor=(255, 30, 0))
fill_stripe_effect_inner_right = fill_stripe.FillStripe(ledAmount=inner_right.length, Background_Color=(0, 255, 255),
                                                        dotColor=(255, 30, 0))
fill_stripe_effect_outer_right = fill_stripe.FillStripe(ledAmount=outer_right.length, Background_Color=(0, 255, 255),
                                                        dotColor=(255, 30, 0))

shootingDotEffectOuterL = shooting_dot.Shooting(ledAmount=outer_left.length, shootingColor=(255, 0, 0))
shootingDotEffectInnerL = shooting_dot.Shooting(ledAmount=inner_left.length, shootingColor=(255, 0, 0))
shootingDotEffectInnerR = shooting_dot.Shooting(ledAmount=inner_right.length, shootingColor=(255, 0, 0))
shootingDotEffectOuterR = shooting_dot.Shooting(ledAmount=outer_right.length, shootingColor=(255, 0, 0))

mario_star_effect = mario_star.MarioStar(ledAmount=num_leds, ledColor=(0, 0, 0))

circle_effect_right = circles.Circles(ledAmount=right_circle.length, Background_Color=(0, 0, 0), dotColor=(255, 0, 0))
circle_effect_left = circles.Circles(ledAmount=left_circle.length, Background_Color=(0, 0, 0), dotColor=(255, 0, 0))

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

table.putNumber("EffectNumber", 9)
table.putNumber("Breathe/R", 0)
table.putNumber("Breathe/G", 255)
table.putNumber("Breathe/B", 255)
table.putNumber("Blink/R", 0)
table.putNumber("Blink/G", 255)
table.putNumber("Blink/B", 0)
table.putNumber("BreatheRate", 0.5)
table.putNumber("FirePallete", 0)

while True:
    targetEffect = table.getNumber("EffectNumber", 4)
    rColorBreathe = table.getNumber("Breathe/R", 0)
    gColorBreathe = table.getNumber("Breathe/G", 255)
    bColorBreathe = table.getNumber("Breathe/B", 0)
    rColorRandom = table.getNumber("Blink/R", 0)
    gColorRandom = table.getNumber("Blink/G", 255)
    bColorRandom = table.getNumber("Blink/B", 0)
    firePalleteNumber = table.getNumber("FirePallete", 0)
    breathColor = (rColorBreathe, gColorBreathe, bColorBreathe)
    blinkColor = (rColorRandom, gColorRandom, bColorRandom)
    breatheEffect.breatheColor = breathColor
    randomBlinkEffect.blinkColor = blinkColor
    breatheEffect.breatheHelper.breatheRate = table.getNumber("BreatheRate", 0.5)

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
    elif targetEffect == 5:
        fill_stripe_effect_outer_left.apply(outer_left)
        fill_stripe_effect_inner_left.apply(inner_left)
        fill_stripe_effect_inner_right.apply(inner_right)
        fill_stripe_effect_outer_right.apply(outer_right)
    elif targetEffect == 6:
        mario_star_effect.apply(dots)
    elif targetEffect == 7:
        circle_effect_left.apply(left_circle)
        circle_effect_right.apply(right_circle)
    elif targetEffect == 8:
        fill_stripe_effect_outer_left.apply(inverse_outer_left)
        fill_stripe_effect_inner_left.apply(inverse_inner_left)
        fill_stripe_effect_inner_right.apply(inverse_inner_right)
        fill_stripe_effect_outer_right.apply(inverse_outer_right)
    elif targetEffect == 9:
        fill_stripe_effect_outer_left.apply(inverse_outer_left)
        fill_stripe_effect_inner_left.apply(inverse_inner_left)
        fill_stripe_effect_inner_right.apply(inverse_inner_right)
        fill_stripe_effect_outer_right.apply(inverse_outer_right)
        fill_stripe_effect_outer_left.apply(outer_left)
        fill_stripe_effect_inner_left.apply(inner_left)
        fill_stripe_effect_inner_right.apply(inner_right)
        fill_stripe_effect_outer_right.apply(outer_right)

    else:

        dots.fill = 0

    dots.show()

    time.sleep(0.01)
