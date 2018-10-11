import time
from threading import Thread, Semaphore

# Semaphore on the LED strip
sem = Semaphore()

ON_RASPBERRY = True
DEBUG = True

# LED strip configuration:
LED_COUNT = 60     # Number of LED pixels.
LED_PIN = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
# True to invert the signal (when using NPN transistor level shift)
LED_INVERT = False
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53




if ON_RASPBERRY:
    from neopixel import *

    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(
        LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()


def RGB_to_byte(red, green, blue):
   # Workaround for bug in Color from Neopixel
   return Color(green, red, blue)

def set_all(red, green, blue, density=1.0, animation=False, animation_speed=0):
    # Set all led to red, green and blue.

    led_density = int(LED_COUNT / (LED_COUNT * density))

    for led in range(0, LED_COUNT, led_density):
        if ON_RASPBERRY:
            strip.setPixelColor(led, RGB_to_byte(int(red), int(green), int(blue)))
            if animation:
                strip.show()
                time.sleep(animation_speed/1000.0)

        if DEBUG:
            print('Set RGB({0}, {1}, {2}) to pixel #{3}'.format(red, green, blue, led))

    if ON_RASPBERRY and not(animation):
        strip.show()


def run_color_wipe(red, green, blue, density=1.0, iterations=1, wait_ms=50):
    # Wipe color across display a pixel at a time.
    sem.acquire()

    for times in range(iterations):

        set_all(red, green, blue, density=density, animation=True, animation_speed=wait_ms)
        set_all(0, 0, 0, density=1.0, animation=True, animation_speed=wait_ms)

    sem.release()


def run_increase(red, green, blue, density=1.0, wait_sec=5):
    sem.acquire()

    colors = {'red': red, 'green': green, 'blue': blue}
    order = sorted(colors, key=colors.get) # Min to max

    colors_dict = dict(zip(order, [0,0,0]))

    min_v = colors[order[0]]
    mid_v = colors[order[1]]
    max_v = colors[order[2]]

    if min_v != 0 and mid_v != 0:

        for c_min in range(0, min_v+1):

            colors_dict[order[0]] = c_min
            colors_dict[order[1]] = round((mid_v/min_v) * colors_dict[order[0]])
            colors_dict[order[2]] = round((max_v/mid_v) * colors_dict[order[1]])

            set_all(colors_dict['red'], colors_dict['green'], colors_dict['blue'], density=density)

            if ON_RASPBERRY:
                time.sleep(wait_sec)
    elif mid_v != 0:

        for c_mid in range(0, mid_v+1):

            colors_dict[order[1]] = c_mid
            colors_dict[order[2]] = round((max_v/mid_v) * colors_dict[order[1]])

            set_all(colors_dict['red'], colors_dict['green'], colors_dict['blue'], density=density)

            if ON_RASPBERRY:
                time.sleep(wait_sec)

    else:

        for c_max in range(0, max_v+1):

            colors_dict[order[2]] = c_max

            set_all(colors_dict['red'], colors_dict['green'], colors_dict['blue'], density=density)

            if ON_RASPBERRY:
                time.sleep(wait_sec)


    sem.release()


def run_ping_pong(red, green, blue, how_many=1, speed_ms=10, iterations=1):
    for led in range(LED_COUNT):
        if ON_RASPBERRY:
            strip.setPixelColor(led, RGB_to_byte(int(red), int(green), int(blue)))
            time.sleep(speed_ms/1000.0)
            

            if led + 1 > how_many:
                strip.setPixelColor(led+1-how_many, RGB_to_byte(0, 0, 0))

            strip.show()

        if DEBUG:
            print('Set RGB({0}, {1}, {2}) to pixel #{3}'.format(red, green, blue, led))
            time.sleep(speed_ms/1000.0)
            print('Clear RGB(0, 0, 0) to pixel #{0}'.format(led+1-how_many))

    for led in reversed(range(LED_COUNT)):
        if ON_RASPBERRY:
            strip.setPixelColor(led, RGB_to_byte(int(red), int(green), int(blue)))
            time.sleep(speed_ms/1000.0)

            if led - 1 > how_many:
                strip.setPixelColor(led-1+how_many, RGB_to_byte(0, 0, 0))

            strip.show()

        if DEBUG:
            print('Set RGB({0}, {1}, {2}) to pixel #{3}'.format(red, green, blue, led))
            time.sleep(speed_ms/1000.0)
            print('Clear RGB(0, 0, 0) to pixel #{0}'.format(led-1+how_many))



def color_wipe(red, green, blue, density=1.0, iterations=1, wait_ms=50):
    my_thread = Thread(target=run_color_wipe, args=(red, green, blue, density, iterations, wait_ms))
    my_thread.start()


def increase(red, green, blue, density=1.0, wait_sec=5):
    my_thread = Thread(target=run_increase, args=(red, green, blue, density, wait_sec))
    my_thread.start()

def ping_pong(red, green, blue, how_many=1, speed_ms=10):
    my_thread = Thread(target=run_ping_pong, args=(red, green, blue, how_many, speed_ms))
    my_thread.start()




if __name__ == "__main__":
    ping_pong(2,2,2)
