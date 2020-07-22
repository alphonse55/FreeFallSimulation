# IMPORTS
from matplotlib import pyplot as plt
import math

# VARIABLES
planet = str(input("Pianeta (Terra , Luna , Marte , Giove): "))
h0 = float(input("Altezza iniziale (in m): "))
v0 = float(input("Velocità iniziale (in m/s): "))
tempo = int(input("Tempo (in s): "))
dt = float(input("dt: "))

if planet == "Terra":
    a = -9.80665
elif planet == "Luna":
    a = -1.62
elif planet == "Marte":
    a = -3.711
elif planet == "Giove":
    a = -24.79

t = 0  # t0
h = h0
v = v0
rimbalzo = False  # già rimbalzato o no?
s = 0  # tempo partendo dal rimbalzo

t_values = []
h_values = []
v_values = []


# OPERATIONS
for i in range(0, int(tempo/dt)+1):

    s += dt

    t_values.append(t)

    if rimbalzo == False:
        v = v0 + a*t
        h = h0 + v0*t + (a*t**2)/2
    elif rimbalzo == True:
        v = v0 + a*s
        h = v*s + (a*s**2)/2

    v_values.append(v)
    h_values.append(h)

    # print("v", i, " = ", v)
    # print("h", i, " = ", h)

    if h <= 0:
        v0 = -v
        rimbalzo = True
        s = 0

    t += dt


# LINEA DELLO 0
count = []
zero = []

for i in range(0, tempo+1):
    count.append(i)
    zero.append(0)

# PLOT
plt.figure("Caduta libera su", planet)
plt.plot(t_values, h_values)
plt.plot(count, zero)
# plt.plot(t_values, v_values)
plt.xlabel("t(s)")
plt.ylabel("h(m)")
plt.title("Altezza in funzione del tempo")

# plt.figure(2)
# plt.plot(t_values, v_values)
# plt.xlabel("t(s)")
# plt.ylabel("v(m/s)")

plt.show()
