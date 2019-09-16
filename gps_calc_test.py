import utm
import math

(aX, aY, aNum, aLet) = utm.from_latlon(40.660943, -91.300914)
(bX, bY, bNum, bLet) = utm.from_latlon(41.415043, -93.046670)

x = abs(aX - bX)
y = abs(aY - bY)

z = math.sqrt(math.pow(x,2)+math.pow(y,2))

bearingRads = math.atan2(bX - aX, bY - aY)
if bearingRads < 0:
    bearingRads += math.pi * 2

bearingDeg = math.degrees(bearingRads)

print('X: {0:.6f}'.format(x))
print('Y: {0:.6f}'.format(y))
print('Z: {0:.6f}'.format(z))
print('Bearing: {0:.1f}'.format(bearingDeg))
