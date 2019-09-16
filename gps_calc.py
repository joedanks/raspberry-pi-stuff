import utm
import math

def calcBearingAndDist(current, waypoint):
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


print(calcBearingAndDist((40.668006, -91.316099), (40.661147, -91.321118)))
# print('X: {0:.6f}'.format(x))
# print('Y: {0:.6f}'.format(y))
# print('Z: {0:.6f}'.format(z))
# print('Bearing: {0:.1f}'.format(bearingDeg))
