def isGreaterThan(colorA, colorB):
    averageA = (colorA[0] + colorA[1] + colorA[2]) / 3
    averageB = (colorB[0] + colorB[1] + colorB[2]) / 3
    return averageA > averageB