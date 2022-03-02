import RPi.GPIO as GPIO
import time

sleep_time = 1.5

GPIO.setmode (GPIO.BCM)

GPIO.setup (17, GPIO.OUT)

GPIO.output (17, GPIO.HIGH)

time.sleep (sleep_time)

GPIO.output (17, GPIO.LOW)

time.sleep (sleep_time)

GPIO.output (17, GPIO.HIGH)

time.sleep (sleep_time)

GPIO.output (17, GPIO.LOW)

time.sleep (sleep_time)

GPIO.output (17, GPIO.HIGH)

time.sleep (sleep_time)

GPIO.output (17, GPIO.LOW)


