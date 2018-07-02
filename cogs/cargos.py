
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


class _cargos():
    def __init__(self, client):
        self.client = client

    
    @commands.command(pass_context = True, aliases=['cargos',"roles"], Pm=False)
    async def _cargos(self,ctx):
       print("Comando [Cargo/Roles] usado por "+str(ctx.message.author)+" em "+str(ctx.message.server.name))
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
        if xtx[1] == "servidor" or xtx[1] == "server": 
          servidor = ctx.message.server
          texto = [x.mention for x in servidor.role_hierarchy if x.mention != "@everyone"]
          stringtexto = "\n".join(texto)
          texto2 = [x.id for x in servidor.role_hierarchy if x.mention != "@everyone"]
          stringtexto2 = "\n".join(texto2)
          servidor = ctx.message.server
          if servidor.icon_url == "":
             img = "https://ethospsicotestes.com.br/images/sem_foto.png"
          else:
            img = servidor.icon_url  
          embed = discord.Embed(description="<:zero_two:461659150989000705> Aqui abaixo está listado todos os cargos do "+ctx.message.server.name+".",colour= 0xF08FA2)
          embed.add_field(name="<:lista_2:461658096289316864> Nome", value=""+stringtexto+"", inline=True)
          embed.add_field(name="<:lista_1:461658095634874388> Id", value=" "+stringtexto2+"", inline=True)
          embed.set_thumbnail(url=img)
          embed.set_footer(text=self.client.user.name+" © 2018")
          await self.client.say(embed = embed)
        elif xtx[1] == "minhas" or xtx[1] == "my": 
          texto = [r.mention for r in ctx.message.author.roles if r.name != "@everyone"]
          stringtexto = "\n".join(texto)
          texto2 = [r.id for r in ctx.message.author.roles if r.name != "@everyone"]
          stringtexto2 = "\n".join(texto2)
          embed = discord.Embed(description="<:zero_two:461659150989000705> Olá "+ctx.message.author.mention+", aqui abaixo está listado todos seus cargo no servidor "+ctx.message.server.name+".",colour= 0xF08FA2)
          embed.add_field(name="<:lista_2:461658096289316864> Nome", value=stringtexto, inline=True)
          embed.add_field(name="<:lista_1:461658095634874388> Id", value=stringtexto2, inline=True)
          embed.set_thumbnail(url=ctx.message.author.avatar_url)
          embed.set_footer(text=self.client.user.name+" © 2018")
          await self.client.say(embed = embed)
        elif xtx[1]: 
          usuario_id = xtx[1].replace("<", "").replace("@", "").replace("!", "").replace(">", "")
          usuario = ctx.message.server.get_member(usuario_id)
          texto = [r.mention for r in usuario.roles if r.name != "@everyone"]
          stringtexto = "\n".join(texto)
          texto2 = [r.id for r in usuario.roles if r.name != "@everyone"]
          stringtexto2 = "\n".join(texto2)
          if usuario.avatar_url == "":
            img = ""
          else:
            img = usuario.avatar_url    
          embed = discord.Embed(description="<:zero_two:461659150989000705> A lista de cargo do usuário "+usuario.mention+" no servidor "+ctx.message.server.name+" é esta.",colour= 0xF08FA2)
          embed.add_field(name="<:lista_2:461658096289316864> Nome", value=""+stringtexto+"", inline=True)
          embed.add_field(name="<:lista_1:461658095634874388> Id", value=" "+stringtexto2+"", inline=True)
          embed.set_thumbnail(url=img)
          embed.set_footer(text=self.client.user.name+" © 2018")
          await self.client.say(embed = embed)
       else:
         if xtx[1] == "servidor" or xtx[1] == "server": 
            servidor = ctx.message.server
            texto = [x.mention for x in servidor.role_hierarchy if x.mention != "@everyone"]
            stringtexto = "\n".join(texto)
            texto2 = [x.id for x in servidor.role_hierarchy if x.mention != "@everyone"]
            stringtexto2 = "\n".join(texto2)
            servidor = ctx.message.server
            if servidor.icon_url == "":
               img = "https://ethospsicotestes.com.br/images/sem_foto.png"
            else:
              img = servidor.icon_url  
            embed = discord.Embed(description="<:zero_two:461659150989000705> Here you can find all the roles of the "+ctx.message.server.name+".",colour= 0xF08FA2)
            embed.add_field(name="<:lista_2:461658096289316864> Name", value=""+stringtexto+"", inline=True)
            embed.add_field(name="<:lista_1:461658095634874388> Id", value=" "+stringtexto2+"", inline=True)
            embed.set_thumbnail(url=img)
            embed.set_footer(text=self.client.user.name+" © 2018")
            await self.client.say(embed = embed)
         elif xtx[1] == "minhas" or xtx[1] == "my": 
           texto = [r.mention for r in ctx.message.author.roles if r.name != "@everyone"]
           stringtexto = "\n".join(texto)
           texto2 = [r.id for r in ctx.message.author.roles if r.name != "@everyone"]
           stringtexto2 = "\n".join(texto2)
           if ctx.message.author.avatar_url == "":
              img = "https://ethospsicotestes.com.br/images/sem_foto.png"
           else:
             img = ctx.message.author.avatar_url    
           embed = discord.Embed(description="<:zero_two:461659150989000705> Hello "+ctx.message.author.mention+", here all your server roles are listed on the server "+ctx.message.server.name+".",colour= 0xF08FA2)
           embed.add_field(name="<:lista_2:461658096289316864> Name", value=""+stringtexto+"", inline=True)
           embed.add_field(name="<:lista_1:461658095634874388> Id", value=" "+stringtexto2+"", inline=True)
           embed.set_thumbnail(url=img)
           embed.set_footer(text=self.client.user.name+" © 2018")
           await self.client.say(embed = embed)
         elif xtx[1]: 
           usuario_id = xtx[1].replace("<", "").replace("@", "").replace("!", "").replace(">", "")
           usuario = ctx.message.server.get_member(usuario_id)
           texto = [r.mention for r in usuario.roles if r.name != "@everyone"]
           stringtexto = "\n".join(texto)
           texto2 = [r.id for r in usuario.roles if r.name != "@everyone"]
           stringtexto2 = "\n".join(texto2)
           if usuario.avatar_url == "":
              img = "https://ethospsicotestes.com.br/images/sem_foto.png"
           else:
             img = usuario.avatar_url    
           embed = discord.Embed(description="<:zero_two:461659150989000705> Here is the list of roles of "+usuario.mention+".",colour= 0xF08FA2)
           embed.add_field(name="<:lista_2:461658096289316864> Name", value=""+stringtexto+"", inline=True)
           embed.add_field(name="<:lista_1:461658095634874388> Id", value=" "+stringtexto2+"", inline=True)
           embed.set_thumbnail(url=img)
           embed.set_footer(text=self.client.user.name+" © 2018")
           await self.client.say(embed = embed)

def setup(client):
    client.add_cog(_cargos(client))
