import adafruit_dotstar as dotstar

class Effect:
    def __init__(self, color):
        self.color = color

    def apply(self, leds: dotstar.DotStar, respectLedsState=False):
        pass
