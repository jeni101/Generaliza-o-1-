float simpson_13_generalizado(float a, float b, int n, float (*f)(float)) {
    if (n % 2 != 0) return -1; // Erro: n deve ser par
    
    float h = (b - a) / n;
    float soma = f(a) + f(b);
    
    for (int i = 1; i < n; i++) {
        if (i % 2 == 0)
            soma += 2 * f(a + i * h);
        else
            soma += 4 * f(a + i * h);
    }
    
    return (h / 3.0) * soma;
}