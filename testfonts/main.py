 # Display text on I2C driven ssd1306 OLED display 
from machine import Pin, I2C, ADC
from ssd1306 import SSD1306_I2C
from writer import Writer
import spleen5x8
import spleen6x12
import spleen12x24
import spleen16x32
#import spleen32x64

sda=machine.Pin(4)
scl=machine.Pin(5)
i2c=machine.I2C(0,sda=sda, scl=scl, freq=400000)

oled = SSD1306_I2C(128, 64, i2c)

wri8 = Writer(oled, spleen5x8, verbose=False)
wri12 = Writer(oled, spleen6x12, verbose=False)
wri24 = Writer(oled, spleen12x24, verbose=False)
wri32 = Writer(oled, spleen16x32, verbose=False)

Writer.set_textpos(oled, 0, 0)
wri32.printstring("0123456")
Writer.set_textpos(oled, 26, 0)
wri24.printstring("0123456789")
Writer.set_textpos(oled, 46, 0)
wri12.printstring("0123456789")
Writer.set_textpos(oled, 56, 0)
wri8.printstring("0123456789")

oled.show()

while True:
    pass


