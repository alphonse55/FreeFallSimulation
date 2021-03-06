from matplotlib import pyplot as plt
import math

# VARIABLES
planet = input("Planet (Earth , Moon , Mars , Jupyter): ")
h0 = float(input("Initial height (in m): "))
v0 = float(input("Initial speed (in m/s): "))
time = float(input("Time to simulate (in s): "))
dt = float(input("dt: "))

if planet == "Earth":
    a = -9.80665
elif planet == "Moon":
    a = -1.62
elif planet == "Mars":
    a = -3.711
elif planet == "Jupyter":
    a = -24.79

t = 0
h = h0
v = v0
s = 0

rebound = False

t_values = []
h_values = []
v_values = []

count = []
zero = []

# OPERATIONS
for i in range(0, int(time / dt) + 1):

    t_values.append(t)

    if rebound == False:
        v = v0 + a * t
        h = h0 + v0 * t + (a * t ** 2) / 2
    elif rebound == True:
        v = v0 + a * s
        h = v * s + (a * s ** 2) / 2

    v_values.append(v)
    h_values.append(h)

    if h <= 0:
        v0 = -v
        rebound = True
        s = 0

    t += dt
    s += dt

    count.append(i * dt)
    zero.append(0)

# PLOT
plt.figure("Free fall on " + planet)
plt.plot(t_values, h_values)
plt.plot(count, zero)  # bottom
plt.plot(t_values, v_values)
plt.xlabel("t(s)")
plt.ylabel("h(m)")
plt.title("Height - Time")

plt.show()
