import discord
from discord.ext import commands
import json

with open('config.json', mode='r', encoding='utf8') as config:
    date = json.load(config)

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('>>機器人已啟動<<')

@bot.event
async def on_member_join(member):
<<<<<<< HEAD
    print(f'{member.id}, {member}加入了伺服器!')
    channel = bot.get_channel(date['join_channel'])
    await channel.send(F'<@{member.id}> 加入了伺服器!')

@bot.event
async def on_member_remove(member):
    print(f'{member.id}, {member}離開了伺服器!')
    channel = bot.get_channel(date['leave_channel'])
    await channel.send(F'<@{member.id}> 離開了伺服器!')
=======
    print(f'{member}加入了伺服器!')
    channel = bot.get_channel(輸入要進入的頻道ID)
    await channel.send(F'{member.mention} 加入了伺服器!')

@bot.event
async def on_member_remove(member):
    print(f'{member}離開了伺服器!')
    channel = bot.get_channel(輸入要離開的頻道ID)
    await channel.send(F'{member.mention} 離開了伺服器!')
>>>>>>> 24b43c86419c5e18744956417c127f333fc5197e

@bot.command()
async def ping(ctx):
    await ctx.send(F'<@{ctx.author.id}> 延遲為{round(bot.latency*1000)}ms')
    print(f'{ctx.author.id},{ctx.author}要求顯示延遲!')

<<<<<<< HEAD
bot.run(date['TOKEN'])
=======
bot.run('在此輸入機器人的Token')
>>>>>>> 24b43c86419c5e18744956417c127f333fc5197e
