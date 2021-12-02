import RPi.GPIO as GPIO 
from time import sleep
GPIO.setmode(GPIO.BCM) #this sets my pin numbering scheme as the BCM nubering scheme
# Variable for the GPIO pin number  
LED_pin_Red = 20
LED_pin_Green = 21
# Tell the Pi we are using the breakout board pin numbering
GPIO.setmode(GPIO.BCM)
 
# Set up the GPIO pin for output
GPIO.setup(LED_pin_Red, GPIO.OUT)
GPIO.setup(LED_pin_Green, GPIO.OUT)
# Loop to blink our led
while True:
        GPIO.output(LED_pin_Red, GPIO.HIGH)  
        GPIO.output(LED_pin_Green, GPIO.LOW) 
        sleep(.5)
        GPIO.output(LED_pin_Red, GPIO.LOW)
        GPIO.output(LED_pin_Green, GPIO.HIGH)
        sleep(.5
)
