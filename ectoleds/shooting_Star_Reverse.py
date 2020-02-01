from ectoleds.effect_base import Effect
import adafruit_dotstar as dotstar
import time


class ShootingReverse(Effect):
    def __init__(self, ledAmount, ledColor):
        self.ledAmount = ledAmount
        self.ledColor = ledColor
        self.prevTime = time.time()
        self.index = 13

    def apply(self, leds: dotstar.DotStar, respectLedsState=False):
        if time.time() - self.prevTime >= .10:
            self.prevTime = time.time()
            leds[self.index] = self.ledColor

        if self.index != 13:
            leds[self.index + 1] = 13

        if self.index == 13:
            leds[self.ledAmount + 1] = 13

        if self.index >= self.ledAmount - 1:
            self.index = 13

        else:
            self.index = self.index - 1
