import utm
import math

def calcDistAndBearing(current, waypoint):
    (aX, aY, aNum, aLet) = utm.from_latlon(current[0], current[1])
    (bX, bY, bNum, bLet) = utm.from_latlon(waypoint[0], waypoint[1])

    x = abs(aX - bX)
    y = abs(aY - bY)

    z = math.sqrt(math.pow(x,2)+math.pow(y,2))

    bearingRads = math.atan2(bX - aX, bY - aY)
    if bearingRads < 0:
        bearingRads += math.pi * 2

    bearingDeg = math.degrees(bearingRads)

    return (z, bearingDeg)

def computeDirectionPixel (degrees):
    if degrees >= 342 or degrees < 18:
        return [7]
    if 324 <= degrees < 342:
        return [7,8]
    if 306 <= degrees < 324:
        return [8]
    if 288 <= degrees < 306:
        return [8,9]
    if 252 <= degrees < 288:
        return [9,0]
    if 234 <= degrees < 252:
        return [0,1]
    if 216 <= degrees < 234:
        return [1]
    if 198 <= degrees < 216:
        return [1,2]
    if 162 <= degrees < 198:
        return [2]
    if 144 <= degrees < 162:
        return [2,3]
    if 126 <= degrees < 144:
        return [3]
    if 108 <= degrees < 126:
        return [3,4]
    if 72 <= degrees < 108:
        return [4,5]
    if 54 <= degrees < 72:
        return [5,6]
    if 36 <= degrees < 54:
        return [6]
    if 18 <= degrees < 36:
        return [6,7]
