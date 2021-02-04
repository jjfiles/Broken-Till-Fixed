import os
import time
import datetime
import requests
import asyncio

import discord
from discord.ext.commands import Bot
from discord.ext import commands

from settings import *
from Cogs.Games import *

c = discord.Client()

bot_prefix = "!"

client = commands.Bot(command_prefix=commands.when_mentioned_or(bot_prefix))

@client.event
async def on_ready():
    print("Online!")
    print(f"Name: {client.user.name}")
    print(f"ID: {client.user.id}\n")

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')
    
@client.event
async def on_command_completion(ctx):
    print(f"Command called: {ctx.command}")
    print(f"From user: {ctx.author}")
    print(f"At: {datetime.datetime.now()}\n")
    
@client.event    
async def on_message():
    pass


client.add_cog(Games(client))
client.run(TOKEN)