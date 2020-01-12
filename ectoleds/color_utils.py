import math


def mergeColor(colorA, colorB):
    averageRed = math.floor((colorA[0] + colorB[0]) / 2)
    averageGreen = math.floor((colorA[1] + colorB[1]) / 2)
    averageBlue = math.floor((colorA[2] + colorB[2]) / 2)
    averageColor = (averageRed, averageGreen, averageBlue)
    return averageColor
