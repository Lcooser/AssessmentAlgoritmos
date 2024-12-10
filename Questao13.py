def knapsack_recursivo(capacidade, pesos, valores, n):
    if n == 0 or capacidade == 0:
        return 0
    if pesos[n-1] > capacidade:
        return knapsack_recursivo(capacidade, pesos, valores, n-1)
    else:
        return max(valores[n-1] + knapsack_recursivo(capacidade - pesos[n-1], pesos, valores, n-1),
                   knapsack_recursivo(capacidade, pesos, valores, n-1))

pesos = [1, 2, 3]
valores = [10, 20, 30]
capacidade = 4
print(knapsack_recursivo(capacidade, pesos, valores, len(pesos)))
