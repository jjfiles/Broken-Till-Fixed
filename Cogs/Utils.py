import os
from discord.ext.commands.errors import MissingPermissions
import dotenv
import requests
from dotenv import load_dotenv, set_key, find_dotenv
from discord.ext import commands

from settings import *

class Utils(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.useOnline = False
        self.PATH = LOCAL
        #self.URL = URL
      
    def isGuildOwner():
       def predicate(ctx):
           return ctx.guild is not None and ctx.guild.owner_id == ctx.author.id
       return commands.check(predicate) 

    @commands.command(
        pass_context=True,
        no_pm=True,
        brief="@Owner Only, Set a local path to store images to",
        help="The owner of the server can select a local folder to store images in"
    ) 
    @commands.check_any(isGuildOwner())
    async def setLocal(self, ctx, arg):
        if os.path.isdir(arg):
            load_dotenv()
            os.environ["LOCAL"] = arg
            dotenv.set_key(dotenv.find_dotenv(), "LOCAL", os.environ["LOCAL"])
            self.PATH = arg
            await ctx.send(f'Path saved!')
        else:
            await ctx.send(f'Invalid path!')
            
    @setLocal.error
    async def setLocalError(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.message.channel.send(f"Sorry {ctx.message.author}, you don't have permission for that command!")
    
    @commands.command(
        pass_context=True,
        no_pm=True,
        brief="@Owner Only, Set a URL to store images to",
        help="The owner of the server can select a URL to store images to"
    ) 
    @commands.check_any(isGuildOwner())
    async def setURL(self):
        pass

    @commands.command(
        pass_context=True,
        no_pm=True,
        brief="Upload an image to the shared folder",
        help="Type the command and attach an image to be uploaded"
    )
    async def upload(self, ctx, *args):
        if self.useOnline:
            return
        else:
            if ctx.message.attachments:
                for each in ctx.message.attachments:
                    if each.url.endswith(("png", "gif", "jpg")):
                        imageData = requests.get(each.url).content
                        sp = each.url.split("/")
                        fname = sp[len(sp) - 2] + "-" + sp[len(sp) - 1]
                        with open(f"{os.path.join(self.PATH, fname)}", "ab") as h:
                            h.write(imageData)
    