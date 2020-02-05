from ectoleds.effect_base import Effect
import adafruit_dotstar as dotstar
import time


class ShootingReverse(Effect):
    def __init__(self, ledAmount, blinkColor):
        self.ledAmount = ledAmount
        self.ledColor = blinkColor
        self.prevTime = time.time()
        self.index = 0

    def apply(self, leds: dotstar.DotStar, respectLedsState=False):
            if time.time() - self.prevTime >= .25:

                self.prevTime = time.time()
                leds[self.index] = self.ledColor

            if self.index != 0:
                leds[self.index - 1] = 0

            if self.index == 0:
                leds[self.ledAmount - 1] = 0

            if self.index >= self.ledAmount - 1:
                self.index = 0

            else:
                self.index = self.index + 1

        if self.index != 0:
            leds[self.index + 1] = 0

        if self.index == 0:
            leds[self.ledAmount + 1] = 0

        if self.index >= self.ledAmount + 1:
            self.index = 0

        else:
            self.index = self.index - 1



