import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt

GPIO.setmode (GPIO.BCM)

leds = [21, 20, 16, 12, 7 ,8, 25, 24]
dac = [26, 19, 13, 6, 5, 11, 9, 10]
clean_bin = [0, 0, 0, 0, 0, 0, 0, 0]

comp = 4
troyka = 17

GPIO.setup (leds, GPIO.OUT)
GPIO.setup (dac, GPIO.OUT)
GPIO.setup (comp, GPIO.IN)
GPIO.setup (troyka, GPIO.OUT)

V_dif_steep = 3.3/255
weit_time_set = 0.1

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

value_date = []

try:
    start = time.time()

    GPIO.output(troyka, 1)
    print("Зарядка конденсатора")
    raw_V = 0
    while (raw_V < 240):
        time.sleep(weit_time_set)
        raw_V = acd()
        value_date.append(raw_V * V_dif_steep)
        drav_valum(raw_V)
    charge =time.time() 

    GPIO.output(troyka, 0)
    print("Разрядка конденсатора")
    while (raw_V > 3):
        time.sleep(weit_time_set)
        raw_V = acd()
        value_date.append(raw_V * V_dif_steep)
        drav_valum(raw_V)

    end = time.time()
    print("Конец измерений")

    long_time = end - start


    plt.plot(value_date)
    plt.show()

    string_value_date = [str(value) for value in value_date] 
    with open("data.txt", 'w') as data_out : 
        data_out.write("\n".join(string_value_date))
    
    frequency = len(value_date)/long_time
    with open("settings.txt", 'w') as settings : 
        settings.write(str(frequency) + "\n")
        settings.write(str(V_dif_steep) + "\n")

    print("Продолжительность эксперемента:", long_time)
    print("Настроенная частота измерений", 1/weit_time_set)
    print("Средняя частота измерений", frequency)
    print("Шаг напряжения", V_dif_steep)

    print("Программа всё")

finally:
    GPIO.output (dac, clean_bin)
    GPIO.cleanup ()