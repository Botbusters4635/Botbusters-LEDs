import time
import board
import adafruit_dotstar as dotstar
from ectoleds import breathe
from ectoleds import random_blink
from ectoleds import shooting_dot
<<<<<<< HEAD
from networktables import NetworkTables

NetworkTables.initialize(server = "192.168.1.104")
table = NetworkTables.getTable("Numeros")
table.getNumber("Num")
=======
from ectoleds import  shooting_Star_Reverse
>>>>>>> d8da8721f16f8b7d966433f6997f1f0628d93060

num_leds = 13
dots = dotstar.DotStar(board.SCK, board.MOSI, num_leds, brightness=0.5, auto_write=False)

breatheEffect = breathe.Breathe(ledAmount=num_leds, breatheColor=(0, 0, 255))
breatheEffect2 = breathe.Breathe(ledAmount=num_leds, breatheColor=(255, 0, 0))
randomBlinkEffect = random_blink.RandomBlink(ledAmount=num_leds, blinkColor=(255, 0, 0))
<<<<<<< HEAD
shootingdotEffect = shooting_dot.Shooting(ledAmount=num_leds, shootingColor=(255, 0, 0))



while True:
    targetEffect = 2
    if targetEffect == 0:
        shootingdotEffect.apply(dots, respectLedsState=True)
    elif targetEffect == 1:
        breatheEffect.apply(dots)
    elif targetEffect == 2:
        breatheEffect2.apply(dots, respectLedsState=True)
    else:
        dots.fill = 0





=======
shootingdotEffect = shooting_dot.Shooting(ledAmount=num_leds, shootingColor=(0, 0, 50))
shootingDotReverseEffect = shooting_Star_Reverse.ShootingReverse(ledAmount=num_leds, ledColor=(0, 0, 255))

while True:
    # breatheEffect.apply(dots)
    # randomBlinkEffect.apply(dots, respectLedsState=True)
    #shootingdotEffect.apply(dots)
    shootingDotReverseEffect.apply(dots)
>>>>>>> d8da8721f16f8b7d966433f6997f1f0628d93060

    dots.show()

    time.sleep(0.01)