from effect_base import Effect
from adafruit_fancyled.fastled_helpers import ColorFromPalette
from adafruit_fancyled.adafruit_fancyled import CRGB
from typing import List
import adafruit_dotstar as dotstar

class FireEffect(Effect):
    def __init__(self, led_amount: int, palette: List[CRGB]):
        self.led_amount = led_amount
        self.palette = palette

    def apply(self, leds: dotstar.DotStar, respectLedsState=False):
        heat = [3][24]
        print(heat)