from ectoleds.effect_base import Effect
from ectoleds.breathe import BreatheHelper, BreatheHelperState
from ectoleds.color_utils import mergeColor
import adafruit_dotstar as dotstar
import time
import math
from random import seed
from random import random


class Blink:
    def __init__(self, basePos: int, breatheHelper: BreatheHelper):
        self.basePos = basePos
        self.breatheHelper = breatheHelper


class RandomBlink(Effect):
    def __init__(self, ledAmount, blinkColor, fadeColor=(0, 0, 0), maxBreatheRate=6, minBreatheRate=2, blinkRange=3,
                 maxParallelBlinks=5):
        super().__init__(blinkColor)
        self.minBreatheRate = minBreatheRate
        self.ledAmount = ledAmount
        self.fadeColor = fadeColor
        self.blinkRange = blinkRange
        self.maxParallelBlinks = maxParallelBlinks
        self.maxBreatheRate = maxBreatheRate
        self.blinks = []
        seed(time.time())
        for blink in range(self.maxParallelBlinks):
            self.blinks.append(Blink(basePos=self.randomPos(), breatheHelper=BreatheHelper(
                breatheRate=self.minBreatheRate + (self.maxBreatheRate - self.minBreatheRate) * random())))

    def randomPos(self):
        return random() * self.ledAmount

    def apply(self, leds: dotstar.DotStar, respectLedsState=False):
        for blink in reversed(self.blinks):
            blink.breatheHelper.update()
            pos = blink.basePos
            startPos = math.floor(pos - self.blinkRange / 2)
            endPos = math.floor(pos + self.blinkRange / 2)
            if startPos < 0:
                startPos = 0

            if endPos > self.ledAmount:
                endPos = self.ledAmount

            for pos in range(startPos, endPos):
                red = math.floor(self.color[0] * blink.breatheHelper.currentBreathe)
                blue = math.floor(self.color[1] * blink.breatheHelper.currentBreathe)
                green = math.floor(self.color[2] * blink.breatheHelper.currentBreathe)
                targetColor = (red, blue, green)

                if respectLedsState:
                    leds[pos] = mergeColor(leds[pos], targetColor)
                else:
                    leds[pos] = [red, blue, green]

            if blink.breatheHelper.count >= 1:
                self.blinks.remove(blink)

        while len(self.blinks) < self.maxParallelBlinks:
            self.blinks.append(Blink(basePos=self.randomPos(),
                                     breatheHelper=BreatheHelper(
                                         breatheRate=self.minBreatheRate +
                                                     (self.maxBreatheRate - self.minBreatheRate) * random())))
