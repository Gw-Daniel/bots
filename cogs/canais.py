
import discord
from discord.ext import commands
import os
import time
from random import *

blacklist = []
file = open("cogs/txt/blacklist.txt", 'r')
for name in file.readlines():
  if len(name.strip()) > 0 :
    blacklist.append(name.strip())
file.close()

lock = []
file = open("cogs/txt/lock.txt", 'r')
for name in file.readlines():
  if len(name.strip()) > 0 :
    lock.append(name.strip())
file.close()

english = []
file = open("cogs/txt/english.txt", 'r')
for name in file.readlines():
  if len(name.strip()) > 0 :
    english.append(name.strip())
file.close()

admin = []
file = open("cogs/txt/admin.txt", 'r')
for name in file.readlines():
  if len(name.strip()) > 0 :
    admin.append(name.strip())
file.close()


class _canais():
    def __init__(self, client):
        self.client = client

    
    @commands.command(pass_context = True, aliases=['canais',"channels"], Pm=False)
    async def _canais(self,ctx):
       print("Comando [Canais/Channels] usado por "+str(ctx.message.author)+" em "+str(ctx.message.server.name))
       blacklist = []
       file = open("cogs/txt/blacklist.txt", 'r')
       for name in file.readlines():
         if len(name.strip()) > 0 :
            blacklist.append(name.strip())
       file.close()
       
       lock = []
       file = open("cogs/txt/lock.txt", 'r')
       for name in file.readlines():
         if len(name.strip()) > 0 :
            lock.append(name.strip())
       file.close()
       
       english = []
       file = open("cogs/txt/english.txt", 'r')
       for name in file.readlines():
         if len(name.strip()) > 0 :
            english.append(name.strip())
       file.close()
      
       admin = []
       file = open("cogs/txt/admin.txt", 'r')
       for name in file.readlines():
         if len(name.strip()) > 0 :
            admin.append(name.strip())
       file.close()



       if ctx.message.author.id in blacklist:
        if ctx.message.author.id not in english:
          ping = '<:info:461658096628924427> Você está na blacklist da **yui**, e não poderá usar mais comandos!'
          embed= discord.Embed(description=ping, color=0xF08FA2)
          await self.client.send_message(ctx.message.author, embed=embed)
          return
        else:
          ping = "<:info:461658096628924427> You're on **yui** blacklist, and you can not use any more commands!"
          embed= discord.Embed(description=ping, color=0xF08FA2)
          await self.client.send_message(ctx.message.author, embed=embed)
          return

       if ctx.message.channel.id in lock and ctx.message.author.id not in admin:
        if ctx.message.author.id not in english:
          ping = '<:info:461658096628924427> Não foi possivel executar o comando no canal <#'+ctx.message.channel.id+'>, porquê ele foi bloqueado por um administrador.'
          embed= discord.Embed(description=ping, color=0xF08FA2)
          await self.client.send_message(ctx.message.author, embed=embed)
          return
        else:
          ping = "<:info:461658096628924427> Could not execute command on channel <#"+ctx.message.channel.id+">, because it was blocked by an administrator!"
          embed= discord.Embed(description=ping, color=0xF08FA2)
          await self.client.send_message(ctx.message.author, embed=embed)
          return
       if ctx.message.server.id in lock and ctx.message.author.id not in admin:
        if ctx.message.author.id not in english:
          ping = '<:info:461658096628924427> Não foi possivel executar o comando no servidor '+ctx.message.server.name+', porquê eu fui bloqueada por um administrador!'
          embed= discord.Embed(description=ping, color=0xF08FA2)
          await self.client.send_message(ctx.message.author, embed=embed)
          return
        else:
          ping = "<:info:461658096628924427> Could not execute command on server "+ctx.message.server.name+", because I was blocked by an administrator!"
          embed= discord.Embed(description=ping, color=0xF08FA2)
          await self.client.send_message(ctx.message.author, embed=embed)
          return
       xtx = ctx.message.content.split(" ", 1)
       if ctx.message.author.id not in english:
        if xtx[1] == "texto" or xtx[1] == "text": 
          servidor = ctx.message.server
          texto = [y.mention for y in servidor.channels if y.type==discord.ChannelType.text]
          stringtexto = "\n".join(texto)
          texto2 = [y.id for y in servidor.channels if y.type==discord.ChannelType.text]
          stringtexto2 = "\n".join(texto2)
          servidor = ctx.message.server
          if servidor.icon_url == "":
             img = "https://ethospsicotestes.com.br/images/sem_foto.png"
          else:
            img = servidor.icon_url  
          embed = discord.Embed(description="<:zero_two:461659150989000705> Aqui abaixo está listado todos os canais de texto do "+ctx.message.server.name+".",colour= 0xF08FA2)
          embed.add_field(name="<:lista_2:461658096289316864> Nome", value=""+stringtexto+"", inline=True)
          embed.add_field(name="<:lista_1:461658095634874388> Id", value=" "+stringtexto2+"", inline=True)
          embed.set_thumbnail(url=img)
          embed.set_footer(text=self.client.user.name+" © 2018")
          await self.client.say(embed = embed)
        elif xtx[1] == "voz" or xtx[1] == "voice": 
          servidor = ctx.message.server
          texto = [y.mention for y in servidor.channels if y.type==discord.ChannelType.voice]
          stringtexto = "\n".join(texto)
          texto2 = [y.id for y in servidor.channels if y.type==discord.ChannelType.voice]
          stringtexto2 = "\n".join(texto2)
          servidor = ctx.message.server
          if servidor.icon_url == "":
             img = "https://ethospsicotestes.com.br/images/sem_foto.png"
          else:
            img = servidor.icon_url  
          embed = discord.Embed(description="<:zero_two:461659150989000705> Aqui abaixo está listado todos os canais de voz do "+ctx.message.server.name+".",colour= 0xF08FA2)
          embed.add_field(name="<:lista_2:461658096289316864> Nome", value=""+stringtexto+"", inline=True)
          embed.add_field(name="<:lista_1:461658095634874388> Id", value=" "+stringtexto2+"", inline=True)
          embed.set_thumbnail(url=img)
          embed.set_footer(text=self.client.user.name+" © 2018")
          await self.client.say(embed = embed)
       else:
         if xtx[1] == "texto" or xtx[1] == "text": 
          servidor = ctx.message.server
          texto = [y.mention for y in servidor.channels if y.type==discord.ChannelType.text]
          stringtexto = "\n".join(texto)
          texto2 = [y.id for y in servidor.channels if y.type==discord.ChannelType.text]
          stringtexto2 = "\n".join(texto2)
          servidor = ctx.message.server
          if servidor.icon_url == "":
             img = "https://ethospsicotestes.com.br/images/sem_foto.png"
          else:
            img = servidor.icon_url  
          embed = discord.Embed(description="<:zero_two:461659150989000705> Here you can find all the text channels of "+ctx.message.server.name+".",colour= 0xF08FA2)
          embed.add_field(name="<:lista_2:461658096289316864> Nome", value=""+stringtexto+"", inline=True)
          embed.add_field(name="<:lista_1:461658095634874388> Id", value=" "+stringtexto2+"", inline=True)
          embed.set_thumbnail(url=img)
          embed.set_footer(text=self.client.user.name+" © 2018")
          await self.client.say(embed = embed)
         elif xtx[1] == "voz" or xtx[1] == "voice": 
          servidor = ctx.message.server
          texto = [y.mention for y in servidor.channels if y.type==discord.ChannelType.voice]
          stringtexto = "\n".join(texto)
          texto2 = [y.id for y in servidor.channels if y.type==discord.ChannelType.voice]
          stringtexto2 = "\n".join(texto2)
          servidor = ctx.message.server
          if servidor.icon_url == "":
             img = "https://ethospsicotestes.com.br/images/sem_foto.png"
          else:
            img = servidor.icon_url  
          embed = discord.Embed(description="<:zero_two:461659150989000705> Here you can find all the voice channels of "+ctx.message.server.name+".",colour= 0xF08FA2)
          embed.add_field(name="<:lista_2:461658096289316864> Name", value=""+stringtexto+"", inline=True)
          embed.add_field(name="<:lista_1:461658095634874388> Id", value=" "+stringtexto2+"", inline=True)
          embed.set_thumbnail(url=img)
          embed.set_footer(text=self.client.user.name+" © 2018")
          await self.client.say(embed = embed)

def setup(client):
    client.add_cog(_canais(client))
