import matplotlib.pyplot as plt
import numpy as np

c_start = -10
c_end = 1
c_delta = 0.5
x = 3.567

c_val = np.arange(c_start, c_end + c_delta, c_delta)
l_val = []

for c in c_val:
    l = np.abs(2 * x - c) ** 3 ** 0.2 + 0.567
    l_val.append(l)

for c, l in zip(c_val, l_val):
    print(f"c = {c:.2f}, l = {l:.2f}")

max_l = max(l_val)
min_l = min(l_val)
mean_l = np.mean(l_val)

print("Max value:",max_l)
print("Min value: ", min_l)
print("Average value:",mean_l)

sorted_y_values = sorted(l_val)

plt.figure(figsize = (10,6))
plt.plot(c_val, l_val, label = "f(c)", marker = '*')
plt.axhline(mean_l, color = 'blue', linestyle = 'dotted', label = "Среднее значение")
plt.title("График функции f(c)")
plt.grid(True)
plt.legend()
plt.show()