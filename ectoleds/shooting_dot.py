from ectoleds.effect_base import Effect
from ectoleds.color_utils import mergeColor
import adafruit_dotstar as dotstar
import time


class Shooting(Effect):
    def __init__(self, ledAmount, shootingColor):
        self.ledAmount = ledAmount
        self.shootingColor = shootingColor
        self.previousTime = time.time()
        self.index = 0

    def apply(self, leds: dotstar.DotStar, respectLedsState=False):

        if time.time()-self.previousTime >= .01:

            self.previousTime = time.time()
            if respectLedsState:
                leds[self.index] = mergeColor(leds[self.index], self.shootingColor)
            else:
                leds[self.index] = self.shootingColor

            if self.index != 0:
                if respectLedsState:
                    leds[self.index - 1] = mergeColor(leds[self.index - 1], 0)
                else:
                    leds[self.index - 1] = 0

            if self.index == 0:
                if respectLedsState:
                    leds[self.index - 1] = mergeColor(leds[self.index - 1], 0)
                else:
                    leds[self.index - 1] = 0

            if self.index >= self.ledAmount - 1:
                self.index = 0
            else:
                self.index = self.index + 1
    bool
