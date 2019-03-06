# CircuitPython demo - Dotstar
import time
import adafruit_dotstar
import board
import math

num_pixels = 30
pixels = adafruit_dotstar.DotStar(board.SCLK, board.MOSI, num_pixels, brightness=0.1, auto_write=False)
state = 0
breatheState = 0
breatheIncreasing = True

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
   if pos < 0 or pos > 255:
        return (0, 0, 0)
   if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
   if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
   pos -= 170
   return (pos * 3, 0, 255 - pos * 3)


def color_fill(color, wait):
    pixels.fill(color)
    pixels.show()
    time.sleep(wait)


def slice_alternating(wait):
    pixels[::2] = [RED] * (num_pixels // 2)
    pixels.show()
    time.sleep(wait)
    pixels[1::2] = [ORANGE] * (num_pixels // 2)
    pixels.show()
    time.sleep(wait)
    pixels[::2] = [YELLOW] * (num_pixels // 2)
    pixels.show()
    time.sleep(wait)
    pixels[1::2] = [GREEN] * (num_pixels // 2)
    pixels.show()
    time.sleep(wait)
    pixels[::2] = [TEAL] * (num_pixels // 2)
    pixels.show()
    time.sleep(wait)
    pixels[1::2] = [CYAN] * (num_pixels // 2)
    pixels.show()
    time.sleep(wait)
    pixels[::2] = [BLUE] * (num_pixels // 2)
    pixels.show()
    time.sleep(wait)
    pixels[1::2] = [PURPLE] * (num_pixels // 2)
    pixels.show()
    time.sleep(wait)
    pixels[::2] = [MAGENTA] * (num_pixels // 2)
    pixels.show()
    time.sleep(wait)
    pixels[1::2] = [WHITE] * (num_pixels // 2)
    pixels.show()
    time.sleep(wait)


def slice_rainbow(wait):
    pixels[::6] = [RED] * (num_pixels // 6)
    pixels.show()
    time.sleep(wait)
    pixels[1::6] = [ORANGE] * (num_pixels // 6)
    pixels.show()
    time.sleep(wait)
    pixels[2::6] = [YELLOW] * (num_pixels // 6)
    pixels.show()
    time.sleep(wait)
    pixels[3::6] = [GREEN] * (num_pixels // 6)
    pixels.show()
    time.sleep(wait)
    pixels[4::6] = [BLUE] * (num_pixels // 6)
    pixels.show()
    time.sleep(wait)
    pixels[5::6] = [PURPLE] * (num_pixels // 6)
    pixels.show()
    time.sleep(wait)


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            rc_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(rc_index & 255)
        pixels.show()
        time.sleep(wait)


RED = (255, 0, 0)
YELLOW = (255, 150, 0)
ORANGE = (255, 40, 0)
GREEN = (0, 255, 0)
TEAL = (0, 255, 120)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
MAGENTA = (255, 0, 20)
WHITE = (255, 255, 255)
blink_time = 0.1


def  blink_cycle(times,color):
	for x in range(times):
		pixels.fill(color)
		pixels.show()
		time.sleep(blink_time)
		pixels.fill((0,0,0))
		pixels.show()
		time.sleep(blink_time)



def  runningLeds(amountRunning, baseColor, runningColor, fill, increase):
	global state
	state = state + increase
	if state > 1.0:
		state = 0
	if fill:
		pixels.fill((255, 255, 255))
	index = math.floor(state * num_pixels)
	for i in range(amountRunning):
		print(index + i)
		if index + i > num_pixels - 1:
			break
		pixels[index + i] = runningColor
	pixels.show()

def breathe(color, increase):
	global breatheState
	global breatheIncreasing

	if breatheIncreasing:
		breatheState = breatheState + increase
	else:
		breatheState = breatheState - increase

	if breatheState > 1.0 and breatheIncreasing:
		breatheState = 1.0
		breatheIncreasing = False
	
	if breatheState < 0.25 and  not breatheIncreasing:
		breatheState = 0.25
		breatheIncreasing = True


	colorFaded  = (math.floor(color[0] * breatheState), math.floor(color[1] * breatheState), math.floor(color[2] * breatheState))
	pixels.fill(colorFaded)
	pixels.show()

def breatheWithRunning(breatheColor, timeBreathe, followColor, timeIncrease):
	breathe(breatheColor, timeBreathe)
	runningLeds(1, breatheColor, followColor, False, timeIncrease)

while True:
#	running_leds(2, (255, 255, 255), (100,100,0))
#	blink_cycle(5, (255, 255, 255))
	breatheWithRunning((0, 50, 0), 0.003, (0, 255, 0), 0.006)
	print(breatheState)	
	print(breatheIncreasing)
