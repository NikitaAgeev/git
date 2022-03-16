import RPi.GPIO as GPIO
import time

GPIO.setmode (GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
clean_bin = [0, 0, 0, 0, 0, 0, 0, 0]

GPIO.setup (dac, GPIO.OUT)

def dec2bin(n):
    return [int(i) for i in bin(n)[2:].zfill(8)]

def prob_out(binary):
    s = 0
    for i in range(7, -1, -1):
        s += binary[i] * 2**(7 - i)
    return s * (3.3/255)


try:
    try:
        binary = dec2bin(int(input("Введите число для ЦАП: ")))
    except ValueError:
        print("Неправильный ввод")
    else:
        try:
            GPIO.output (dac, binary)
        except RuntimeError:
            print("Слишком большое значение")
        else:
            print ("Прдполагаемый выход:", "{:.4}".format(prob_out(binary)))
            a = 1
            while a != "q": a = input("Enter q ")
finally:
    GPIO.output (dac, clean_bin)
    GPIO.cleanup ()