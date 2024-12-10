class Fila:
    def __init__(self):
        self.chamados = []

    def inserir(self, chamado):
        self.chamados.append(chamado)

    def remover(self):
        if len(self.chamados) > 0:
            return self.chamados.pop(0)
        return "Nenhum chamado para remover"

fila_atendimento = Fila()
fila_atendimento.inserir("Chamado 1")
fila_atendimento.inserir("Chamado 2")
fila_atendimento.inserir("Chamado 3")

print(fila_atendimento.remover()) 
print(fila_atendimento.remover()) 
print(fila_atendimento.remover()) 
