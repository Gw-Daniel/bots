
import discord
from discord.ext import commands
import os
import random
import time
from PIL import Image
import datetime
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


class _help():
    def __init__(self, client):
        self.client = client
    
    @commands.command(pass_context=True, aliases=['getcolor'])
    async def getcolour(self, ctx, colour_code):
        if not colour_code.startswith("#"):
            colour_code = "#" + colour_code
        image = Image.new("RGB", (200, 200), colour_code)
        image.save("colour_file.png")
        await self.client.send_file(ctx.message.channel, "colour_file.png", content="Cor com código hexadecimal {}:".format(colour_code))
        os.remove("colour_file.png")

    
    @commands.command(pass_context = True, aliases=['help'], Pm=False)
    async def _help(self,ctx):
       print("Comando [Help] usado por "+str(ctx.message.author)+" em "+str(ctx.message.server.name))
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
          embed= discord.Embed(description=ping, color=0xF392B1)
          await self.client.send_message(ctx.message.author, embed=embed)
          return
        else:
          ping = "<:info:461658096628924427> You're on **yui** blacklist, and you can not use any more commands!"
          embed= discord.Embed(description=ping, color=0xF392B1)
          await self.client.send_message(ctx.message.author, embed=embed)
          return

       if ctx.message.channel.id in lock and ctx.message.author.id not in admin:
        if ctx.message.author.id not in english:
          ping = '<:info:461658096628924427> Não foi possivel executar o comando no canal <#'+ctx.message.channel.id+'>, porquê ele foi bloqueado por um administrador.'
          embed= discord.Embed(description=ping, color=0xF392B1)
          await self.client.send_message(ctx.message.author, embed=embed)
          return
        else:
          ping = "<:info:461658096628924427> Could not execute command on channel <#"+ctx.message.channel.id+">, because it was blocked by an administrator!"
          embed= discord.Embed(description=ping, color=0xF392B1)
          await self.client.send_message(ctx.message.author, embed=embed)
          return
      
       if ctx.message.server.id in lock and ctx.message.author.id not in admin:
        if ctx.message.author.id not in english:
          ping = '<:info:461658096628924427> Não foi possivel executar o comando no servidor '+ctx.message.server.name+', porquê eu fui bloqueada por um administrador!'
          embed= discord.Embed(description=ping, color=0xF392B1)
          await self.client.send_message(ctx.message.author, embed=embed)
          return
        else:
          ping = "<:info:461658096628924427> Could not execute command on server "+ctx.message.server.name+", because I was blocked by an administrator!"
          embed= discord.Embed(description=ping, color=0xF392B1)
          await self.client.send_message(ctx.message.author, embed=embed)
          return


       if ctx.message.author.id not in english:
          embed = discord.Embed(timestamp= datetime.datetime.now(), description="Aqui abaixo está listado toda as categoria de modulos com os comandos de cada modulo, para visualizar os comando de cada modulo basta clicar na reação.", color=0x00ff00)
          embed.add_field(name="Modulos", value="<:discord:462861174417915914> : Discord\n<:admin:462862684015034398> : Administração\n<:config:462865085476372480> : Logs\n<:musica:462948418692579328> : Música", inline=True)
          embed.set_thumbnail(url="https://i.imgur.com/azN8QCR.png")
          embed.set_footer(text=self.client.user.name+" © 2018")
          msg = await self.client.send_message(ctx.message.channel, embed=embed)
          await self.client.add_reaction(msg, "❓")
          messagem_2 = msg.id
          usuario_2 = ctx.message.author.id
          @self.client.event
          async def on_reaction_add(reaction, user):
             usuario_1 = user.id
             message_1 = msg.id
             if usuario_1 == "461520049229004830":return
             if reaction.emoji == "❓" and message_1 == messagem_2 and usuario_1 == usuario_2:
                embed1 = discord.Embed(title="sem comandos!!", description="sem comandos!!", color=0x00ff00)
                embed1.set_thumbnail(url="https://i.imgur.com/azN8QCR.png")
                embed1.set_footer(text=self.client.user.name+" © 2018")
                await self.client.edit_message(msg, embed=embed1)   
                await self.client.remove_reaction(msg, "❓", user)
       else:
         timep = time.time()
         emb = discord.Embed(description='Wait..', color=0xF392B1)
         pingm0 = await self.client.say(embed=emb)
         ping = time.time() - timep
         ping = '<:ping:462345020998156323> My ping is %1.2fms' % ping
         pingm1 = discord.Embed(description=str(ping).replace("0.",""), color=0xF392B1)
         await self.client.edit_message(pingm0, embed=pingm1)

def setup(client):
    client.add_cog(_help(client))
