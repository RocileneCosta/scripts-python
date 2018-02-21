# -*- coding: utf-8 -*-
import shutil
import os
from glob import glob
import datetime
from datetime import date
from pprint import pprint

def VerificaArquivo (arquivo, pasta):
    local = os.chdir(pasta)
    existe = os.path.isfile(arquivo)
    return existe

def TrocaDiretorio (caminho):
    diretorio = os.chdir(caminho)
    return diretorio

hoje = date.today()
print("\nOi, hoje %s vou ajudá-lo a trabalhar com seus arquivos!" %hoje)
print("Insira o caminho do diretório em que iremos trabalhar.")
print("Como nos exemplos abaixo: \n--> /home/seu-usuario/Documentos *Documentos*\n--> /home/seu-usuario/.local/share/Trash/files *Lixeira*")
print("                         ")
caminho = str(input("--> "))
pasta = TrocaDiretorio(caminho)
arquivos = os.listdir(pasta)
print("\n Estes são os arquivos existentes na pasta:")
print(arquivos)

#/home/miti/Documentos/pasta2
cond = 0
while cond <= 5:
        
    print("\nO que deseja fazer? ") 
    print("|| 1-Copiar || 2-Mover || 3-Deletar ||")
    opcao = int(input("--> "))

    if opcao == 1:
        destino = str(input("Digite o destino: "))
        
        for arquivo in arquivos:
            VerificaArquivo(destino, arquivo) 
            
            if existe == False:
                TrocaDiretorio(caminho)
                shutil.copy(arquivo, destino)
            else:
                print("o %s já existe no destino, não precisa mover" %arquivo)
                print("                      ")       

        print("                         ")
        print("Os arquivos foram copiados")
        destino = os.listdir(destino)
        print(destino)    
        break

    if opcao == 2:
        destino = str(input("Digite o destino: "))
        
        for arquivo in arquivos:
            VerificaArquivo(destino, arquivo) 

            if existe == False:
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