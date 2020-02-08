import adafruit_dotstar as dotstar
from typing import Tuple

class DotstarSegment:
    def __init__(self, full_leds:  dotstar.DotStar, segment_start: int, segment_end: int, inverted: bool = False):
        """Please document your code :D"""
        self.segment_start = segment_start
        self.segment_end = segment_end
        self.leds = full_leds
        self.length = segment_end - segment_start
        self.inverted = inverted
        if self.length <= 0:
            raise ValueError('Segment length must be greater than zero')

    def __check_index(self, key: int):
        if not (0 <= key < self.length):
            raise IndexError('Tried to access index out of segment {}'.format(key))

    def __getitem__(self, key: int) -> Tuple[int, int, int]:
        self.__check_index(key)
        if self.inverted:
            return self.leds[self.segment_end - key]
        else:
            return self.leds[key + self.segment_start]
    
    def __setitem__(self, key: int, value: Tuple[int, int, int]):
        self.__check_index(key)
        if self.inverted:
            self.leds[self.segment_end - key] = value
        else:
            self.leds[key + self.segment_start] = value