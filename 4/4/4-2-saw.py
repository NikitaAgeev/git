import RPi.GPIO as GPIO
import time

GPIO.setmode (GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
clean_bin = [0, 0, 0, 0, 0, 0, 0, 0]

GPIO.setup (dac, GPIO.OUT)

def dec2bin(n):
    return [int(i) for i in bin(n)[2:].zfill(8)]


try:
    try:
        d = float(input("Введите периoд: "))
    except ValueError:
        print("Неправильный ввод")
    else:
        for i in range(2):
            for j in range(256):
                GPIO.output (dac, dec2bin(j))
                time.sleep(d/256)
finally:
    GPIO.output (dac, clean_bin)
    GPIO.cleanup ()