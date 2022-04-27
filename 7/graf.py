import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt
from matplotlib.axis import Axis
from matplotlib.ticker import MultipleLocator, ScalarFormatter
import numpy as np

    

seyttings = np.loadtxt("settings.txt" , dtype=float, delimiter = '\n')

V_data = np.loadtxt("data.txt" , dtype=float, delimiter = '\n')

time = len(V_data)/seyttings[0]
T_data = np.arange(0, time, 1/seyttings[0], dtype=float) 
 
fig, ax = plt.subplots(figsize = (16,10), dpi = 400)

#Подписи
ax.set_xlabel("Время t,с")
ax.set_ylabel("Напряжение V,В") 

#линии
ax.grid(which = "major", visible = True)
ax.grid(which = "minor", visible = True)

#минор
Axis.set_minor_locator(ax.xaxis, MultipleLocator(2))
Axis.set_minor_locator(ax.yaxis, MultipleLocator(0.1))
#Axis.set_minor_formatter(ax.xaxis, ScalarFormatter()) 

plt.xlim(0, 85)
plt.ylim(0, 3.5)

ax.plot(T_data, V_data)
fig.savefig("test.png")
print("я сделять")