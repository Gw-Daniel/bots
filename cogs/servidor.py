
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

admin = []
file = open("cogs/txt/admin.txt", 'r')
for name in file.readlines():
  if len(name.strip()) > 0 :
    admin.append(name.strip())
file.close()

class _servidor():
    def __init__(self, client):
        self.client = client

    
    @commands.command(pass_context = True, aliases=['servidor','serverinfo'], Pm=False)
    async def _servidor(self,ctx):
       print("Comando [Servidor/Serverinfo] usado por "+str(ctx.message.author)+" em "+str(ctx.message.server.name))
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
          servidor = ctx.message.server
          criado_em = str(servidor.created_at.strftime("20%y/%m/%d | %H:%M:%S"))
          cargos = len([y.id for y in servidor.role_hierarchy])
          informacao = "\n<:simbolo:461714381156253707> Nome : "+str(servidor.name)+"\n<:simbolo:461714381156253707> Id : "+str(servidor.id)+"\n<:simbolo:461714381156253707> Dono : "+str(servidor.owner)+"\n<:simbolo:461714381156253707> Criado em : "+str(criado_em)+""
          emojis = len([y.id for y in servidor.emojis])
          cargos = len([y.id for y in servidor.role_hierarchy])
          verificao = str(servidor.verification_level).replace("low","Baixa").replace("medium","Média").replace("high","Alta").replace("4","Super Alta").replace("none","Nenhuma")
          localizacao = str(servidor.region).title()
          informacao_add = "\n<:simbolo:461714381156253707> "+str(emojis)+" Emojis"+"\n<:simbolo:461714381156253707> "+str(cargos)+" Cargos"+"\n<:simbolo:461714381156253707> Verificação : "+str(verificao)+"\n<:simbolo:461714381156253707> Localização : "+str(localizacao)+""
          bots= len([y.id for y in servidor.members if y.bot])
          humanos = len([y.id for y in servidor.members if not y.bot])
          usuario_total = bots+humanos
          usuarios = "\n<:simbolo:461714381156253707> "+str(bots)+" Bots\n<:simbolo:461714381156253707> "+str(humanos)+" Humanos"
          online = len([y.id for y in servidor.members if y.status == discord.Status.online])
          afk  = len([y.id for y in servidor.members if y.status == y.status == discord.Status.idle])
          offline = len([y.id for y in servidor.members if y.status == y.status == discord.Status.offline])
          dnd = len([y.id for y in servidor.members if y.status == y.status == discord.Status.dnd])
          status_usuarios ="\n<:simbolo:461714381156253707> "+str(online)+" Online \n<:simbolo:461714381156253707> "+str(afk)+" Ausente \n<:simbolo:461714381156253707> "+str(dnd)+" Não Pertube \n<:simbolo:461714381156253707> "+str(offline)+" Offline"
          texto = len([y.id for y in servidor.channels if y.type==discord.ChannelType.text])
          voz = len([y.id for y in servidor.channels if y.type==discord.ChannelType.voice])
          if texto > 0:
             text = 1
          else:
            text = 0
          if voz > 0:
             voice = 1
          else:
            voice = 0
          categoria = voice+text
          canais = "\n<:simbolo:461714381156253707> "+str(categoria)+" Categoria\n<:simbolo:461714381156253707> "+str(texto)+" Texto\n<:simbolo:461714381156253707> "+str(voz)+" Voz"
          canais_total = texto+voz
          if servidor.icon_url == "":
             img = "https://ethospsicotestes.com.br/images/sem_foto.png"
          else:
            img = servidor.icon_url  
          embed = discord.Embed(colour=0xF08FA2)
          embed.add_field(name="<:info_2:461712111475753000> Informação ", value = informacao, inline=True)
          embed.add_field(name="<:lista_2:461658096289316864> Canais ["+str(canais_total)+"] ", value = canais, inline=True)
          embed.add_field(name="<:usuario:461658093059833857> Status do usuários ", value = status_usuarios, inline=True)
          embed.add_field(name="<:adicional:461658090916413452> Informação Adicional ", value = informacao_add, inline=True)
          embed.set_thumbnail(url=img)
          embed.set_footer(text=self.client.user.name+" © 2018")
          await self.client.say(embed = embed)
       else:
          servidor = ctx.message.server
          criado_em = str(servidor.created_at.strftime("20%y/%m/%d | %H:%M:%S"))
          cargos = len([y.id for y in servidor.role_hierarchy])
          informacao = "\n<:simbolo:461714381156253707> Name : "+str(servidor.name)+" "+"\n<:simbolo:461714381156253707> Id : "+str(servidor.id)+" ""\n<:simbolo:461714381156253707> Owner : "+str(servidor.owner)+" \n<:simbolo:461714381156253707> Created on : "+str(criado_em)+" "
          emojis = len([y.id for y in servidor.emojis])
          cargos = len([y.id for y in servidor.role_hierarchy])
          verificao = str(servidor.verification_level).replace("low","Low").replace("medium","Medium").replace("high","High").replace("4","Super High").replace("none","None")
          localizacao = str(servidor.region).title()
          informacao_add = "\n<:simbolo:461714381156253707> "+str(emojis)+" Emojis"+"\n<:simbolo:461714381156253707> "+str(cargos)+" Roles"+"\n<:simbolo:461714381156253707> Verification : "+str(verificao)+" "+"\n<:simbolo:461714381156253707> Location : "+str(localizacao)+" "
          bots= len([y.id for y in servidor.members if y.bot])
          humanos = len([y.id for y in servidor.members if not y.bot])
          usuario_total = bots+humanos
          usuarios = "\n<:simbolo:461714381156253707> "+str(bots)+" Bots\n<:simbolo:461714381156253707> "+str(humanos)+" Humans"
          online = len([y.id for y in servidor.members if y.status == discord.Status.online])
          afk  = len([y.id for y in servidor.members if y.status == y.status == discord.Status.idle])
          offline = len([y.id for y in servidor.members if y.status == y.status == discord.Status.offline])
          dnd = len([y.id for y in servidor.members if y.status == y.status == discord.Status.dnd])
          status_usuarios ="\n<:simbolo:461714381156253707> "+str(online)+" Online \n<:simbolo:461714381156253707> "+str(afk)+" Absent \n<:simbolo:461714381156253707> "+str(dnd)+" DnD \n<:simbolo:461714381156253707> "+str(offline)+" Offline"
          texto = len([y.id for y in servidor.channels if y.type==discord.ChannelType.text])
          voz = len([y.id for y in servidor.channels if y.type==discord.ChannelType.voice])
          if texto > 0:
             text = 1
          else:
            text = 0
          if voz > 0:
             voice = 1
          else:
            voice = 0
          if servidor.icon_url == "":
             img = "https://ethospsicotestes.com.br/images/sem_foto.png"
          else:
            img = servidor.icon_url  
          categoria = voice+text
          canais = "\n<:simbolo:461714381156253707> "+str(categoria)+" Category\n<:simbolo:461714381156253707> "+str(texto)+" Text\n<:simbolo:461714381156253707> "+str(voz)+" Voice"
          canais_total = texto+voz
          embed = discord.Embed(colour=0xF08FA2)
          embed.add_field(name="<:info_2:461712111475753000> Information ", value = informacao, inline=True)
          embed.add_field(name="<:lista_2:461658096289316864> Channels ["+str(canais_total)+"] ", value = canais, inline=True)
          embed.add_field(name="<:usuario:461658093059833857> User Status ", value = status_usuarios, inline=True)
          embed.add_field(name="<:adicional:461658090916413452> Additional information ", value = informacao_add, inline=True)
          embed.set_thumbnail(url=img)
          embed.set_footer(text=self.client.user.name+" © 2018")
          await self.client.say(embed = embed)


def setup(client):
    client.add_cog(_servidor(client))
