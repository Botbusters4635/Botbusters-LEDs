# this code what made possible by KAREN

from ectoleds.effect_base import Effect
from ectoleds.color_utils import mergeColor
import adafruit_dotstar as dotstar
import time


class FillStripe(Effect):
    prevTime: float

    def __init__(self, ledAmount, Background_Color, dotColor):
        self.ledAmount = ledAmount
        self.Background_Color = Background_Color
        self.prevTime = time.time()
        self.current_pos = 0
        self.dotColor = dotColor

    def apply(self, leds: dotstar.DotStar, respectLedsState=False):
        if time.time() - self.prevTime >= .05:
            self.prevTime = time.time()

            if respectLedsState:
                leds[self.current_pos] = mergeColor(leds[self.current_pos], self.Background_Color)
            else:
                leds[self.current_pos] = self.dotColor

            if self.current_pos != self.ledAmount - self.ledAmount:
                if respectLedsState:
                    leds[self.current_pos - 2] = mergeColor(leds[self.current_pos - 1], (0, 255, 0))
                else:
                    leds[self.current_pos - 1] = self.Background_Color

            if self.current_pos == self.ledAmount - self.ledAmount:
                if respectLedsState:
                    leds[self.ledAmount - 1] = mergeColor(leds[self.Background_Color - 1], 0)
                else:
                    leds[self.ledAmount - 1] = self.Background_Color

            if self.current_pos >= self.ledAmount - 1:
                self.current_pos = self.ledAmount - self.ledAmount
            else:
                self.current_pos = self.current_pos + 1
