import numpy as np
import sys
from pick import pick

from minimos_quadrados.minimos_quadrados import perform_mq as minimos_quadrados
from simpson13.simpson13_graph import perform_13 as simpson13
from simpson38.simpson38_graph import perform38 as simpson38
from trapezio.trapezio import plotar_trapezios as trapezio

def main():
    funcao_base = "np.sin(x)**2"
    limite_a = 0
    limite_b = np.pi
    n_intervalos = 6

    title = '=== CÁLCULO NUMÉRICO: SELECIONE O MÉTODO ==='
    options = [
        'Simpson 1/3 (n deve ser par)',
        'Simpson 3/8 (n deve ser múltiplo de 3)',
        'Trapézio Generalizado',
        'Mínimos Quadrados',
        'Sair'
    ]

    option, index = pick(options, title, indicator='=>')

    if option == 'Sair':
        sys.exit()

    print(f"\nExecutando: {option}")
    print(f"Função: {funcao_base} | Intervalo: [{limite_a}, {limite_b}] | n = {n_intervalos}\n")

    try:
        if index == 0:  # Simpson 1/3
            simpson13(funcao_base, limite_a, limite_b, n_intervalos)
        
        elif index == 1:  # Simpson 3/8
            simpson38(funcao_base, limite_a, limite_b, n_intervalos)
        
        elif index == 2:  # Trapézio
            trapezio(funcao_base, limite_a, limite_b, n_intervalos)
        
        elif index == 3:  # Mínimos Quadrados
            minimos_quadrados(funcao_base, limite_a, limite_b, n_intervalos)

    except Exception as e:
        print(f"Erro ao executar o cálculo: {e}")

    input("\nProcesso finalizado. Pressione Enter para fechar...")

if __name__ == "__main__":
    main()