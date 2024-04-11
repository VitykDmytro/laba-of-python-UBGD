import numpy as np
import matplotlib.pyplot as plt

# Визначення функції sinc(x)
def sinc(x):
    return np.sin(x) / x if x != 0 else 1.0

# Визначення функції f(x)
def f(x, N):
    return sinc(2 * x * N - 1)

# Протабулювання функції на проміжку [0, 1]
x_values = np.linspace(0.01, 1, 1000)  # Виключаємо x=0, щоб уникнути ділення на нуль
N = 3
y_values = f(x_values, N)

# Побудова графіка
plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values, label=f'f(x), N={N}')
plt.title('Графік функції f(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()
