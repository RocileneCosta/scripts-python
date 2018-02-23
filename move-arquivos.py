# -*- coding: utf-8 -*-
import shutil
import os
from glob import glob
import datetime
from datetime import date

def VerificaArquivo (diretorio, arquivo):
    print("*estou no verifica arquivo")
    caminho = "%s%s" % (diretorio, arquivo)
    existe = os.path.isfile(caminho)
    return existe

def MudaDiretorio (caminho):
    diretorio = os.chdir(caminho)
    arquivos = os.listdir(diretorio)
    print("Os aquivos da pasta são estes: %s" %arquivos)
    
hoje = date.today()
print("\nOi, hoje %s vou ajudá-lo a trabalhar com seus arquivos!" %hoje)
print("exemplos de caminho: \n--> /home/seu-usuario/Documentos/ *Documentos*\n--> /home/seu-usuario/.local/share/Trash/files/ *Lixeira*")
print("                         ")
caminho1 = str(input("Insira o caminho do diretório de origem --> "))
MudaDiretorio(caminho1)

print("                         ")
caminho2 = str(input("Insira o caminho do diretório de destino --> "))
MudaDiretorio(caminho2)

#         /home/miti/Documentos/pasta2/
cond = 0
while cond <= 5:
        
    print("\nO que deseja fazer? ") 
    print("|| 1-Copiar || 2-Mover || 3-Deletar ||")
    print("Ou ctrl+c para sair")
    opcao = int(input("--> "))

    if opcao == 1:
        
        for arquivo in arquivos:
            verifica = "%s%s" % (caminho, arquivo)
            existe = os.path.isfile(verifica)
            
            if existe == False:
                shutil.copy(arquivo, caminho)
                                   
            else:
                print("o %s já existe no destino, não precisa mover" %arquivo)
                print("                      ")       
            
        break

    if opcao == 2:
        destino = str(input("Digite o destino: "))
        
        for arquivo in arquivos:
            VerificaArquivo(destino, arquivo) 

            if existe == True:
                TrocaDiretorio(caminho)
                shutil.move(arquivo, destino)
            else:
                print("o %s já existe no destino, não precisa mover" %arquivo)
                print("                      ")        
        
        print("                         ")
        print("Os arquivos foram copiados")
        destino = os.listdir(destino)
        print(destino)   
        break
        
    if opcao == 3:
        for arquivo in arquivos:
            os.remove(arquivo)
        
        print("                         ")
        print("Os arquivos foram removidos, a pasta ficou vazia!")
        destino = os.listdir(local)
        print(destino)    
        break

    elif opcao != 1:
        cond += 1
        print("\n------------Vamos de novo------------")
