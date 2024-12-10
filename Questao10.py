class Navegador:
    def __init__(self):
        self.pilha_voltar = []
        self.pilha_avancar = []

    def visitar(self, pagina):
        self.pilha_voltar.append(pagina)
        self.pilha_avancar.clear() 

    def voltar(self):
        if len(self.pilha_voltar) > 1:
            self.pilha_avancar.append(self.pilha_voltar.pop())
            return self.pilha_voltar[-1]
        return "Não há páginas anteriores"

    def avancar(self):
        if self.pilha_avancar:
            pagina = self.pilha_avancar.pop()
            self.pilha_voltar.append(pagina)
            return pagina
        return "Não há páginas para avançar"

navegador = Navegador()
navegador.visitar("Página 1")
navegador.visitar("Página 2")
print(navegador.voltar())  
print(navegador.avancar()) 
