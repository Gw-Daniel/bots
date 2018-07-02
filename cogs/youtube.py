
import discord
from discord.ext import commands
import os
import random
import time
from urllib.parse import quote
from urllib.request import urlopen
import urllib.request as urlreq
from urllib.request import urlopen
from urllib.request import unquote
from random import choice
import json
import asyncio

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


class _youtube():
    def __init__(self, client):
        self.client = client

    
    @commands.command(pass_context = True, aliases=['youtube','yt'], Pm=False)
    async def _youtube(self,ctx, *,word):
       print("Comando [youtube/yt] usado por "+str(ctx.message.author)+" em "+str(ctx.message.server.name))
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
          ping = '<:5912_aviso:456088917050130432> Você está na blacklist da **yui**, e não poderá usar mais comandos!'
          embed= discord.Embed(description=ping, color=0xF392B1)
          await self.client.send_message(ctx.message.author, embed=embed)
          return
        else:
          ping = "<:5912_aviso:456088917050130432> You're on **yui** blacklist, and you can not use any more commands!"
          embed= discord.Embed(description=ping, color=0xF392B1)
          await self.client.send_message(ctx.message.author, embed=embed)
          return

       if ctx.message.channel.id in lock and ctx.message.author.id not in admin:
        if ctx.message.author.id not in english:
          ping = '<:5912_aviso:456088917050130432> Não foi possivel executar o comando no canal <#'+ctx.message.channel.id+'>, porquê ele foi bloqueado por um administrador.'
          embed= discord.Embed(description=ping, color=0xF392B1)
          await self.client.send_message(ctx.message.author, embed=embed)
          return
        else:
          ping = "<:5912_aviso:456088917050130432> Could not execute command on channel <#"+ctx.message.channel.id+">, because it was blocked by an administrator!"
          embed= discord.Embed(description=ping, color=0xF392B1)
          await self.client.send_message(ctx.message.author, embed=embed)
          return
      
       if ctx.message.server.id in lock and ctx.message.author.id not in admin:
        if ctx.message.author.id not in english:
          ping = '<:5912_aviso:456088917050130432> Não foi possivel executar o comando no servidor '+ctx.message.server.name+', porquê eu fui bloqueada por um administrador!'
          embed= discord.Embed(description=ping, color=0xF392B1)
          await self.client.send_message(ctx.message.author, embed=embed)
          return
        else:
          ping = "<:5912_aviso:456088917050130432> Could not execute command on server "+ctx.message.server.name+", because I was blocked by an administrator!"
          embed= discord.Embed(description=ping, color=0xF392B1)
          await self.client.send_message(ctx.message.author, embed=embed)
          return

       if ctx.message.author.id not in english:
        try:   
           len(word) > 0
           s_result = "";
           sarr = word;
           for i in range(0, len(sarr)):
             if(ord(sarr[i]) < 128):
                   s_result += sarr[i]
           site= "https://www.googleapis.com/youtube/v3/search?q=" + s_result.replace(" ", "%20")  + "&part=snippet&key=AIzaSyAig0iRsiSYnZ-Dc1VAKYF4lkVQkofjO8I"
           response = urlopen(site).read()
           json_response = json.loads(response.decode())
           if(len(json_response["items"]) > 0):
                video = json_response["items"][0]["id"]["videoId"]
                title = json_response["items"][0]["snippet"]["title"]
                uploader = json_response["items"][0]["snippet"]["channelTitle"]
                count = json_response["items"][0]["snippet"]["publishedAt"].replace("T", " | ").replace(".000Z", "").replace("-", "/")
                description = json_response["items"][0]["snippet"]["description"]
                urla = urlreq.urlopen("https://www.googleapis.com/youtube/v3/videos?id=%s&key=AIzaSyAig0iRsiSYnZ-Dc1VAKYF4lkVQkofjO8I&fields=items(id,snippet(channelId,title,categoryId),statistics)&part=snippet,statistics" % (video))
                stat = json.loads(urla.read().decode())['items'][0]['statistics']
                liked = stat["likeCount"]
                disliked = stat["dislikeCount"]
                views = stat["viewCount"]
                comt = stat["commentCount"]
                fav = stat["favoriteCount"]
                await self.client.say("https://www.youtube.com/watch?v="+video)
                await asyncio.sleep(0.5)
                embed=discord.Embed(color=0xff0000)
                embed.add_field(name="Visualizações", value=views, inline=True)
                embed.add_field(name="Gostei", value=liked, inline=True)
                embed.add_field(name="Não Gostei", value=disliked, inline=True)
                embed.add_field(name="Postado às", value=count, inline=True)
                embed.add_field(name="Comentários", value=comt, inline=True)
                embed.add_field(name="Adicionado Fav", value=fav, inline=True)
                embed.add_field(name="Descrição", value= description, inline=True)
                embed.set_footer(text="Yui © 2018")
                await self.client.say(embed=embed)
        except Exception as e:
           await self.client.say("Não foi possível localizar o video, tente novamente.")
       else:
        try:   
           len(word) > 0
           s_result = "";
           sarr = word;
           for i in range(0, len(sarr)):
             if(ord(sarr[i]) < 128):
                   s_result += sarr[i]
           site= "https://www.googleapis.com/youtube/v3/search?q=" + s_result.replace(" ", "%20")  + "&part=snippet&key=AIzaSyAig0iRsiSYnZ-Dc1VAKYF4lkVQkofjO8I"
           response = urlopen(site).read()
           json_response = json.loads(response.decode())
           if(len(json_response["items"]) > 0):
                video = json_response["items"][0]["id"]["videoId"]
                title = json_response["items"][0]["snippet"]["title"]
                uploader = json_response["items"][0]["snippet"]["channelTitle"]
                count = json_response["items"][0]["snippet"]["publishedAt"].replace("T", " | ").replace(".000Z", "").replace("-", "/")
                description = json_response["items"][0]["snippet"]["description"]
                urla = urlreq.urlopen("https://www.googleapis.com/youtube/v3/videos?id=%s&key=AIzaSyAig0iRsiSYnZ-Dc1VAKYF4lkVQkofjO8I&fields=items(id,snippet(channelId,title,categoryId),statistics)&part=snippet,statistics" % (video))
                stat = json.loads(urla.read().decode())['items'][0]['statistics']
                liked = stat["likeCount"]
                disliked = stat["dislikeCount"]
                views = stat["viewCount"]
                comt = stat["commentCount"]
                fav = stat["favoriteCount"]
                await self.client.say("https://www.youtube.com/watch?v="+video)
                await asyncio.sleep(0.5)
                embed=discord.Embed(color=0xff0000)
                embed.add_field(name="Views", value=views, inline=True)
                embed.add_field(name="Like", value=liked, inline=True)
                embed.add_field(name="No Like", value=disliked, inline=True)
                embed.add_field(name="Posted at", value=count, inline=True)
                embed.add_field(name="Comments", value=comt, inline=True)
                embed.add_field(name="Added Fav", value=fav, inline=True)
                embed.add_field(name="Description", value= description, inline=True)
                embed.set_footer(text="Yui © 2018")
                await self.client.say(embed=embed)
        except Exception as e:
           await self.client.say("The video could not be found, please try again.")

def setup(client):
    client.add_cog(_youtube(client))
