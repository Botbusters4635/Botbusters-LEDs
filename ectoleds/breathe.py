from ectoleds.effect_base import Effect
import adafruit_dotstar as dotstar
from ectoleds.color_utils import mergeColor
import time
import math
from enum import Enum


class BreatheHelperState(Enum):
    Rising = 1
    Fading = 2


class BreatheHelper:
    def __init__(self, breatheRate=0.5):
        self.state = BreatheHelperState.Rising
        self.breatheRate = breatheRate
        self.currentBreathe = 0.0
        self.previousTime = time.time()
        self.count = 0.0
        if breatheRate < 0.0:
            self.breatheRate = 0.0
        else:
            self.breatheRate = breatheRate

    def update(self):
        timeStep = time.time() - self.previousTime
        breatheChange = self.breatheRate * timeStep

        if self.state == BreatheHelperState.Rising:
            if self.currentBreathe + breatheChange > 1.0:
                self.currentBreathe = 1.0
                self.state = BreatheHelperState.Fading
            else:
                self.currentBreathe += breatheChange
        elif self.state == BreatheHelperState.Fading:
            if self.currentBreathe - breatheChange < 0.0:
                self.currentBreathe = 0.0
                self.state = BreatheHelperState.Rising
                self.count += 1
            else:
                self.currentBreathe -= breatheChange

        self.previousTime = time.time()


class Breathe(Effect):
    def __init__(self, ledAmount, breatheColor, fadeColor=(0, 0, 0), breatheRate=0.5):
        super().__init__(breatheColor)
        self.ledAmount = ledAmount
        self.fadeColor = fadeColor
        self.breatheHelper = BreatheHelper(breatheRate=breatheRate)


    def apply(self, leds: dotstar.DotStar, respectLedsState=False):
        self.breatheHelper.update()
        red = math.floor(self.color[0] * self.breatheHelper.currentBreathe)
        blue = math.floor(self.color[1] * self.breatheHelper.currentBreathe)
        green = math.floor(self.color[2] * self.breatheHelper.currentBreathe)

        targetColor = (red, blue, green)

        for pixel in range(self.ledAmount):
            if respectLedsState:
                leds[pixel] = mergeColor(leds[pixel], targetColor)
            else:
                leds[pixel] = [red, blue, green]
