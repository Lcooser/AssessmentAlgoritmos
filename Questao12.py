import os

def listar_arquivos(diretorio):
    for item in os.listdir(diretorio):
        caminho = os.path.join(diretorio, item)
        if os.path.isdir(caminho):
            listar_arquivos(caminho)
        else:
            print(caminho) 

listar_arquivos('caminho da pasta')
