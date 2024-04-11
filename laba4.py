import numpy as np
import matplotlib.pyplot as plt

def sinc(x):
    return np.sin(x) / x if x != 0 else 1.0

def f(x, N):
    return sinc(2 * x * N - 1)

x_values = np.linspace(0.001, 1, 1000)  # Уникнення ділення на нуль, x не може дорівнювати 0
N = 3
y_values = f(x_values, N)

plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values, label=f'f(x), N={N}')
plt.title('Графік функції f(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()
