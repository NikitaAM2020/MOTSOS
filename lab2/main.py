import math
import numpy as np
import matplotlib.pyplot as plt
import time
import sys


def furier_coefficient(k, N, x):
    """
    Функція обчислює коефіцієнт Фур'є Ck для заданого значення k, довжини вхідного вектора N та вхідного вектора x.
    """
    count_mult = 0
    count_add = 0
    Ck = 0
    for n in range(N):
        # Обчислюємо дійсну та уявну складові
        cos_component = math.cos(2 * math.pi * k * n / N)
        sin_component = -1j * math.sin(2 * math.pi * k * n / N)
        # Обчислюємо коефіцієнт за формулою
        Ck += x[n] * (cos_component + sin_component)
        count_mult += 3  # Одне множення та дві операції з плаваючою точкою
        count_add += 2  # Два додавання з плаваючою точкою
    # Кількість операцій на виході
    count = count_mult + count_add
    return Ck / N, count_mult, count_add, count



def furier_series(N, x):
    """
    Функція обчислює ряд Фур'є для вхідного вектора x довжини N та повертає послідовність коефіцієнтів Фур'є Ck.
    """
    coefficients = []
    count = sys.getsizeof(N) + sys.getsizeof(x) + sys.getsizeof(coefficients)
    count_mult = 0
    count_add = 0
    for k in range(N):
        Ck, count_k, count_k_mult, count_k_add = furier_coefficient(k, N, x)
        coefficients.append(Ck)
        count += count_k + sys.getsizeof(Ck) + sys.getsizeof(coefficients)
        count_mult += count_k_mult
        count_add += count_k_add
    return coefficients, count, count_mult, count_add



# генерація довільного вхідного вектору
N = 180
x = np.random.randn(N)

# Обчислити коефіцієнти Фур'є
start_time = time.time()
coefficients, total_count, count_mult, count_add = furier_series(N, x)
end_time = time.time()

print("Кількість операцій множення: ", count_mult)
print("Кількість операцій додавання: ", count_add)
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

# print("Вхідний вектор x:", x)
print("\nКоефіцієнти ряду Фур'є:")
for k, Ck in enumerate(coefficients):
    print("C[{}] = {:.4f} + {:.4f}j".format(k, Ck.real, Ck.imag))
