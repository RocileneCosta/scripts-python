# -*- coding: utf-8 -*-
import shutil
import os
from glob import glob
import datetime
from datetime import date
from pprint import pprint

hoje = date.today()
print("\nOi, hoje %s vou ajudá-lo a trabalhar com seus arquivos!" %hoje)

#Escolhendo o diretório
#local = os.getcwd()
#Alterei o diretório para teste
local = os.chdir("/home/miti/Documentos/pasta2")
local = os.getcwd()
print("Nós estamos aqui: %s" %local)
print("Quer mudar de diretório?")
print("Digite: 1-Sim ou 2-Não")
quero = int(input("-->  "))

if quero == 1:
    print("                         ")
    print("Qual o nome do diretório?")
    diretorio = str(input("--> "))
    local = os.chdir(diretorio)
    arquivos = os.listdir(local)
    print("estes são os arquivos existentes na pasta")
    print(arquivos)

if quero == 2:
    print("                         ")
    arquivos = os.listdir(local)
    print("Okay, estes são os arquivos existentes na pasta") 
    print(arquivos)  

elif quero != 1:
        print("\n------------Vamos de novo------------")

cond = 0
while cond <= 5:
        
    print("\nO que deseja fazer? ") 
    print("|| 1-Copiar || 2-Mover || 3-Deletar ||")
    opcao = int(input("--> "))

    if opcao == 1:
        destino = str(input("Digite o destino: "))
        
        for arquivo in arquivos:
            shutil.copy(arquivo, destino)
        
        print("Os arquivos foram copiados")
        destino = os.listdir(destino)
        print(destino)    
        
        break
    if opcao == 2:
        print("Vamos Mover")
        break
    if opcao == 3:
        print("Vamos Deletar")
        break

    elif opcao != 1:
        cond += 1
        print("\n------------Vamos de novo------------")