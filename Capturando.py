import requests
import json
from time import sleep
from tabulate import tabulate
from random import randint
from gns3fy import Gns3Connector, Project

urlServidor= 'http://localhost:3080'
projetcID = '2073e2d8-6fd3-4ceb-82a7-20698ae8f6ba'

linkPC1 = '1500f49b-071e-4a2e-b501-a2adafabebb5'

linkDelay = 'a3807de3-4274-48ed-b601-76b874d133d6'
linkJitter = 'a496844b-9bf2-4511-bc4b-e975c61b7bed'
linkNormal = 'c8248876-42f7-442b-9f71-ee5becf9677d'

server = Gns3Connector(urlServidor)

mudar = 0
countD = 0
countJ = 0
countN = 0

def capturaStart(name):
    url =  urlServidor+'/v2/projects/'+projetcID+'/links/'+linkPC1+'/start_capture'
    x = requests.post(url, data = json.dumps({"capture_file_name": name}))

def capturaStop():
    url =  urlServidor+'/v2/projects/'+projetcID+'/links/'+linkPC1+'/stop_capture'
    x = requests.post(url)

def linkSuspend(link):
    url = urlServidor+'/v2/projects/'+projetcID+'/links/'+link
    x = requests.put(url, data = json.dumps({"suspend": True}))

def linkStart(link):
    url = urlServidor+'/v2/projects/'+projetcID+'/links/'+link
    x = requests.put(url, data = json.dumps({"suspend": False}))


while(True):
    print('Parando Captura')
    capturaStop()
    sleep(5)
    print('Desabilitando os Links')
    linkSuspend(linkJitter)
    linkSuspend(linkDelay)
    linkSuspend(linkNormal)
    sleep(5)

    if(mudar == 0):
        print('Captura Delay ',countD)
        linkStart(linkDelay)
        sleep(5)

        name = 'Delay_'+str(countD)+'.pcap'
        capturaStart(name)
        countD = countD + 1

    if mudar == 1:        
        print('Captura Jitter ', countJ)
        linkStart(linkJitter)
        sleep(5)
        name = 'Jitter_'+str(countJ)+'.pcap'
        capturaStart(name)
        countJ = countJ + 1

    if mudar == 2:        
        print('Captura Normal ',countN)
        linkStart(linkNormal)
        sleep(5)

        name = 'Normal_'+str(countN)+'.pcap'
        capturaStart(name)
        countN = countN + 1

    mudar = mudar + 1
    if mudar == 3: mudar = 0
    sleep(3600)
