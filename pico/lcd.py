from machine import Pin, I2C
from lib.ssd1306 import SSD1306_I2C

i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)
display = SSD1306_I2C(128, 64, i2c)

print("did init")

display.text('Hello World', 0, 0, 1)
display.show()

