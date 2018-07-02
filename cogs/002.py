
import discord
from discord.ext import commands
import os
import random
import time
import uptime
import os
import psutil
import datetime
from datetime import datetime
from random import randint
import platform

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
file = open("cogs/txt/english.txt", 'r')
for name in file.readlines():
  if len(name.strip()) > 0 :
    admin.append(name.strip())
file.close()

def up():
    ping = os.popen('python -m uptime')
    result = ping.readlines()
    msLine = result[0].strip()
    return msLine.replace("day","dia").replace("hour","hora").replace("minute","minuto").replace("second","segundo").replace("Uptime:","")

def up2():
    ping = os.popen('python -m uptime')
    result = ping.readlines()
    msLine = result[0].strip()
    return msLine.replace("Uptime:","")

class _002():
    def __init__(self, client):
        self.client = client
        self.start_time = datetime.now()

    
    @commands.command(pass_context = True, aliases=['002'], Pm=False)
    async def _002(self,ctx):
       print("Comando [002] usado por "+str(ctx.message.author)+" em "+str(ctx.message.server.name))
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
         segundos = round((datetime.now() - self.start_time).total_seconds())
         p = psutil.Process(os.getpid())  # p.create_time()
         tempo = p.create_time()
         w = int(tempo) - int(tempo)+segundos
         minute = 60
         hour = minute * 60
         day = hour * 24
         days =  int(w / day)
         hours = int((w % day) / hour)
         minutes = int((w % hour) / minute)
         seconds = int(w % minute)
         string = ""
         if days > 0:
            string += str(days) + " " + (days == 1 and "dia" or "dias" ) + ", "
         if len(string) > 0 or hours > 0:
            string += str(hours) + " " + (hours == 1 and "hora" or "horas" ) + ", "
         if len(string) > 0 or minutes > 0:
            string += str(minutes) + " " + (minutes == 1 and "minuto" or "minutos" ) + ", "
         string += str(seconds) + " " + (seconds == 1 and "segundo" or "segundos" )
         gg = ("%s"% string)
         process = psutil.Process(os.getpid())
         python = (process.memory_info().rss)
         memoria = f"\n<:simbolo:461714381156253707> Ram : {psutil.virtual_memory().used / 0x40_000_000:.2f}GB/{psutil.virtual_memory().total / 0x40_000_000:.2f}GB {psutil.virtual_memory().percent}%"
         memoria1 = f"\n<:simbolo:461714381156253707> Postgre : {psutil.swap_memory().used / 0x40_000_000:.2f}GB/{psutil.swap_memory().total / 0x40_000_000:.2f}GB {psutil.swap_memory().percent}%"
         memoria3 = f"\n<:simbolo:461714381156253707> Processo : {python / 0x400_000:.2f}MB"
         usuario = "Daniel#0205"
         usuario2 = "Vagner#4500"
         embed = discord.Embed(colour= 0xF08FA2)
         aa =memoria+memoria3+memoria1
         bb = "\n<:simbolo:461714381156253707> Python : "+str(platform.python_version())+"\n<:simbolo:461714381156253707> Discord : "+str(discord.__version__)+"\n<:simbolo:461714381156253707> Modulos : 32\n<:simbolo:461714381156253707> Database (Postgre) : 9.6.1"
         cc = "\n<:simbolo:461714381156253707> Servidores : "+str(len(self.client.servers))+"\n<:simbolo:461714381156253707> Usuários : "+str(len(set(self.client.get_all_members())))+"\n<:simbolo:461714381156253707> Emojis : "+str(len(set(self.client.get_all_emojis())))+"\n<:simbolo:461714381156253707> Canais : "+str(len(set(self.client.get_all_channels())))+""
         ee = "\n<:simbolo:461714381156253707> 002 : "+str(gg)+"\n<:simbolo:461714381156253707> Servidor : "+str(up())
         embed.add_field(name="<:zero_two:461659150989000705> 002 ", value = cc, inline=True)
         embed.add_field(name="<:memoria:461959710078140416> Memoria", value = aa, inline=True)
         embed.add_field(name="<:lang:461959258120912917> Python ", value = bb, inline=True)
         embed.add_field(name="<:dev:461958982110543882> Desenvolvedores", value = "\n <:simbolo:461714381156253707>  "+str(usuario2)+"\n<:simbolo:461714381156253707> "+str(usuario)+"\n<:simbolo:461714381156253707> Pablo#6236\n<:simbolo:461714381156253707> LordeFS#6214", inline=True)
         embed.add_field(name="<:atividade:461958574726316063> Atividade", value = ee, inline=True)
         embed.set_footer(text=self.client.user.name+" © 2018")
         embed.set_thumbnail(url="https://78.media.tumblr.com/7881ef85773ef803d04a8f2c66110180/tumblr_p6a6rc8fy91th57iio1_500.png")
         await self.client.say(embed = embed)
       else:
         segundos = round((datetime.now() - self.start_time).total_seconds())
         p = psutil.Process(os.getpid())  # p.create_time()
         tempo = p.create_time()
         w = int(tempo) - int(tempo)+segundos
         minute = 60
         hour = minute * 60
         day = hour * 24
         days =  int(w / day)
         hours = int((w % day) / hour)
         minutes = int((w % hour) / minute)
         seconds = int(w % minute)
         string = ""
         if days > 0:
            string += str(days) + " " + (days == 1 and "day" or "days" ) + ", "
         if len(string) > 0 or hours > 0:
            string += str(hours) + " " + (hours == 1 and "hour" or "hours" ) + ", "
         if len(string) > 0 or minutes > 0:
            string += str(minutes) + " " + (minutes == 1 and "minute" or "minutes" ) + ", "
         string += str(seconds) + " " + (seconds == 1 and "second" or "seconds" )
         gg = ("%s"% string)
         process = psutil.Process(os.getpid())
         python = (process.memory_info().rss)
         memoria = f"\n<:simbolo:461714381156253707> Ram : {psutil.virtual_memory().used / 0x40_000_000:.2f}GB/{psutil.virtual_memory().total / 0x40_000_000:.2f}GB {psutil.virtual_memory().percent}%"
         memoria1 = f"\n<:simbolo:461714381156253707> Postgre : {psutil.swap_memory().used / 0x40_000_000:.2f}GB/{psutil.swap_memory().total / 0x40_000_000:.2f}GB {psutil.swap_memory().percent}%"
         memoria3 = f"\n<:simbolo:461714381156253707> Process : {python / 0x400_000:.2f}MB"
         usuario = "Daniel#0205"
         usuario2 = "Vagner#4500"
         embed = discord.Embed(colour= 0xF08FA2)
         aa =memoria+memoria3+memoria1
         bb = "\n<:simbolo:461714381156253707> Python : "+str(platform.python_version())+"\n<:simbolo:461714381156253707> Discord : "+str(discord.__version__)+"\n<:simbolo:461714381156253707> Modules : 32\n<:simbolo:461714381156253707> Database (Postgre) : 9.6.1"
         cc = "\n<:simbolo:461714381156253707> Servers : "+str(len(self.client.servers))+"\n<:simbolo:461714381156253707> Users : "+str(len(set(self.client.get_all_members())))+"\n<:simbolo:461714381156253707> Emojis : "+str(len(set(self.client.get_all_emojis())))+"\n<:simbolo:461714381156253707> Channels : "+str(len(set(self.client.get_all_channels())))+""
         ee = "\n<:simbolo:461714381156253707> 002 : "+str(gg)+"\n<:simbolo:461714381156253707> Server : "+str(up2())
         embed.add_field(name="<:zero_two:461659150989000705> 002 ", value = cc, inline=True)
         embed.add_field(name="<:memoria:461959710078140416> Memory", value = aa, inline=True)
         embed.add_field(name="<:lang:461959258120912917> Python ", value = bb, inline=True)
         embed.add_field(name="<:dev:461958982110543882> Developers", value = "\n <:simbolo:461714381156253707> "+str(usuario2)+"\n<:simbolo:461714381156253707> "+str(usuario)+"\n<:simbolo:461714381156253707> Pablo#6236\n<:simbolo:461714381156253707> LordeFS#6214", inline=True)
         embed.add_field(name="<:atividade:461958574726316063> Activity", value = ee, inline=True)
         embed.set_footer(text=self.client.user.name+" © 2018")
         embed.set_thumbnail(url="https://78.media.tumblr.com/7881ef85773ef803d04a8f2c66110180/tumblr_p6a6rc8fy91th57iio1_500.png")
         await self.client.say(embed = embed)

def setup(client):
    client.add_cog(_002(client))
