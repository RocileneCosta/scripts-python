# -*- coding: utf-8 -*-
import shutil
import os
from glob import glob
import datetime
from datetime import date
from pprint import pprint

#coletando a data de hoje e convertendo para um formato conhecido
hoje = date.today()
passado = date.fromordinal(hoje.toordinal()-30)
hoje = hoje.toordinal()

#Listagem de pastas por cliente
lista_clientes = ["cli1", "cli 2"]

for cliente in lista_clientes:
    #Indico o caminho da pasta *Origem
    pasta = "/home/infra/Documentos/%s/dez" % cliente

    #Alterando o caminho atual de trabalho para pasta *Origem
    origem = os.chdir(pasta)

    #Exibindo onde estou
    #destino = os.getcwd()

    #Listando o que tem no diretório
    origem = os.listdir()
    #pprint(origem)

    for arquivo in origem:
        info = os.stat(arquivo)
        #Armazena a data de criação do arquivo
        a = info.st_mtime

        #Converte para um tipo conhecido
        a = datetime.datetime.fromtimestamp(a)
        data_arquivo = a.toordinal()
        
        #Faz o cálculo para identificar o tempo de criação do arquivo
        diferenca = hoje - data_arquivo
        
        if diferenca > 30:
                    
            #Se o arquivo foi criado a mais de 30 dias vou mover para o novo destino
            shutil.move("%s" % arquivo, "/home/infra/Downloads/%s/dez" %cliente)

            #imprimindo arquivos movidos
            print(arquivo, a)

#https://pythonhelp.wordpress.com/2012/07/10/trabalhando-com-datas-e-horas-em-python-datetime/
#http://turing.com.br/pydoc/2.7/tutorial/stdlib.html
#http://carneiro.blog.br/um/Navegando-em-diret%C3%B3rios-no-Python.html


