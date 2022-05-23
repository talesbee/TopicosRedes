
import requests
import json
from gns3fy import Gns3Connector, Project

def buscalinks(urlServidor, projetcID):

    class linkOject:
        Rota = ''
        ID = ''
        
    nodesLinksList = []

    server = Gns3Connector(urlServidor)

    nodes = server.get_nodes(projetcID)

    links = server.get_links(projetcID)

    for node in nodes:
        print('Node: '+node.get('name')+' ID: '+node.get('node_id'))

    for link in links:
        nodesLink = link.get('nodes')
        node1Name = ''
        node2Name = ''
        node1 = nodesLink[0].get('node_id')
        node2 = nodesLink[1].get('node_id')
        for node in nodes:
            if node1 == node.get('node_id'):
                node1Name = node.get('name')
                
            if node2 == node.get('node_id'):
                node2Name = node.get('name')
                
        print('Link: '+node1Name+' -> '+node2Name + ' / ID: '+link.get('link_id'))
        rotas = linkOject()
        rotas.Rota = node1Name+':'+node2Name
        rotas.ID = link.get('link_id')    
        nodesLinksList.append(rotas)
    return nodesLinksList





def soDeixaRota(rotas, urlServidor, projetcID, nodesLinksList):
    linkSuspend = {"suspend": True} 
    for link in nodesLinksList:
        for rota in rotas:
            if link.Rota == rota:
                print('Suspendendo a rota: '+link.Rota)    
                link1 = urlServidor+'/v2/projects/'+projetcID+'/links/'+link.ID
                x = requests.put(link1, data = json.dumps(linkSuspend))

def ativaTodasRotas(urlServidor, projetcID, nodesLinksList):
    linkStart = {"suspend": False}
    for link in nodesLinksList:
        print('Ativando a rota: '+link.Rota)    
        urlRota = urlServidor+'/v2/projects/'+projetcID+'/links/'+link.ID
        x = requests.put(urlRota, data = json.dumps(linkStart))



buscalinks('http://localhost:3080','2073e2d8-6fd3-4ceb-82a7-20698ae8f6ba')



# while(True):
#     ativaTodasRotas()
#     escolheRota = randint(0, 2)
#     print('Rota escolhida: ',escolheRota)
#     print('Rota Delay: 0, Rota Jitter: 1, Rota PackageLost: 2')
#     soDeixaRota(RotasList[escolheRota])
#     sleep(40)










