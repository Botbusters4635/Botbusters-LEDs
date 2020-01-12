import ectoleds.effect_base
import adafruit_dotstar as dotstar
import time
import math
from enum import Enum


class BreatheState(Enum):
    Rising = 1
    Fading = 2


class Breathe(ectoleds.effect_base.Effect):
    def __init__(self, ledAmount, breatheColor, fadeColor=(0, 0, 0), breatheRate=0.5):
        self.ledAmount = ledAmount
        self.breatheColor = breatheColor
        self.fadeColor = fadeColor
        self.currentBreathe = 0.0
        self.previousTime = time.time()
        self.state = BreatheState.Rising

        if breatheRate > 1.0:
            self.breatheRate = 1.0
        elif breatheRate < 0.0:
            self.breatheRate = 0.0
        else:
            self.breatheRate = breatheRate

    def apply(self, leds: dotstar.DotStar):
        timeStep = time.time() - self.previousTime
        breatheChange = self.breatheRate * timeStep

        if self.state == BreatheState.Rising:
            if self.currentBreathe >= 1.0:
                self.currentBreathe = 1.0
                self.state = BreatheState.Fading
            else:
                self.currentBreathe += breatheChange
        elif self.state == BreatheState.Fading:
            if self.currentBreathe <= 0.0:
                self.currentBreathe = 0.0
                self.state = BreatheState.Rising
            else:
                self.currentBreathe -= breatheChange

        red = math.floor(self.breatheColor[0] * self.currentBreathe)
        blue = math.floor(self.breatheColor[1] * self.currentBreathe)
        green = math.floor(self.breatheColor[2] * self.currentBreathe)

        leds.fill((red, blue, green))
        self.previousTime = time.time()
        pass
