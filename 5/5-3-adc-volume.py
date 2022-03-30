import RPi.GPIO as GPIO
import time

GPIO.setmode (GPIO.BCM)

leds = [21, 20, 16, 12, 7 ,8, 25, 24]
dac = [26, 19, 13, 6, 5, 11, 9, 10]
clean_bin = [0, 0, 0, 0, 0, 0, 0, 0]

comp = 4
troyka = 17

GPIO.setup (leds, GPIO.OUT)
GPIO.setup (dac, GPIO.OUT)
GPIO.setup (comp, GPIO.IN)
GPIO.setup (troyka, GPIO.OUT, initial = 1)

def dec2bin(n):
    return [int(i) for i in bin(n)[2:].zfill(8)]

def drav_valum(n):
    for i in range(7):
        n -= 255/10
        if n > 0:
            GPIO.output(leds[-i-1], 1)
        else:
            GPIO.output(leds[-i-1], 0)

def acd():
    status = 0
    for i in range(7):
        status += 2**(7-i)
        GPIO.output(dac, dec2bin(status))
        time.sleep(0.001)
        if not GPIO.input(comp):
             status -= 2**(7-i)
    return status


try:
    while True:
        i = acd()
        drav_valum(i)
        print(f"i = {i}, V = {(3.3*i)/255}")
finally:
    GPIO.output (dac, clean_bin)
    GPIO.cleanup ()