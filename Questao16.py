class Node:
    def __init__(self, chave):
        self.chave = chave
        self.esquerda = None
        self.direita = None

class BST:
    def __init__(self):
        self.raiz = None

    def inserir(self, chave):
        if not self.raiz:
            self.raiz = Node(chave)
        else:
            self._inserir_recursivo(self.raiz, chave)

    def _inserir_recursivo(self, node, chave):
        if chave < node.chave:
            if node.esquerda:
                self._inserir_recursivo(node.esquerda, chave)
            else:
                node.esquerda = Node(chave)
        else:
            if node.direita:
                self._inserir_recursivo(node.direita, chave)
            else:
                node.direita = Node(chave)

    def buscar(self, chave):
        return self._buscar_recursivo(self.raiz, chave)

    def _buscar_recursivo(self, node, chave):
        if node is None or node.chave == chave:
            return node
        elif chave < node.chave:
            return self._buscar_recursivo(node.esquerda, chave)
        else:
            return self._buscar_recursivo(node.direita, chave)

    def remover(self, raiz, chave):
        if raiz is None:
            return raiz
        if chave < raiz.chave:
            raiz.esquerda = self.remover(raiz.esquerda, chave)
        elif chave > raiz.chave:
            raiz.direita = self.remover(raiz.direita, chave)
        else:
            if raiz.esquerda is None:
                return raiz.direita
            elif raiz.direita is None:
                return raiz.esquerda
            raiz.chave = self._minimo(raiz.direita)
            raiz.direita = self.remover(raiz.direita, raiz.chave)
        return raiz

    def _minimo(self, node):
        while node.esquerda:
            node = node.esquerda
        return node.chave

    def em_ordem(self, raiz):
        if raiz:
            self.em_ordem(raiz.esquerda)
            print(raiz.chave, end=" ")
            self.em_ordem(raiz.direita)

produtos = [45, 25, 65, 20, 30, 60, 70]
arvore_inventario = BST()
for produto in produtos:
    arvore_inventario.inserir(produto)

print("Árvore original (em ordem):")
arvore_inventario.em_ordem(arvore_inventario.raiz)
print("\n")

arvore_inventario.remover(arvore_inventario.raiz, 20)
print("Árvore após remover 20 (nó folha):")
arvore_inventario.em_ordem(arvore_inventario.raiz)
print("\n")

arvore_inventario.remover(arvore_inventario.raiz, 25)
print("Árvore após remover 25 (nó com um filho):")
arvore_inventario.em_ordem(arvore_inventario.raiz)
print("\n")

arvore_inventario.remover(arvore_inventario.raiz, 45)
print("Árvore após remover 45 (nó com dois filhos):")
arvore_inventario.em_ordem(arvore_inventario.raiz)
