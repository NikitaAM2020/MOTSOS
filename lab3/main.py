import cmath
import numpy as np
import time


# Функція для обчислення ШПФ для вхідного сигналу x
def fft(x):
    N = len(x)
    if N <= 1:
        return x
    even = fft(x[0::2])
    odd = fft(x[1::2])
    T = [cmath.exp(-2j * cmath.pi * k / N) * odd[k] for k in range(N // 2)]
    return [even[k] + T[k] for k in range(N // 2)] + [even[k] - T[k] for k in range(N // 2)]


# Генеруємо випадковий сигнал
N = 128
x = np.random.rand(N)

# Доповнюємо вхідний сигнал нулями до степеня 2
M = 2 ** int(np.ceil(np.log2(N)))
x = np.concatenate([x, np.zeros(M - N)])

t1 = time.time()
# Обчислюємо ШПФ
X = fft(x)
t2 = time.time()

# Виводимо результат
for i, val in enumerate(X):
    print(f"C_{i}: {val}")

# вивід часу обчислення
execution_time = t2 - t1
print(f"\nЧас виконання: {execution_time:.10f} секунд")

# обчислення кількості операцій
num_plus = N
num_mult = 4 * N
num_operations = num_plus + num_mult

print(f"\nКількість операцій множення: {num_mult}")
print(f"Кількість операцій додавання: {num_plus}")
print(f"Загальна кількість операцій: {num_operations}")
