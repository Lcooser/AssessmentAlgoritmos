import time

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

precos = [i for i in range(1000, 0, -1)]
start = time.time()
bubble_sort(precos)
print("Tempo de execução para 1 mil:", time.time() - start)

precos = [i for i in range(10000, 0, -1)]
start = time.time()
bubble_sort(precos)
print("Tempo de execução para 10 mil:", time.time() - start)
