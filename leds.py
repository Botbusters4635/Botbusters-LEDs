import time
import adafruit_dotstar
import board
import math
import numpy as np

from networktables import NetworkTables


class RunningLedsConfig:
    __slots__ = ["amountRunning", "baseColor", "runningColor", "fill", "increaseStep"]

    def __init__(self, amountRunning, baseColor, runningColor, fill, increaseStep):
        self.amountRunning = amountRunning
        self.baseColor = baseColor
        self.runningColor = runningColor
        self.fill = fill
        self.increaseStep = increaseStep


class BreatheConfig:
    __slots__ = ["color", "increaseStep"]

    def __init__(self, color, increaseStep):
        self.color = color
        self.increaseStep = increaseStep


def runningLeds(runningConfig):
    global state
    state = state + runningConfig.increaseStep
    if state > 1.0:
        state = 0
    if runningConfig.fill:
        pixels.fill(runningConfig.baseColor)
    index = math.floor(state * num_pixels)

    for i in range(runningConfig.amountRunning):
        if index + i < num_pixels:
            pixels[index + i] = runningConfig.runningColor

        print(num_pixels - 1 - i - index)
        if num_pixels - 1 - i - index >= 0:
            pixels[num_pixels - 1 - i - index] = runningConfig.runningColor

def breathe(breatheConfig):
    global breatheState
    global breatheIncreasing

    if breatheIncreasing:
        breatheState = breatheState + breatheConfig.increaseStep
    else:
        breatheState = breatheState - breatheConfig.increaseStep

    if breatheState > 1.0 and breatheIncreasing:
        breatheState = 1.0
        breatheIncreasing = False

    if breatheState < 0.25 and not breatheIncreasing:
        breatheState = 0.25
        breatheIncreasing = True

    colorFaded = (math.floor(breatheConfig.color[0] * breatheState), math.floor(breatheConfig.color[1] * breatheState),
                  math.floor(breatheConfig.color[2] * breatheState))
    pixels.fill(colorFaded)


def breatheWithRunning(breatheConfig, runningConfig):
    breathe(breatheConfig)
    runningLeds(runningConfig)


def limit(source, minVal, maxVal):
    if source > maxVal:
        source = maxVal
    if source < minVal:
        source = minVal
    return source


def stringToColor(string):
    splitMsg = string.split(",")
    if len(splitMsg) != 3:
        return 0, 0, 0

    r = int(splitMsg[0])
    g = int(splitMsg[1])
    b = int(splitMsg[2])

    r = limit(r, 0, 255)
    g = limit(g, 0, 255)
    b = limit(b, 0, 255)
    return r, g, b


NetworkTables.initialize(server="10.46.35.2")
table = NetworkTables.getTable("EctoLeds")

num_pixels = 30
pixels = adafruit_dotstar.DotStar(board.SCLK, board.MOSI, num_pixels, brightness=1.0, auto_write=False)

state = 0
breatheState = 0
breatheIncreasing = True

while True:
    breatheColorMessage = table.getString("BreatheColor", "0,70,0")
    breatheColor = stringToColor(breatheColorMessage)
    breatheColorSpeed = table.getNumber("BreatheColorSpeed", 0.003)

    followerColorMessage = table.getString("FollowerColor", "0,255,0")
    followerColor = stringToColor(followerColorMessage)
    followerSpeed = table.getNumber("FollowerSpeed", 0.006)
    followerAmount = int(table.getNumber("FollowerAmount", 1))

    breatheConfig = BreatheConfig(breatheColor, breatheColorSpeed)

    runningConfig = RunningLedsConfig(followerAmount, breatheColor, followerColor, False, breatheColorSpeed)

    breatheWithRunning(breatheConfig, runningConfig)
    pixels.show()
