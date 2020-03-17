import time
import board
import adafruit_dotstar as dotstar
import leds
from ectoleds import dotstar_segment
from ectoleds import walking_dot
from ectoleds.effect_base import Effect
from ectoleds.color_utils import mergeColor


num_leds = 90
dots = dotstar.DotStar(board.SCK, board.MOSI, num_leds, brightness=1.0, auto_write=False)
dots.fill((0, 0, 0))

outer_left = dotstar_segment.DotstarSegment(dots, 0, 23)
inner_left = dotstar_segment.DotstarSegment(dots, 24, 43, True)
inner_right = dotstar_segment.DotstarSegment(dots, 44, 63)
outer_right = dotstar_segment.DotstarSegment(dots, 64, 88, True)


class WalkingDotFull(Effect):

    walking_dot_effect_outer_left = walking_dot.WalkingDot(ledAmount=outer_left.length, Background_Color=(0, 255, 255),
                                                           dotColor=(255, 30, 0))
    walking_dot_effect_inner_left = walking_dot.WalkingDot(ledAmount=inner_left.length, Background_Color=(0, 255, 255),
                                                           dotColor=(255, 30, 0))
    walking_dot_effect_inner_right = walking_dot.WalkingDot(ledAmount=inner_right.length, Background_Color=(0, 255, 255),
                                                            dotColor=(255, 30, 0))
    walking_dot_effect_outer_right = walking_dot.WalkingDot(ledAmount=outer_right.length, Background_Color=(0, 255, 255),
                                                            dotColor=(255, 30, 0))
