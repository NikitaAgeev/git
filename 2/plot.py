def bin_for_rp (x):
    x_bin = format (x, '08b')

    return list (map (int, list(x_bin)))

digis = [255, 127, 64, 32, 5, 0, 255]
digs_num = len (digis)
volts = digs_num * [0.0]

import time
break_time = 0.53

import RPi.GPIO as GPIO
dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setmode (GPIO.BCM)
GPIO.setup (dac, GPIO.OUT)

for num_id in range (0, digs_num):
    print (f'Now processing [{digis[num_id]}]:')

    out = bin_for_rp (digis[num_id])
    
    GPIO.output (dac, out)

    time.sleep (break_time)

    volts[num_id] = float (input ())

    time.sleep (break_time)

    GPIO.output (dac, GPIO.LOW)

import matplotlib.pyplot as plt

plt.scatter (volts, digis)
plt.show ()

GPIO.output (dac, GPIO.LOW)
GPIO.cleanup ()