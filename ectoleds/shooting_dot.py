from ectoleds.effect_base import Effect
from ectoleds.color_utils import mergeColor
import adafruit_dotstar as dotstar
import time


class Shooting(Effect):
    def __init__(self, ledAmount, shootingColor):
        super().__init__(shootingColor)
        self.ledAmount = ledAmount
        self.previousTime = time.time()
        self.index = 0

    def apply(self, leds: dotstar.DotStar, respectLedsState=False):

        if time.time()-self.previousTime >= .01:

            self.previousTime = time.time()
            if respectLedsState:
                leds[self.index] = mergeColor(leds[self.index], self.color)
            else:
                leds[self.index] = self.color

            if self.index != 0:
                if respectLedsState:
                    leds[self.index - 1] = mergeColor(leds[self.index - 1], 0)
                else:
                    leds[self.index - 1] = 0

            if self.index == 0:
                if respectLedsState:
                    leds[self.ledAmount - 1] = mergeColor(leds[self.ledAmount - 1], 0)
                else:
                    leds[self.ledAmount - 1] = 0

            if self.index >= self.ledAmount - 1:
                self.index = 0
            else:
                self.index = self.index + 1
