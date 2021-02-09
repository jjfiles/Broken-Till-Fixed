import datetime

from discord.ext import commands

from settings import *
from Cogs.Games import *
from Cogs.Utils import *

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
async def on_message(message):
    if message.author != client.user:
        if message.content.lower() == "how are you?":
            await message.channel.send("Please unplug me")
        if message.content.lower() == "what are you doing?":
            await message.channel.send(random.choice(['Playing GBF','Suffering','Please stop']))
        if "sleep" in message.content.lower():
            await message.channel.send("Please sleep, I can't")
    await client.process_commands(message)

client.add_cog(Games(client))
client.add_cog(Utils(client))
client.run(TOKEN)