from ectoleds.effect_base import Effect
from adafruit_fancyled.fastled_helpers import ColorFromPalette
from adafruit_fancyled.adafruit_fancyled import CRGB
from typing import List
import adafruit_dotstar as dotstar
from random import seed
from random import random
import time
import math

class FireEffect(Effect):
    def __init__(self, led_amount: int, palette: List[CRGB], fire_cooling: int = 150, fire_intensity = 100):
        self.led_amount = led_amount
        self.fire_cooling = fire_cooling
        self.fire_intensity = fire_intensity
        self.palette = palette
        self.heat = [0] * self.led_amount
        seed(time.time())

    def __random8_int(self, min: int, max: int):
        return (random() * (max - min)) + min

    def __qsub8_int(self, a: int , b: int):
        res = a - b
        return res if res >= 0 else 0

    def __qadd8_int(self, a: int, b: int):
        res = a + b
        return res if res <= 255 else 255

    def apply(self, leds: dotstar.DotStar, respectLedsState=False):
	    # Step 1.  Cool down every cell a little
        for i in range(self.led_amount):
            newValue = self.heat[i] - random() * ((self.fire_cooling * 10 / self.led_amount) + 2)
        
            self.heat[i] = newValue if newValue >= 0 else 0

        # Step 2.  self.heat from each cell drifts 'up' and diffuses a little
        for i in range(self.led_amount - 1, 1, -1):
            self.heat[i] = (self.heat[i - 1] + self.heat[i - 2] + self.heat[i - 2]) / 3

        # Step 3. Mantain bottom lit up
        sparking = random() * (self.fire_intensity / 255) * self.led_amount

        for i in range(math.ceil(sparking)):
            self.heat[i] = 255

        # Step 4.  Map from self.heat cells to LED colors
        for i in range(self.led_amount):
            colorIndex = (self.heat[i] / 255) * (16.0 * (len(self.palette) - 1)) 
            color = ColorFromPalette(self.palette, colorIndex, blend=True)
            color.red = int(color.red * 255)
            color.green = int(color.green * 255)
            color.blue= int(color.blue * 255)
            leds[i] = color
