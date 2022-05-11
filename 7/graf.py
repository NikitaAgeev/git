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

plt.legend()

dot_dif = 20

dot_x = [T_data[i*dot_dif] for i in range(len(V_data) // dot_dif)]
dot_y = [V_data[i*dot_dif] for i in range(len(V_data) // dot_dif)]


#Подписи
ax.set_xlabel("Время t,с")
ax.set_ylabel("Напряжение V,В") 

#линии
ax.grid(which = "major", visible = True,  linewidth = 2)
ax.grid(which = "minor", visible = True, linestyle = '--')

#минор
Axis.set_minor_locator(ax.xaxis, MultipleLocator(2))
Axis.set_minor_locator(ax.yaxis, MultipleLocator(0.1))


plt.xlim(0, 85)
plt.ylim(0, 3.5)

ax.plot(T_data, V_data, c = "b", label='V(t)')
ax.scatter(dot_x, dot_y, c = "r")

top_time = T_data[np.argmax(V_data)]

plt.text(1, 3, "Время зарядки {}c \nВремя разрядки {} ".format(top_time, T_data.max() - top_time))

plt.title("График зависимости V(t) во время зарядки и разрядки конденсатора")

plt.legend()
fig.savefig("test.png")
print("я сделять")
