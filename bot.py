import discord
from discord.ext import commands
import asyncio
import time
import requests
import datetime
import os
import datetime
import time
from datetime import datetime
import platform
import json
from urllib.parse import quote
from urllib.request import urlopen
import urllib.request as urlreq
from urllib.request import urlopen
from urllib.request import unquote
from random import *
from urllib import request
from io import StringIO
from io import BytesIO



#################################################################################################################
#################################################################################################################
#################################################################################################################
blacklist = []
file = open("cogs/txt/blacklist.txt", 'r')
for name in file.readlines():
  if len(name.strip()) > 0 :
    blacklist.append(name.strip())
file.close()


time = datetime.now()
client = commands.Bot(command_prefix="y.")
modulos = ["cogs.idioma","cogs.canais","cogs.cargos","cogs.id-servidor","cogs.perfil","cogs.servidor","cogs.youtube","cogs.002"]
client.remove_command("help")

#################################################################################################################
#################################################################################################################
#################################################################################################################

@client.event
async def on_ready():
    print("=================================")
    print("Nome : %s" % client.user.name)
    print("ID : %s" % client.user.id)
    print("Servidores : %s" % str(len(client.servers)))
    print("Canais : %s" % str(len(set(client.get_all_channels()))))
    print("Emojis : %s" % str(len(set(client.get_all_emojis()))))
    print("Usuários : %s" % str(len(set(client.get_all_members()))))
    print("=================================")

#################################################################################################################
#################################################################################################################
#################################################################################################################

@client.event
async def on_message(message):
    if message.content.lower().startswith("y.eval"):
      if message.author.id == "235206988160696320":
        try:
            await client.send_message(message.channel, str(eval(message.content[7:])))
        except Exception as e:
            await client.send_message(message.channel, repr(e))


    if message.content.lower().startswith("y.reload"):
      if message.author.id == "235206988160696320":
        try:
            cogs = message.content[9:]
            client.unload_extension("cogs."+cogs)
            await asyncio.sleep(0.2)
            client.load_extension("cogs."+cogs)
            ping = "<:reload:461663444177780737> O modulo "+message.content[9:]+" foi recarregado."
            embed= discord.Embed(description=ping, color=0xF08FA2)
            await client.send_message(message.channel, embed=embed)
        except Exception as e:
            await client.send_message(message.channel, repr(e))
    
    if message.content.lower().startswith("y.lat"):
      if message.author.id == "235206988160696320":
         ping = os.popen('ping '+message.content[6:]+' -n 4')
         result = ping.readlines()
         msLine1 = result[1].strip()
         msLine2 = result[2].strip()
         msLine3 = result[3].strip()
         msLine4 = result[4].strip()
         msLine5 = result[5].strip()
         msLine6 = result[6].strip()
         msLine7 = result[7].strip()
         msLine8 = result[8].strip()
         msLine9 = result[9].strip()
         msLine10 = result[10].strip()
         msLine11 = result[11].strip()
         pix = "\n"+msLine1+"\n"+msLine2+"\n"+msLine3+"\n"+msLine4+"\n"+msLine5+"\n"+msLine6+"\n"+msLine7+"\n"+msLine8+"\n"+msLine9+"\n"+msLine10+"\n"+msLine11
         pg = str(pix).replace("M‚dia","Media").replace("n£mero","numero").replace(" ximo = ","aximo = ").replace("M¡nimo","Minimo").replace("Estat¡sticas","Estatisticas")
         texto = "```"+pg+"```"
         await client.send_message(message.channel, texto)
      else:
        pass


    await client.process_commands(message)

#################################################################################################################
#################################################################################################################
#################################################################################################################

if __name__ =="__main__":
    for script in modulos:
        try:
            client.load_extension(script)
        except Exception as e :
            exc = '{}.{}'.format(type(e).__name__,e)
            print('[Erro] : {} - {}'.format(script,e))

#################################################################################################################
#################################################################################################################
#################################################################################################################

client.run('NDYxNTIwMDQ5MjI5MDA0ODMw.DhWhmw.1p_3O1KGogg9MhTHd-XZ3ZkRN60')
