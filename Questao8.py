def selection_sort(lista):
    for i in range(len(lista)):
        menor_indice = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[menor_indice]:
                menor_indice = j
        lista[i], lista[menor_indice] = lista[menor_indice], lista[i]

pontuacoes = [1500, 1200, 2000, 1000, 1800]
selection_sort(pontuacoes)
print(pontuacoes)
