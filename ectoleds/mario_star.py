import time
from ectoleds.effect_base import Effect
import adafruit_dotstar as dotstar
import random


class MarioStar(Effect):

    def __init__(self, ledAmount, ledColor):
        self.ledAmount = ledAmount
        self.ledColor = ledColor
        self.actualTime = time.time()

    def apply(self, ledAmount, ledColor):

        if time.time() == self.actualTime <= 0.1:
            self.ledColor == 0,
            self.actualTime == 1.0
        elif time.time() == self.actualTime and 0.2 >= self.actualTime >= 0.1:
            self.ledColor == (255, 0, 0)
        elif time.time() == self.actualTime and 0.3 <= self.actualTime >= 0.2:
            self.ledColor == (255, 187, 0)
        elif time.time() == self.actualTime and 0.4 <= self.actualTime >= 0.3:
            self.ledColor == (255, 255, 255)
        elif time.time() == self.actualTime >= 0.4:
            self.actualTime == 0
