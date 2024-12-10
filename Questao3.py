def busca_linear(contatos, nome_procurado):
    for nome, telefone in contatos:
        if nome == nome_procurado:
            return telefone
    return None

contatos = [("Alice", "123-4567"), ("Bob", "234-5678"), ("Charlie", "345-6789")]
nome_procurado = "Charlie"
telefone = busca_linear(contatos, nome_procurado)
if telefone:
    print(f"Telefone de {nome_procurado}: {telefone}")
else:
    print(f"Contato {nome_procurado} não encontrado")
