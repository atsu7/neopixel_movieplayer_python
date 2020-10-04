# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel
import cv2
import numpy as np

#

# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18

# The number of NeoPixels
num_rows = 16
num_columns = 16
num_pixels = num_rows*num_columns

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)


# readImage
img = cv2.imread('sample.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Change the order to RGB
pixel_values = []
for i in range(num_rows):
    for j in range(num_columns):
        pixel_values.append(img[i, j])

for k in range(num_pixels):
    if(k // num_columns % 2 == 0): # LEDパネルの下から数えて奇数行目（最下行は１）
        pixels[k] = pixel_values[(num_rows - (k+1) // num_columns -1 ) * num_columns + k % num_columns]
    else: # LEDパネルの下から数えて偶数行目（最下行は１）
        pixels[k] = pixel_values[num_pixels-1 - k]

pixels.show()

# while True:
#     # Comment this line out if you have RGBW/GRBW NeoPixels
#     pixels.fill((0, 0, 255))
#     pixels.show()
#     time.sleep(1)