# -*- coding: utf-8 -*-
import shutil
import os
from glob import glob
import datetime
from datetime import date
from pprint import pprint

hoje = date.today()
print("\nOi, hoje %s vou ajudá-lo a trabalhar com seus arquivos!" %hoje)

#Vamos escolher o diretório
local = os.getcwd()
print("Nós estamos aqui: %s" %local)
print("Quer mudar de diretório?")

quero = input("sim ou nao?:  ")

if quero == sim:
    print("Vamos escolher um diretório para trabalhar!")
else:
    print("Vamos ficar aqui: ")    

cond = 0
while cond <= 5:
        
    print("\nO que deseja fazer? ") 
    print("|| 1-Copiar || 2-Mover || 3-Deletar || \n")
    opcao = input( "Digite o valor: \n")

    if opcao == 1:
        print("Vamos Copiar")
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
        
        

"""
print("Informe o diretório que iremos ")
#Vamos agora listar as pastas do diretório

pasta = "/home/infra/Documentos/%s/dez" % cliente


    #Alterando o caminho atual de trabalho para pasta *Origem
    origem = os.chdir(pasta)

    #Exibindo onde estou
    #destino = os.getcwd()

    #Listando o que tem no diretório
    origem = os.listdir()
    #pprint(origem)
"""

