# -*- coding: utf-8 -*-
import  telepot
import string
import requests 
import json
from bs4 import BeautifulSoup
import sys
import key

bot = key.bot

import time
from telepot.loop import MessageLoop
response = bot.getUpdates()

def consulta(param):
    r = requests.post("http://consultaoperadora.com.br/site2015/resposta.php",  data = {'tipo':'consulta', 'numero':param})   
    soup = BeautifulSoup(r.content, 'html.parser')
    i=0
    st ='';  
    for p in soup.findAll('span', {"class": "lead laranja"}):
        if(i==0):
            st = st+" *Operadora:*"
        if(i==1):
            st = st+" *Portado:* "
        if(i==2):
            st = st+" *Numero:* "
        st= st +" _"+ p.text+"_  \n"
        i = i+1
    return st

def handle(msg):

    if(msg['chat']['type']=='supergroup'):
        chat_id= msg['chat']['id']
        command = msg['text']
        #bot.sendMessage(chat_id, "Sim, entao Temos um grupo..."

    else:
        chat_id = msg['chat']['id']
        if not msg['contact']['phone_number']:
          command = msg['text']  
        else :
          command = msg['contact']['phone_number']
        nome = msg['chat']['first_name']
    if command == '/start':
           bot.sendMessage(chat_id, "OLa, SOu um bot que identifica a operadora de um contato!")
    elif(command):
          bot.sendMessage(chat_id, consulta(command), parse_mode='Markdown')
    else:
            bot.sendMessage(chat_id, "Apenos entendo contatos, vcard ou numero de telefone xx12341234")


MessageLoop(bot, handle).run_as_thread()

while 1:
      time.sleep(5)

