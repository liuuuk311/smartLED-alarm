from neopixel import Color

# Helper
def RGB_to_byte(red, green, blue):
   # Workaround for bug in Color from Neopixel
   return Color(green, red, blue)
