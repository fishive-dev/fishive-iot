import neopixel
import board

pixels = neopixel.NeoPixel(board.D18, 60)

def set_rgba(r = 255, g = 255, b = 255, a = 0.5):
    pixels.fill((r,g,b))
    pixels.brightness = a

set_rgba()