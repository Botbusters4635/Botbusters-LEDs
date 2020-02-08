import adafruit_dotstar as dotstar
from typing import Tuple

class DotstarSegment:
    def __init__(self, full_leds:  dotstar.DotStar, segment_start: int, segment_end: int, inverted: bool = False):
        """Please document your code :D"""
        self.segment_start = segment_start
        self.segmentEnd = segment_end
        self.leds = full_leds
        self.length = segment_end - segment_start
        self.inverted = inverted
        if self.length <= 0:
            raise ValueError('Segment length must be greater than zero')

    def __check_index(self, key: int):
        if key < 0:
            raise IndexError('Tried to access negative index of segment')
        if key > self.length:
            raise IndexError('Tried to access index out of segment')

    def __getitem__(self, key: int) -> Tuple[int, int, int]:
        self.__check_index(key)
        if self.inverted:
            return self.leds[self.segmentEnd - key]
        else:
            return self.leds[key + self.segment_start]
    
    def __setitem__(self, key: int, value: Tuple[int, int, int]):
        self.__check_index(key)
        if self.inverted:
            self.leds[self.segmentEnd - key] = value
        else:
            self.leds[key + self.segment_start] = value