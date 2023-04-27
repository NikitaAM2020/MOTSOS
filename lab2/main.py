import math
import numpy as np
import matplotlib.pyplot as plt
import time
import sys


def furier_coefficient(k, N, x):
    """
    Функція обчислює коефіцієнт Фур'є Ck для заданого значення k, довжини вхідного вектора N та вхідного вектора x.
    """
    count = sys.getsizeof(k) + sys.getsizeof(N) + sys.getsizeof(x[k]) + 4 * sys.getsizeof(math.pi) + 2 * sys.getsizeof(
        math.cos) + 2 * sys.getsizeof(math.sin) + sys.getsizeof(1j) + sys.getsizeof(0)
    Ck = 0
    for n in range(N):
        count += sys.getsizeof(n) + sys.getsizeof(x[n]) + 4 * sys.getsizeof(math.pi) + 2 * sys.getsizeof(
            math.cos) + 2 * sys.getsizeof(math.sin) + sys.getsizeof(1j) + sys.getsizeof(0)
        Ck += x[n] * (math.cos(2 * math.pi * k * n / N) - 1j * math.sin(2 * math.pi * k * n / N))
        count += sys.getsizeof(Ck)
    return Ck / N, count


def furier_series(N, x):
    """
    Функція обчислює ряд Фур'є для вхідного вектора x довжини N та повертає послідовність коефіцієнтів Фур'є Ck.
    """
    coefficients = []
    count = sys.getsizeof(N) + sys.getsizeof(x) + sys.getsizeof(coefficients)
    for k in range(N):
        Ck, count_k = furier_coefficient(k, N, x)
        coefficients.append(Ck)
        count += count_k + sys.getsizeof(Ck) + sys.getsizeof(coefficients)
    return coefficients, count


# генерація довільного вхідного вектору
N = 18
x = np.random.randn(N)

# Обчислити коефіцієнти Фур'є
start_time = time.time()
coefficients, total_count = furier_series(N, x)
end_time = time.time()

print("Загальна кількість операцій: ", total_count)
print("Час обчислення коефіцієнтів Фур'є: {:.6f} с".format(end_time - start_time))

# Побудувати графіки амплітуд та фаз коефіцієнтів Фур'є
amplitudes = np.abs(coefficients)
phases = np.angle(coefficients)

plt.subplot(2, 1, 1)
plt.stem(amplitudes)
plt.title("Амплітуди коефіцієнтів Фур'є")

plt.subplot(2, 1, 2)
plt.stem(phases)
plt.title("Фази коефіцієнтів Фур'є")

plt.tight_layout()
plt.show()

print("Вхідний вектор x:", x)
print("\nКоефіцієнти ряду Фур'є:")
for k, Ck in enumerate(coefficients):
    print("C{} = {:.4f} + {:.4f}j".format(k, Ck.real, Ck.imag))
