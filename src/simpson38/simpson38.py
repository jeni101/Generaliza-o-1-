def f(x):
    return 1 / (1 + x**2)

def simpson38(a, b, n):
    if n % 3 != 0:
        raise ValueError("n deve ser multimo de 3")
    
    h = (b - a) / n

    soma = f(a) + f(b)

    for i in range(1, n):
        x_i = a + i * h
        if i % 3 == 0:
            soma += 2 * f(x_i)
        else:
            soma += 3 * f(x_i)
        
    resultado = (3 * h / 8) * soma
    return resultado

limite_inferior = 0
limite_superior = 100
intervalos = 120

integral = simpson38(limite_inferior, limite_superior, intervalos)

print(f"valor é: {integral:.6}")