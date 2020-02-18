import discord
from discord.ext import commands
import json

with open('config.json', mode='r', encoding='utf8') as config:
    date = json.load(config)

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('>>Bot is Online!<<')

@bot.event
async def on_member_join(member):
    print(f'{member.id}, {member}Join the server!')
    channel = bot.get_channel(date['join_channel'])
    await channel.send(F'<@{member.id}> Join the server!')

@bot.event
async def on_member_remove(member):
    print(f'{member.id}, {member} leave the server!')
    channel = bot.get_channel(date['leave_channel'])
    await channel.send(F'<@{member.id}> leve the server!')

@bot.command()
async def ping(ctx):
    await ctx.send(F'<@{ctx.author.id}> 延遲為{round(bot.latency*1000)}ms')
    print(f'{ctx.author.id},{ctx.author}要求顯示延遲!')

bot.run(date['TOKEN'])
