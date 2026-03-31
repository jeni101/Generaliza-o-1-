import numpy as np
import matplotlib.pyplot as plt

def simpson38(y, h):
    n = len(y) - 1
    if n % 3 != 0:
        raise ValueError("n tem que ser multiplo de 3")

    weights = np.ones(n + 1)
    weights[1:-1:3] = 3
    weights[2:-1:3] = 3
    weights[3:-1:3] = 2

    return (3 * h / 8) * np.sum(weights * y)

def perform(f_str, a, b, n_max):
    f = lambda x: eval(f_str, {"np": np, "x": x})

    n_values = [i for i in range(3, n_max + 1, 3)]
    resultados = []
    
    for n in n_values:
        x = np.linspace(a, b, n + 1)
        y = f(x)
        h = (b - a) / n
        resultados.append(simpson38(y, h))

    plt.figure(figsize=(10, 5))
    plt.plot(n_values, resultados, 'o-', color='darkblue', label='Valor da Integral')
    plt.axhline(y=resultados[-1], color='red', linestyle='--', label='Convergência')
    plt.title("Convergência do Método de Simpson 3/8")
    plt.xlabel("Número de Segmentos (n)")
    plt.ylabel("Resultado da Integral")
    plt.grid(True)
    plt.legend()
    plt.show()

funcao = "np.sin(x)**2"
perform(funcao, 0, np.pi, 30)