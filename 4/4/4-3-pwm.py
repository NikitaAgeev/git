import RPi.GPIO as GPIO
import time

GPIO.setmode (GPIO.BCM)

leds = [21, 20, 16, 12, 7 ,8, 25, 24]
clean_bin = [0, 0, 0, 0, 0, 0, 0, 0]
on_bin = [1, 1, 1, 1, 1, 1, 1, 1]

GPIO.setup (leds, GPIO.OUT)
GPIO.setup (2, GPIO.OUT)

def dec2bin(n):
    return [int(i) for i in bin(n)[2:].zfill(8)]


try:
    try:
        d = float(input("Введите звполнение: "))
        print ("Прдполагаемый выход:", "{:.4}".format(3.3*d/100))
    except ValueError:
        print("Неправильный ввод")
    else:
        while 1:
            b = 0
            for b in range(100):
                if b < d:
                    GPIO.output (leds, on_bin)
                    GPIO.output (2, 1)
                else:
                    GPIO.output (leds, clean_bin)
                    GPIO.output (2, 0)
                    
        
finally:
    GPIO.output (leds, clean_bin)
    GPIO.cleanup ()