import csv
from time import sleep




def rodarArquivo (nomeArquivo,saida, label,labelP,labelDU,perda=True,mult=1,):
    pacotes = []

    class pack:
        label = ''
        time = ''
        tipo = '' #request / reply
        teveReply = False

    # 1. abrir o arquivo
    with open(nomeArquivo, encoding='utf-8') as arquivo_referencia:
        with open(saida, 'w' , encoding='utf-8') as f: #Mudar o csv que vai ter que escrever
            # 2. ler a tabela
            tabela = csv.reader(arquivo_referencia, delimiter=',')

            # 3. navegar pela tabela
            for l in tabela:    
                if len(l) >= 6:
                    
                    if l[6].split(' ')[0] == 'Echo':             
                        data = pack()
                        data.time = l[1]
                        data.tipo = l[6].split(' ')[2] 
                        pacotes.append(data)

                    if l[6].split(' ')[0] == 'Destination':             
                        data = pack()
                        data.time = 0
                        data.tipo = 'D_U' 
                        pacotes.append(data)

            for idx, p in enumerate(pacotes):
                pk = pack()     
                pk.label = label

                if p.tipo == 'request':
                    if len(pacotes) > (idx + 1)  :  
                        if pacotes[idx+1].tipo == 'reply':

                            pk.time= float(pacotes[idx+1].time) - float(p.time)           
                            pk.time= (pk.time*mult)
                            pk.time = int(pk.time)
                            
                            string = str(pk.time) +","+str(1) +","+str(0)+","+str(pk.label)


                            f.write(string + "\n")

                        else:
                            if(perda): 
                                pk.teveReply = 0
                                pk.time = 0
        
                                string = str(0) +","+str(0) +","+str(0)+","+str(labelP)


                                f.write(string + "\n") 
                if p.tipo == 'D_U':
                    pk.teveReply = 0
                    pk.time = 0
                    string = str(0) +","+str(0) +","+str(1)+","+str(labelDU)

                    f.write(string + "\n") 

