import numpy as np
import matplotlib.pyplot as plt 

def calcular_integral_trapezio(funcao, inicio, fim, quantidade_de_trapezios):
    largura = (fim - inicio) / quantidade_de_trapezios
    pontos = np.linspace(inicio, fim, quantidade_de_trapezios + 1)
    valores = funcao(pontos)
    
    soma = valores[0] + valores[-1] + 2 * sum(valores[1:-1])
    integral = (largura / 2) * soma 
    
    return integral, pontos, valores 

def plotar_trapezios(funcao, inicio, fim, quantidade_de_trapezios):
    integral, pontos, valores = calcular_integral_trapezio(funcao, inicio, fim, quantidade_de_trapezios)
    
    pontos_suaves = np.linspace(inicio, fim, 1000)
    valores_suaves = funcao(pontos_suaves)
    
    # curva da função
    plt.plot(pontos_suaves, valores_suaves, label="Função")
    
    # trapézios
    for i in range(quantidade_de_trapezios):
        plt.fill(
            [pontos[i], pontos[i], pontos[i + 1], pontos[i + 1]],
            [0, valores[i], valores[i + 1], 0],
            alpha=0.3
        )
    
    plt.title(f"Integral aproximada = {integral:.4f}")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid()
    plt.show()
    
    return integral
