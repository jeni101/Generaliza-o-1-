import numpy as np
from trapezio.trapezio import plotar_trapezios as trapezio
from simpson38.simpson38_graph import perform38 as simpson38
from simpson13.simpson13_graph import perform_13 as simpson13

# Função base
funcao_simpson = "np.sin(x)**2"

# Simpson 1/3
# python main.py simpson13
# Deve ter número de intervalos par
numero_13 = 9
simpson13(funcao_simpson, 0, np.pi, numero_13)

# Simpson 3/8
# python main.py simpson38
# Deve ser um múltiplo de 3
numero_38 = 9
simpson38(funcao_simpson, 0, np.pi, numero_38)

##

#imformations

def ajuda_sintaxe():
    print("""|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|
|                 COMO DIGITAR A FUNÇÃO                       |
|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|
| USE SEMPRE: x como variável                                 |
| Exemplo: x**2, x**3 + 2*x                                   |
|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|
| FUNÇÕES DISPONÍVEIS (direto, sem np.):                      |
| FUNÇÕES DISPONÍVEIS:                                        |
| sin(x)   → seno                                             |
| cos(x)   → cosseno                                          |
| exp(x)   → exponencial                                      |
| log(x)   → logaritmo natural                                |
|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|
| EXEMPLOS VÁLIDOS:                                           |
| x**2                                                        |
| x**3 + 2*x                                                  |
| sin(x)                                                      |
| x**2 + cos(x)                                               |
| exp(x) + x                                                  |
| log(x) + x**2                                               |
|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|
| ERROS COMUNS:                                               |
| ❌ sin(4)        → não depende de x                         |
| ❌ x^2           → use x**2                                 |
| ❌ sen(x)        → use sin(x)                               |
| ❌ faltar *       → ex: 2x → use 2*x                        |
| ❌ usar np.sin(x) → não precisa do np.                      |
|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|
| DICA: sempre use x dentro da função!                        |
|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|
""")
