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

precos = [100, 50, 150, 30, 70, 130, 170]
bst = BST()
for preco in precos:
    bst.inserir(preco)

resultado = bst.buscar(70)
if resultado:
    print(f"Preço {resultado.chave} encontrado.")
else:
    print("Preço não encontrado.")
