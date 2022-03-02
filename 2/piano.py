import RPi.GPIO as GPIO
import time

sleep_time = 0.2
GPIO.setmode (GPIO.BCM)


leds = [21, 20, 16, 12, 7, 8, 25, 24]

aux = [22, 23, 27, 18, 15, 14,3, 2]
leds_num = len (leds)
GPIO.setup (leds, GPIO.OUT)
GPIO.output (leds, GPIO.LOW)
GPIO.setup (aux, GPIO.IN)

while (True):
    for led_id in range (len (leds)):
        GPIO.output (leds[led_id], GPIO.input (aux[led_id]))
        
GPIO.cleanup ()