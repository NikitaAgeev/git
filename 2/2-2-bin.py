import RPi.GPIO as GPIO
import time

sleep_time = 0.2
GPIO.setmode (GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
gpio_num = len (dac)
number = [1, 1, 1, 1, 1, 1, 1, 1]

GPIO.setup (dac, GPIO.OUT)

GPIO.output (dac, number)
time.sleep (12)

GPIO.output (dac, GPIO.LOW)
GPIO.cleanup ()


