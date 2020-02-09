from effect_base import Effect
from adafruit_fancyled.fastled_helpers import ColorFromPalette

class FireEffect(Effect):
    def __init__(self, led_amount: int)