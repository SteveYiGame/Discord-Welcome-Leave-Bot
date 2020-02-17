import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('>>機器人已啟動<<')

@bot.event
async def on_member_join(member):
    print(f'{member}加入了伺服器!')
    channel = bot.get_channel(輸入要進入的頻道ID)
    await channel.send(F'{member.mention} 加入了伺服器!')

@bot.event
async def on_member_remove(member):
    print(f'{member}離開了伺服器!')
    channel = bot.get_channel(輸入要離開的頻道ID)
    await channel.send(F'{member.mention} 離開了伺服器!')

@bot.command()
async def ping(ctx):
    await ctx.send(F'{round(bot.latency*1000)}ms')

bot.run('在此輸入機器人的Token')
