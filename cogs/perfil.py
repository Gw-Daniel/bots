
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

class _perfil():
    def __init__(self, client):
        self.client = client

    
    @commands.command(pass_context = True, aliases=['perfil','userinfo'], Pm=False)
    async def _perfil(self,ctx):
       print("Comando [Perfil/Profile] usado por "+str(ctx.message.author)+" em "+str(ctx.message.server.name))
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
        if len(xtx) == 1:
           usuario_id = ctx.message.author.id
        else:
          usuario_id = xtx[1].replace("<", "").replace("@", "").replace("!", "").replace(">", "")
        servidor_id = ctx.message.server.id
        servidor = self.client.get_server(servidor_id)
        usuario = ctx.message.server.get_member(usuario_id)
        if usuario.avatar_url == "":
           img = ""
        else:
          img = usuario.avatar_url    
        entrou_servidor = str(usuario.joined_at.strftime("20%y/%m/%d | %H:%M:%S"))
        conta_criada = str(usuario.created_at.strftime("20%y/%m/%d | %H:%M:%S"))
        if usuario.display_name == usuario.name:
           apelido = "Não definido"
        else:
          apelido = usuario.display_name  
        informacao = "\n<:simbolo:461714381156253707> Nome : "+str(usuario.name)+"#"+str(usuario.discriminator)+" ("+str(usuario.mention)+")\n<:simbolo:461714381156253707> Apelido : "+str(apelido)+"\n<:simbolo:461714381156253707> Id : "+str(usuario.id)+"\n<:simbolo:461714381156253707> Criada em : "+str(conta_criada)+"\n<:simbolo:461714381156253707> Entrou em : "+str(entrou_servidor)+""
        jogando = str(usuario.game).replace("None","Nenhum jogo detectado") 
        cargos = len([r.name for r in usuario.roles if r.name != "@everyone"])
        status = str(usuario.status).replace("streaming","streamando").replace("online","Disponível").replace("dnd","Não pertube").replace("idle","Ausente").replace("offline","Indisponível")
        servidores_compartilhados = len([y.server.name for y in self.client.get_all_members() if y.id == str(usuario.id)])
        if usuario.id in [y.id for y in servidor.members if y.bot]:
            bot = "Bot"
        else:
          bot = "Normal"         
        informacao_add = "\n<:simbolo:461714381156253707> Jogando : "+str(jogando)+"\n<:simbolo:461714381156253707> Status : "+str(status)+"\n<:simbolo:461714381156253707> Cargos : "+str(cargos)+"\n<:simbolo:461714381156253707> Tipo de conta : "+str(bot)+"\n<:simbolo:461714381156253707> Servidores compartilhados : "+str(servidores_compartilhados)+""
        embed = discord.Embed(colour=0xF08FA2)
        embed.add_field(name="<:info_2:461712111475753000> Informação ", value = informacao, inline=True)
        embed.add_field(name="<:adicional:461658090916413452> Informação Adicional ", value = informacao_add, inline=False)
        embed.set_thumbnail(url=img)
        embed.set_footer(text=self.client.user.name+" © 2018")
        await self.client.say(embed = embed)
       else:
         if len(xtx) == 1:
            usuario_id = ctx.message.author.id
         else:
           usuario_id = xtx[1].replace("<", "").replace("@", "").replace("!", "").replace(">", "")
         servidor_id = ctx.message.server.id
         servidor = self.client.get_server(servidor_id)
         usuario = ctx.message.server.get_member(usuario_id)
         if usuario.avatar_url == "":
            img = ""
         else:
           img = usuario.avatar_url    
         entrou_servidor = str(usuario.joined_at.strftime("20%y/%m/%d | %H:%M:%S"))
         conta_criada = str(usuario.created_at.strftime("20%y/%m/%d | %H:%M:%S"))
         if usuario.display_name == usuario.name:
            apelido = "Undefined"
         else:
           apelido = usuario.display_name  
         informacao = "\n<:simbolo:461714381156253707> Name : "+str(usuario.name)+"#"+str(usuario.discriminator)+" ("+str(usuario.mention)+")\n<:simbolo:461714381156253707> Nickname : "+str(apelido)+"\n<:simbolo:461714381156253707> Id : "+str(usuario.id)+"\n<:simbolo:461714381156253707> Created in : "+str(conta_criada)+"\n<:simbolo:461714381156253707> Entered into : "+str(entrou_servidor)+""
         jogando = str(usuario.game).replace("None","No game detected") 
         cargos = len([r.name for r in usuario.roles if r.name != "@everyone"])
         status = str(usuario.status).replace("streaming","Streaming").replace("online","Online").replace("dnd","DnD").replace("idle","Absent").replace("offline","Offline")
         servidores_compartilhados = len([y.server.name for y in self.client.get_all_members() if y.id == str(usuario.id)])
         if usuario.id in [y.id for y in servidor.members if y.bot]:
            bot = "Bot"
         else:
           bot = "Normal"         
         informacao_add = "\n<:simbolo:461714381156253707> Playing : "+str(jogando)+"\n<:simbolo:461714381156253707> Status : "+str(status)+"\n<:simbolo:461714381156253707> Roles : "+str(cargos)+"\n<:simbolo:461714381156253707> Account Type : "+str(bot)+"\n<:simbolo:461714381156253707> Shared Servers : "+str(servidores_compartilhados)+""
         embed = discord.Embed(colour=0xF08FA2)
         embed.add_field(name="<:info_2:461712111475753000> Information ", value = informacao, inline=True)
         embed.add_field(name="<:adicional:461658090916413452> Additional information ", value = informacao_add, inline=False)
         embed.set_thumbnail(url=img)
         embed.set_footer(text=self.client.user.name+" © 2018")
         await self.client.say(embed = embed)

def setup(client):
    client.add_cog(_perfil(client))
