# integral = h / 3 * [f(x0) + 4 * f(x1) +  f(x2)]
# com repetição precisa de nummero impar de pontos ou nuero par de intervalos
# "" = h / 3 * [f(X0) + 4 * f(x impar) +  2 * f(X par) + f(Xn)]
# intervalos são medidos pelo x0 e xfinal, (xf-x0)/n2 = h
#ponto intermediario x1 = (xfinal+x0)


import numpy as np
import matplotlib.pyplot as plt

def simpson13(y, h):
    n = len(y) - 1
    
    if n % 2 != 0:
        raise ValueError("Simpson 1/3 exige n par.")

    
    weights = np.ones(n + 1)
    weights[1:-1:2] = 4 
    weights[2:-1:2] = 2  
    
    
    return (h / 3) * np.dot(weights, y)

def perform_13(f_str, a, b, n_max):
    
    n_values = np.arange(2, n_max + 1, 2)
    resultados = []
    
    for n in n_values:
        x = np.linspace(a, b, n + 1)
        h = (b - a) / n
        y = eval(f_str, {"__builtins__": None}, {"np": np, "x": x})
        
        
        resultados.append(simpson13(y, h))

   
    _plotar_resultados(n_values, resultados, f_str)

def _plotar_resultados(n_values, resultados, f_str):
    res = np.array(resultados)
    ref = res[-1]
    erros = np.abs(res[:-1] - ref)
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
    ax1.plot(n_values, res, 'o-', label='Simpson 1/3')
    ax1.set_title(f"Convergência: {f_str}")
    ax2.semilogy(n_values[:-1], erros, 's-r', label='Erro Residual')
    plt.tight_layout()
    plt.show()

