from time import sleep
from os import path, remove 

import Processador

import Misturador

import ExecutandoIA

entradaD = './entrada/d0.csv'
entradaJ = './entrada/j0.csv'
entradaN = './entrada/n0.csv'


saidaD = './saida/processadoD.csv'
saidaJ = './saida/processadoJ.csv'
saidaN = './saida/processadoN.csv'

saidaM = './saida/arquivoProcessado.csv'

print('Limpando a pasta de saida!')

if path.exists(saidaD):
    remove(saidaD)
if path.exists(saidaJ):
    remove(saidaJ)
if path.exists(saidaN):
    remove(saidaN)
if path.exists(saidaM):
    remove(saidaM)

sleep(3)

print('Processando Delay')

#Entrada (nomeArquivo,saida, label,labelP, labelDu,perda=True,mult=10000)
#Saida: ["tempo resposta", "teve resposta" 0 / 1, "Destination unreachable" 0 / 1, "label"]
Processador.rodarArquivo(entradaD,saidaD,'0','3','4',True,10000)
sleep(5)

print('Processando Jitter')
#Entrada (nomeArquivo,saida, label,labelP, labelDu,perda=True,mult=1,)
#Saida: ["tempo resposta", "teve resposta" 0 / 1, "Destination unreachable" 0 / 1, "label"]
Processador.rodarArquivo(entradaJ,saidaJ,'1','3','4',True,10000)
sleep(5)

print('Processando Normal')
#Entrada (nomeArquivo,saida, label,labelP, labelDu,perda=True,mult=1,)
#Saida: ["tempo resposta", "teve resposta" 0 / 1, "Destination unreachable" 0 / 1, "label"]
Processador.rodarArquivo(entradaN,saidaN,'2','3','3',True,10000)
sleep(5)

print('Misturando')
Misturador.misturaArquivos(saidaD, saidaJ, saidaN,saidaM)
sleep(3)

print('Executando IA')
ExecutandoIA.executaIA(saidaM, 0.2)

