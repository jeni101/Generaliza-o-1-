import numpy as np

def simpson38_comp(x, y = None, func = None, n = None):
    if func is not None:
        if n is None or n % 3 != 0:
            raise ValueError("n deve ser multiplo de 3")
        
        x = np.linspace(x[0], x[1], n + 1)
        y = func(x)

    n = len(x) - 1
    h = (x[-1] - x[0]) / n

    if n % 3 != 0:
        return "Erro, n deve ser multiplo de 3"
        
    weigths = np.ones(n + 1)
    weigths[1:-1:3] = 3
    weigths[2:-1:3] = 3
    weigths[3:-1:3] = 2

    integral = (3 * h / 8) * np.sum(weigths * y)
    return integral

f = lambda x: np.exp(-x**2) * np.cos(x)
resultado = simpson38_comp([0, 2], func=f, n=9)

print(f"Resultado {resultado:.10f}")