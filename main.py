import os
import time
#import random

import discord
from discord.ext import commands
#from dotenv import load_dotenv
#from webserver import keep_alive
from discord import FFmpegPCMAudio
intents = discord.Intents.default()
#intents.members = True

#async def on_ready(self):
 #       print('Logged on as {0}!'.format(self.user))
#load_dotenv()
TOKEN = 'OTYyMTYyMDk3NjQ1NTUxNjM2.YlDhSA.sIB7eDtBjaLEP46Gd1u6Fq5bjVE'

client = commands.Bot(command_prefix = "-", intents=intents)

@client.command(pass_context = True)
async def join(ctx):
  if(ctx.author.voice):
    await ctx.send("joined vc")
    channel = ctx.author.voice.channel
    voice = await channel.connect()
    source = FFmpegPCMAudio('here.mp3')
    player = voice.play(source)
  else:
    await ctx.send("hey bozo you arent in a vc")
   # print("fail")

@client.command(pass_context = True)
async def silentjoin(ctx):
  if(ctx.author.voice):
    await ctx.send("joined vc")
    channel = ctx.author.voice.channel
    voice = await channel.connect()
    #source = FFmpegPCMAudio('here.mp3')
    #player = voice.play(source)
  else:
    await ctx.send("hey bozo you arent in a vc")

@client.command(pass_context = True)
async def leave(ctx):
    if(ctx.author.voice):
      await ctx.send("bye bozo")
      voice = ctx.guild.voice_client
      source = FFmpegPCMAudio('goner.wav')
      player = voice.play(source)
      time.sleep(2)
      await ctx.voice_client.disconnect()
    else:
      await ctx.send("im not in a vc + ratio")
#response = 'bruh'

@client.command(pass_context = True)
async def yes(ctx):
  if(ctx.author.voice):
    voice = ctx.guild.voice_client
    source = FFmpegPCMAudio('yes.wav')
    player = voice.play(source)
  else:
    await ctx.send("hey bozo you arent in a vc")

@client.command(pass_context = True)
async def sissy(ctx):
  if(ctx.author.voice):
    voice = ctx.guild.voice_client
    source = FFmpegPCMAudio('sissy.wav')
    player = voice.play(source)
  else:
    await ctx.send("hey bozo you arent in a vc")

@client.command(pass_context = True)
async def worth(ctx):
  if(ctx.author.voice):
    voice = ctx.guild.voice_client
    source = FFmpegPCMAudio('worth.wav')
    player = voice.play(source)
  else:
    await ctx.send("hey bozo you arent in a vc")

@client.command(pass_context = True)
async def boo(ctx):
  if(ctx.author.voice):
    voice = ctx.guild.voice_client
    source = FFmpegPCMAudio('boo.wav')
    player = voice.play(source)
  else:
    await ctx.send("hey bozo you arent in a vc")

@client.command(pass_context = True)
async def uncledame(ctx):
  if(ctx.author.voice):
    voice = ctx.guild.voice_client
    source = FFmpegPCMAudio('dame.wav')
    player = voice.play(source)
  else:
    await ctx.send("hey bozo you arent in a vc")

@client.command(pass_context = True)
async def skill(ctx):
  if(ctx.author.voice):
    voice = ctx.guild.voice_client
    source = FFmpegPCMAudio('skill.mp3')
    player = voice.play(source)
  else:
    await ctx.send("hey bozo you arent in a vc")

@client.command(pass_context = True)
async def bttb(ctx):
  if(ctx.author.voice):
    voice = ctx.guild.voice_client
    source = FFmpegPCMAudio('bttb.mp3')
    player = voice.play(source)
  else:
    await ctx.send("hey bozo you arent in a vc")

@client.command(pass_context = True)
async def erec(ctx):
  if(ctx.author.voice):
    voice = ctx.guild.voice_client
    source = FFmpegPCMAudio('erecting.mp3')
    player = voice.play(source)
  else:
    await ctx.send("hey bozo you arent in a vc")

@client.command(pass_context = True)
async def no(ctx):
  if(ctx.author.voice):
    voice = ctx.guild.voice_client
    source = FFmpegPCMAudio('no.wav')
    player = voice.play(source)
  else:
    await ctx.send("hey bozo you arent in a vc")

@client.command(pass_context = True)
async def really(ctx):
  if(ctx.author.voice):
    voice = ctx.guild.voice_client
    source = FFmpegPCMAudio('really.mp3')
    player = voice.play(source)
  else:
    await ctx.send("hey bozo you arent in a vc")

@client.command(pass_context = True)
async def what(ctx):
  if(ctx.author.voice):
    voice = ctx.guild.voice_client
    source = FFmpegPCMAudio('15ai.wav')
    player = voice.play(source)
  else:
    await ctx.send("hey bozo you arent in a vc")

@client.command(pass_context = True)
async def gw(ctx):
  if(ctx.author.voice):
    voice = ctx.guild.voice_client
    source = FFmpegPCMAudio('guesshwat.mp3')
    player = voice.play(source)
  else:
    await ctx.send("hey bozo you arent in a vc")

@client.command(pass_context = True)
async def cheer(ctx):
  if(ctx.author.voice):
    voice = ctx.guild.voice_client
    source = FFmpegPCMAudio('cheer.wav')
    player = voice.play(source)
  else:
    await ctx.send("hey bozo you arent in a vc")

@client.command(pass_context = True)
async def dammit(ctx):
  if(ctx.author.voice):
    voice = ctx.guild.voice_client
    source = FFmpegPCMAudio('dammit.wav')
    player = voice.play(source)
  else:
    await ctx.send("hey bozo you arent in a vc")

@client.command(pass_context = True)
async def goodjob(ctx):
  if(ctx.author.voice):
    voice = ctx.guild.voice_client
    source = FFmpegPCMAudio('goodjob.wav')
    player = voice.play(source)
  else:
    await ctx.send("hey bozo you arent in a vc")

@client.command(pass_context = True)
async def laugh(ctx):
  if(ctx.author.voice):
    voice = ctx.guild.voice_client
    source = FFmpegPCMAudio('laugh.wav')
    player = voice.play(source)
  else:
    await ctx.send("hey bozo you arent in a vc")

@client.command(pass_context = True)
async def helpme(ctx):
  if(ctx.author.voice):
    voice = ctx.guild.voice_client
    source = FFmpegPCMAudio('help.wav')
    player = voice.play(source)
  else:
    await ctx.send("hey bozo you arent in a vc")

@client.command(pass_context = True)
async def sucks(ctx):
  if(ctx.author.voice):
    voice = ctx.guild.voice_client
    source = FFmpegPCMAudio('sucks.wav')
    player = voice.play(source)
  else:
    await ctx.send("hey bozo you arent in a vc")

@client.command(pass_context = True)
async def texas(ctx):
  if(ctx.author.voice):
    voice = ctx.guild.voice_client
    source = FFmpegPCMAudio('texas.wav')
    player = voice.play(source)
  else:
    await ctx.send("hey bozo you arent in a vc")
    
@client.command(pass_context = True)
async def saul(ctx):
  if(ctx.author.voice):
    voice = ctx.guild.voice_client
    source = FFmpegPCMAudio('sault.mp3')
    player = voice.play(source)
  else:
    await ctx.send("hey bozo you arent in a vc")

@client.command(pass_context = True)
async def amongus(ctx):
  if(ctx.author.voice):
    voice = ctx.guild.voice_client
    source = FFmpegPCMAudio('amongus.mp3')
    player = voice.play(source)
  else:
    await ctx.send("hey bozo you arent in a vc")

@client.command(pass_context = True)
async def prejudice(ctx):
  if(ctx.author.voice):
    voice = ctx.guild.voice_client
    source = FFmpegPCMAudio('prejudice.mp3')
    player = voice.play(source)
  else:
    await ctx.send("hey bozo you arent in a vc")
#keep_alive()


client.run(TOKEN)