import numpy as np
import trapezio
from trapezio import *

def escolher_funcao(opcao):
    if opcao == 1:
        return lambda x: x**2
    elif opcao == 2:
        return lambda x: np.sin(x)
    elif opcao == 3:
        return lambda x: np.exp(x)
    else:
        print("Opção inválida")
        return None


print("Escolha a função:")
print("1 - x^2")
print("2 - sin(x)")
print("3 - e^x")

opcao = int(input("Digite a opção: "))
funcao = escolher_funcao(opcao)

if funcao:
    inicio = float(input("Digite o início do intervalo: "))
    fim = float(input("Digite o fim do intervalo: "))
    n = int(input("Quantidade de trapézios: "))
    
    resultado = trapezio.plotar_trapezios(funcao, inicio, fim, n)
    
    print(f"Resultado da integral: {resultado:.4f}")