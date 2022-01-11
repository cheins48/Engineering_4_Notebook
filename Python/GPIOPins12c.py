# GPIO Pins -I2C (ENGR4) Conrad Heins Used Harriet Novacs Code as a 
# reference

import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import Adafruit_LSM303
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# Raspberry Pi pin configuration:
RST = 24
# Note the following are only used with SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

# Create a LSM303 instance.
lsm303 = Adafruit_LSM303.LSM303()
disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST, i2c_address=0x3d)

# Initialize library.
disp.begin()
# Clear display.
disp.clear()
disp.display()
# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()
while True:
    draw.rectangle((0,0,width,height), outline=0, fill=0)
      # Read the X, Y, Z axis acceleration values and print them.
    accel, mag = lsm303.read()
    # Grab the X, Y, Z components from the reading and print them out.
    accel_x, accel_y, accel_z = accel
    mag_x, mag_y, mag_z = mag
    print('Accel X={0}, Accel Y={1}, Accel Z={2}, Mag X={3}, Mag Y={4}, Mag Z={5}'.format(
          accel_x, accel_y, accel_z, mag_x, mag_y, mag_z))
    draw.text((0, 0),    ("x: " + str(accel_x)),  font=font, fill=255)
    draw.text((0, 10),   ("y: " + str(accel_y)),  font=font, fill=255)
   # t = img_value_axis.rotate(90, expand=1)
    draw.text((0, 20),   ("z: " + str(accel_z)),  font=font, fill=255)
   # t = img_value_axis.rotate(45, expand=1)
    disp.image(image)
    disp.display()
    time.sleep(0.1)
