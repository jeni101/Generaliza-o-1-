float simpson_38_generalizado(float a, float b, int n, float (*f)(float)) {
    if (n % 3 != 0) return -1; // Erro: n deve ser múltiplo de 3
    
    float h = (b - a) / n;
    float soma = f(a) + f(b);
    
    for (int i = 1; i < n; i++) {
        if (i % 3 == 0)
            soma += 2 * f(a + i * h);
        else
            soma += 3 * f(a + i * h);
    }
    
    return (3.0 * h / 8.0) * soma;
}