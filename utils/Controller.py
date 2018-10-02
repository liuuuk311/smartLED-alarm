import time
import threading
# from neopixel import *

PIXEL_NUM = 10
DEBUG = True


def set_color_to_all(red, green, blue):
    # Set all led to red, green and blue. No animations
    for i in range(PIXEL_NUM):
        # strip.setPixelColor(i, color)
        if DEBUG:
            print('Set RGB({0}, {1}, {2}) to pixel #{3}'.format(red, green, blue, i))
    # strip.show()

def color_wipe(red, green, blue, wait_ms=50):
    # Wipe color across display a pixel at a time.

    for i in range(PIXEL_NUM):
        # strip.setPixelColor(i, color)
        # strip.show()
        if DEBUG:
            print('Set RGB({0}, {1}, {2}) to pixel #{3}'.format(red, green, blue, i))
        time.sleep(wait_ms/1000.0)
    for i in range(PIXEL_NUM):
        # strip.setPixelColor(i, color)
        # strip.show()
        if DEBUG:
            print('Clearing set RGB(0, 0, 0) to pixel #{0}'.format(i))
        time.sleep(wait_ms/1000.0)

