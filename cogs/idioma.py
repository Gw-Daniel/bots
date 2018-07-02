
import discord
from discord.ext import commands
import os
import random
import time
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

admin= []
file = open("cogs/txt/admin.txt", 'r')
for name in file.readlines():
  if len(name.strip()) > 0 :
    admin.append(name.strip())
file.close()

class _idioma():
    def __init__(self, client):
        self.client = client
    
 
    @commands.command(pass_context = True, aliases=['language','idioma'], Pm=False)
    async def _idioma(self,ctx):
       print("Comando [idioma/language] usado por "+str(ctx.message.author)+" em "+str(ctx.message.server.name))
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


       if ctx.message.author.id not in english:
         ping = '<:idioma:461658094657601537> Had a change in my language and he changed to the **English**.'
         embed= discord.Embed(description=str(ping), color=0xF08FA2)
         await self.client.say(embed=embed)
         english.append(ctx.message.author.id)
         f = open("cogs/txt/english.txt", "w")
         f.write("\n".join(english))
         f.close() 
       else:
         ping = '<:idioma:461658094657601537> Teve uma alteração no meu idioma e ele mudou para o **Português**.'
         embed = discord.Embed(description=str(ping), color=0xF08FA2)
         await self.client.say(embed=embed)
         english.remove(ctx.message.author.id)
         f = open("cogs/txt/english.txt", "w")
         f.write("\n".join(english))
         f.close() 

def setup(client):
    client.add_cog(_idioma(client))
