import csv
from random import randint

def abreArquivo(arquivo):
    lista = []
    with open(arquivo,  encoding='utf-8') as arquivo_referencia:
        reader = csv.reader(arquivo_referencia)
        for linha in reader:
            lista.append(linha)
    return lista        


def misturaArquivos(arquivo1, arquivo2, arquivo3,saida):
    lista1 = abreArquivo(arquivo1)
    lista2 = abreArquivo(arquivo2)
    lista3 = abreArquivo(arquivo3)

    listaMisturada = []

    total1 = len(lista1)
    total2 = len(lista2)
    total3 = len(lista3)

    ultimo1 = 0
    ultimo2 = 0
    ultimo3 = 0

    rodar = True

    while(rodar):
        escolheLista= randint(0, 2)

        if escolheLista==0:
            if ultimo1 <= total1:
                listaMisturada.append(lista1[ultimo1])
                ultimo1 = 1 + ultimo1
                
        if escolheLista==1:
            if ultimo2 <= total2:
                listaMisturada.append(lista2[ultimo2])
                ultimo2 = 1 + ultimo2

        if escolheLista==2:
            if ultimo3 <= total3:
                listaMisturada.append(lista3[ultimo3])
                ultimo3 = 1 + ultimo3

        if ultimo1 == total1 or ultimo2 == total2 or ultimo3 == total3:
            rodar = False

    with open(saida, 'w' , encoding='utf-8') as f:
        for t in listaMisturada:
            string = str(t[0]) +","+ str(t[1]) +","+ str(t[2])+","+ str(t[3])
            f.write(string + "\n")