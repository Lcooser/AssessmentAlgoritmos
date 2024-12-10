class Hashtable:
    def __init__(self):
        self.tabela = {}

    def adicionar(self, chave, valor):
        self.tabela[chave] = valor

    def buscar(self, chave):
        return self.tabela.get(chave, "Usuário não encontrado")

tabela_perfis = Hashtable()
tabela_perfis.adicionar("alice", {"nome": "Alice", "idade": 25})
tabela_perfis.adicionar("bob", {"nome": "Bob", "idade": 30})

print(tabela_perfis.buscar("alice"))
