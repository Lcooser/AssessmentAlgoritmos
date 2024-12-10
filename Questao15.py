notas = [85, 70, 95, 60, 75, 90, 100]
bst_notas = BST()
for nota in notas:
    bst_notas.inserir(nota)

def minimo(node):
    while node.esquerda:
        node = node.esquerda
    return node.chave

def maximo(node):
    while node.direita:
        node = node.direita
    return node.chave

print("Nota mínima:", minimo(bst_notas.raiz))
print("Nota máxima:", maximo(bst_notas.raiz))
