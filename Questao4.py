def busca_binaria(lista, isbn):
    inicio, fim = 0, len(lista) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == isbn:
            return meio 
        elif lista[meio] < isbn:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1  