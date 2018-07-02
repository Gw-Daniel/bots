import os
import discord
import psutil
from discord.ext import commands
Roxo = 0x690FC3

espaco = '            '
class stats():
    def __init__(self, bot):
        self.bot = bot


    @commands.command(pass_context = True)
    async def stats(self):
       mem = psutil.virtual_memory()
       uso = f"Em uso : {mem.used / 0x40_000_000:.2f}GB"
       total = f"Total : {mem.total / 0x40_000_000:.2f}GB"
       dispo = f"Disponível : {mem.available / 0x40_000_000:.2f}GB"
       mem1 = psutil.disk_usage('/')
       uso1 = f"Em uso : {mem1.used / 0x40_000_000:.2f}GB"
       total1 = f"Total : {mem1.total / 0x40_000_000:.2f}GB"
       dispo1 = f"Disponível : {mem1.free / 0x40_000_000:.2f}GB"
       port = psutil.cpu_percent()
       embed1 = discord.Embed(colour= Roxo)
       embed1.add_field(name = "Memoria", value =""+uso+"\n"+dispo+"\n"+total+"")
       embed1.add_field(name = "Armazenamento", value =""+uso1+"\n"+dispo1+"\n"+total1+"")
       embed1.add_field(name = "Processador", value = "\nNome : IntelCoreI5-4210®  2,93 GHz\n"+"Uso : "+str(port)+"%\nCore : 4/8 ")
       embed1.add_field(name = "Bot", value = "\nServidores : "+str(len(self.bot.servers))+"\n"+"Usuários : "+str(len(set(self.bot.get_all_members())))+"\nCanais : "+str(len(set(self.bot.get_all_channels()))))

       embed1.add_field(name = "Link's", value = "Discord :[**Clique aki**](https://discord.gg/AVNSzAm) {} Website :[**Clique aki**](https://mitsu.glitch.me)".format(espaco))

       await self.bot.say(embed=embed1)


def setup(bot):
    bot.add_cog(stats(bot))
    print('comando foi carregado com sucesso!')