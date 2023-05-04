import cmath
import random
import time


def generate_signal(n):
    """Генерувати випадкову послідовність значень від -1 до 1"""
    return [random.uniform(-1, 1) for i in range(n)]


def fft(x):
    """Швидке перетворення Фур'є"""
    n = len(x)
    if n == 1:
        return x
    even = fft(x[0::2])
    odd = fft(x[1::2])
    return [even[k] + cmath.exp(-2j * cmath.pi * k / n) * odd[k]
            for k in range(n // 2)] + \
        [even[k] - cmath.exp(-2j * cmath.pi * k / n) * odd[k]
         for k in range(n // 2)]


def ifft(x):
    """Інверсне швидке перетворення Фур'є"""
    n = len(x)
    if n == 1:
        return x
    even = ifft(x[0::2])
    odd = ifft(x[1::2])
    return [even[k] + cmath.exp(2j * cmath.pi * k / n) * odd[k]
            for k in range(n // 2)] + \
        [even[k] - cmath.exp(2j * cmath.pi * k / n) * odd[k]
         for k in range(n // 2)]


def bitreverse_copy(x):
    """Обернення бітів у індексах"""
    n = len(x)
    result = [0] * n
    for i in range(n):
        result[int('{:0{width}b}'.format(i, width=int.bit_length(n - 1))[::-1], 2)]= x[i]
    return result

def fft(x):
    """Швидке перетворення Фур'є"""
    n = len(x)
    if n == 1:
        return x
    even = fft(x[0::2])
    odd = fft(x[1::2])
    twiddle = [cmath.exp(-2j * cmath.pi * k / n) * odd[k] for k in range(n // 2)]
    return [even[k] + twiddle[k] for k in range(n // 2)] + \
           [even[k] - twiddle[k] for k in range(n // 2)]


def ifft(x):
    """Інверсне швидке перетворення Фур'є"""
    n = len(x)
    if n == 1:
        return x
    even = ifft(x[0::2])
    odd = ifft(x[1::2])
    twiddle = [cmath.exp(2j * cmath.pi * k / n) * odd[k] for k in range(n // 2)]
    return [even[k] + twiddle[k] for k in range(n // 2)] + \
           [even[k] - twiddle[k] for k in range(n // 2)]


def fft_iter(x):
    """Ітеративне ШПФ"""
    n = len(x)
    levels = int.bit_length(n - 1)
    x = bitreverse_copy(x)
    for level in range(1, levels + 1):
        m = 2 ** level
        omega_m = cmath.exp(-2j * cmath.pi / m)
        for k in range(0, n, m):
            omega = 1
            for j in range(0, m // 2):
                t = omega * x[k + j + m // 2]
                u = x[k + j]
                x[k + j] = u + t
                x[k + j + m // 2] = u - t
                omega *= omega_m
    return x


def ifft_iter(x):
    """Ітеративне інверсне ШПФ"""
    n = len(x)
    levels = int.bit_length(n - 1)
    x = bitreverse_copy(x)
    for level in range(1, levels + 1):
        m = 2 ** level
        omega_m = cmath.exp(2j * cmath.pi / m)
        for k in range(0, n, m):
            omega = 1
            for j in range(0, m // 2):
                t = omega * x[k + j + m // 2]
                u = x[k + j]
                x[k + j] = u + t
                x[k + j + m // 2] = u - t
                omega *= omega_m
    return [i / n for i in x]


# Тестування
signal = generate_signal(256)

start = time.perf_counter()
fft_result = fft(signal)
end = time.perf_counter()
print(f"FFT час: {end - start:.8f} секунд")

start = time.perf_counter()
ifft_result = ifft(fft_result)
end = time.perf_counter()
print(f"IFFT час: {end - start:.8f} секунд")

fft_iter_result = fft_iter(signal)
end = time.perf_counter()
print(f"FFT ітеративне час обчислення: {end - start} секунд")

# Підрахунок кількості операцій
n = len(signal)
operations = 0
levels = int.bit_length(n - 1)
for level in range(1, levels + 1):
    m = 2 ** level
    operations += 2 * n * level // m
print(f"FFT ітеративне кількість операцій: {operations}")

# Порівняння швидкодії з ДПФ
start = time.perf_counter()
# dft_result = dft(signal)
end = time.perf_counter()
print(f"DFT час обчислення: {end - start} секунд")

# Підрахунок кількості операцій
operations = n ** 2
print(f"DFT кількість операцій: {operations}")
