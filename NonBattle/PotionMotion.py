import time
import mouse

# upper left corner of upper left tile - 650 285
# bottom right corner of upper right tile - 1270 815

initialX = 650
initialY = 285
tileWidth = 88.571
tileHeight = 88.333

def getTileLocation(tileX, tileY):
    x = initialX + tileWidth * tileX - (tileWidth / 2)
    y = initialY + tileHeight * tileY - (tileHeight / 2)

    return x, y

time.sleep(1.5)

# verticle movement
for x in range(1, 8):
    startX, startY = getTileLocation(x, 1)
    for y in range(1, 7):
        endX, endY = getTileLocation(x, y)
        mouse.drag(startX, startY, endX, endY, duration=0.05)
        time.sleep(0.05)

# horizontal movement
for y in range(1, 7):
    startX, startY = getTileLocation(1, y)
    for x in range(1, 8):
        endX, endY = getTileLocation(x, y)
        mouse.drag(startX, startY, endX, endY, duration=0.05)
        time.sleep(0.05)