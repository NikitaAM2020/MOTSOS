import numpy as np
import matplotlib.pyplot as plt


def generate_sequence(N, A, n, phi):
    x = np.linspace(0, 2 * np.pi, N)  # Задаємо проміжок значень x
    exact_values = A * np.sin(n * x + phi)  # Точні значення функції
    max_error = 0.05 * A  # Максимальна похибка не більше 5% від амплітуди
    noisy_values = exact_values + np.random.uniform(-max_error, max_error,
                                                    N)  # Застосовуємо випадкове відхилення до точних значень
    return x, noisy_values


def arithmetic_mean(values):
    return np.mean(values)


def harmonic_mean(values):
    return len(values) / np.sum(1.0 / values)


def geometric_mean(values):
    return np.prod(values) ** (1 / len(values))


def plot_graph(x, y):
    plt.figure()
    plt.plot(x, y)
    plt.plot(x, exact_value(x, A, n, phi), color='red')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()


def exact_value(x, A, n, phi):
    return A * np.sin(n * x + phi)


def compare_values(approximate, exact):
    absolute_error = np.abs(approximate - exact)
    relative_error = absolute_error / np.abs(exact)
    return absolute_error, relative_error


def compare_errors(approximate, exact):
    absolute_error, relative_error = compare_values(approximate, exact)
    max_absolute_error = np.max(absolute_error)
    min_absolute_error = np.min(absolute_error)
    max_relative_error = np.max(relative_error)
    min_relative_error = np.min(relative_error)
    return max_absolute_error, min_absolute_error, max_relative_error, min_relative_error


def visualize_results(x, exact, approximate):
    plt.figure()
    plt.plot(x, exact, label='')
    # plt.plot(x, np.full_like(x, approximate), label='Approximate')
    plt.title('Comparison')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()


N = 800  # Кількість значень в послідовності
A = 1.0  # Амплітуда
n = 8  # Параметр n
phi = np.pi / 4  # Зсув по фазі

x, y = generate_sequence(N, A, n, phi)
plot_graph(x, y)

approximate_mean = arithmetic_mean(y)
harmonic_mean = harmonic_mean(y)
geometric_mean = geometric_mean(y)

exact_values = exact_value(x, A, n, phi)
max_absolute, min_absolute, max_relative, min_relative = compare_errors(approximate_mean, exact_values)

print(f'Arithmetic Mean: {approximate_mean}')
print(f'Harmonic Mean: {harmonic_mean}')
print(f'Geometric Mean: {geometric_mean}')
print(f'Max Absolute Error: {max_absolute}')
print(f'Min Absolute Error: {min_absolute}')
print(f'Max Relative Error: {max_relative}')
print(f'Min Relative Error: {min_relative}')
