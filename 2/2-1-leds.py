import RPi.GPIO as GPIO
import time

sleep_time = 0.2
GPIO.setmode (GPIO.BCM)


leds = [21, 20, 16, 12, 7, 8, 25, 24]
leds_num = len (leds)
GPIO.setup (leds, GPIO.OUT)


cycles_num = 3
for iter_id in range (cycles_num):
    for i in range (0,leds_num):
        GPIO.output (leds[i], GPIO.HIGH)
        time.sleep (sleep_time)
        GPIO.output (leds[i], GPIO.LOW)

GPIO.output (leds, GPIO.HIGH)
time.sleep (sleep_time)
GPIO.output (leds, GPIO.LOW)

GPIO.cleanup ()