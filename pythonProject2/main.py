import numpy as np
import matplotlib.pyplot as plt


# функція яка розкладається у ряд Фур'є
def f(x):
    return x * 8 * np.exp(-1 * (x ** 2) / 8)


# обчислює коефіцієнти a_k
def ak(k):
    if k == 0:
        return 0
    else:
        return (-1) ** k * np.sqrt(2) * np.pi * k


# обчислює коефіцієнти b_k
# def bk(k):
#     return np.sqrt(2) * np.pi * k * np.exp(-0.5 * (np.pi * k) ** 2)


# повертає результат обчислення ряду Фур'є
def fourier_series(x, N):
    a0 = 0
    s = a0
    for k in range(1, N + 1):
        s += ak(k) * np.cos(k * x) #+ bk(k) * np.sin(k * x)
    return s


# будує графік оригінальної функції
def plot(N):
    x = np.linspace(-np.pi, 3*np.pi, 1000)
    y = f(x)

    plt.figure(figsize=(15, 10))
    # plt.xlim(-5, 5)

    plt.plot(x, y, label='Original function')
    plt.legend()
    plt.show()


# будує графіки наближення
def plot_harmonics(N):
    x = np.linspace(-np.pi, 3*np.pi, 1000)
    y = f(x)
    s = np.zeros_like(x)

    plt.figure(figsize=(15, 10))
    # plt.xlim(-5, 5)

    plt.plot(x, y, label='Original function')
    for k in range(1, N + 1):
        s += ak(k) * np.cos(k * x) #+ bk(k) * np.sin(k * x)
        plt.plot(x, s, label=f'N={k}')
    plt.legend()
    plt.show()


# будує графіки відносної похибки для кожної точки
def plot_error(N):
    x = np.linspace(-2, 2, 1000)
    error = np.vectorize(lambda x: relative_error(x, N))(x)

    plt.figure(figsize=(15, 10))
    plt.plot(x, error, label=f'Relative error for N={N}')
    #plt.legend()
    plt.show()



def plot_ak(N):
    x = np.linspace(0, N, N)
    y = [ak(k) for k in range(1, N + 1)]
    plt.figure(figsize=(15, 10))
    plt.stem(x, y, label='ak coefficients')
    plt.legend()
    plt.show()



# повертає значення відносної похибки, обчисленої з використанням ряду Фур'є
def relative_error(x, N):
    y = f(x)
    s = fourier_series(x, N)
    error = np.abs((s - y) / y)
    return np.max(error)


# зберігає результати у файл results.txt
def save_results(x, N):
    ak_list = [ak(k) for k in range(1, N + 1)]
    #bk_list = [bk(k) for k in range(1, N + 1)]
    error = relative_error(x, N)
    with open('results.txt', 'w') as f:
        f.write(f'Value x: {x}\n\n')
        f.write(f'Order N: {N}\n\n')
        f.write('ak coefficients:\n')
        f.write(str(ak_list) + '\n\n')
        #f.write('bk coefficients:\n')
        #f.write(str(bk_list) + '\n\n')
        f.write(f'Relative error: {error}\n')
        f.write(f'Value for x = {x}: {one}\n')


# введення значення x з консолі
x = float(input("Enter x value: "))
N = int(input("Enter N value: "))
one = fourier_series(x, N)
plot(N)
plot_harmonics(N)
plot_error(N)
plot_ak(N)

error = relative_error(x, N)
print(f'Relative error for N = {N}: {error}')
print(f'for x = {x}: {one}')

save_results(x, N)
