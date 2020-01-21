from ectoleds.effect_base import Effect
import adafruit_dotstar as dotstar
from ectoleds.color_utils import mergeColor
import time
import math
from enum import Enum


class Shooting(Effect):
    def __init__(self, ledAmount, shootingColor):
        self.ledAmount = ledAmount
        self.shootingColor = shootingColor
        self.previousTime = time.time()
        self.index = 0

    def apply(self, leds: dotstar.DotStar, respectLedsState=False):
        if time.time()-self.previousTime >= .25:
            print(self.index)
            self.previousTime = time.time()
            leds[self.index] = self.shootingColor

            if self.index != 0:
                leds[self.index-1] = 0

            if self.index == 0:
                leds[self.ledAmount-1] = 0

            if self.index >= self.ledAmount-1:
                self.index = 0
            else:
                self.index = self.index + 1



