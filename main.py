import discord
from discord.ext import commands
import json
import random
from pynput.keyboard import Key, Controller
keyboard = Controller()
with open('setting.json', 'r', encoding='utf-8') as jfile:
    jdata = json.load(jfile)
bot = commands.Bot(command_prefix='!')
f = open("bot\\JMusicBot-0.2.6.jar" ,'wb')

@bot.event
async def on_ready():
    print("Bot is online!")


@bot.event
async def on_member_join(member):
    channel = bot.get_channel(670963161486065677)
    await channel.send(f'{member}join!')


async def on_member_remove(member):
    channel = bot.get_channel(670963161486065677)
    await channel.send(f'{member}leave!')


@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)}(ms)')


@bot.command()
async def 圖片(ctx):
    random_pic = random.choice(jdata['url_pic'])
    await ctx.send(random_pic)


@bot.command()
async def pic(ctx):
    random_pic = random.choice(jdata['pic'])
    pic = discord.File(random_pic)
    await ctx.send(file=pic)

@bot.command()
async def 指令(ctx):
    for data in jdata['construct']:
        await ctx.send(data.strip())
@bot.command()
async def loading(ctx):
    bot.reload_extension('reloading...');
    await discord.Disconnect();    

bot.run('NjY5MjM5NjAyNzQ1MzExMjM5.Xi17kw.dwcg-BgThk2gSO8cXnuSYLtwvkI') 

