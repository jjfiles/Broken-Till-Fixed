from asyncio.windows_events import NULL
import os
import time
import datetime
import random
import requests
import asyncio

import discord
from discord.ext.commands import Bot
from discord.ext import commands

from settings import *

class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(
        pass_context=True,
        no_pm=False,
        brief="Choose between two things",
        help="Picks between to items (i.e. !pick x or y)"
    )
    async def pick(self, ctx, *args):
        choices = [""]
        i, j = 0, 0
        while(args):
            if args[i] != "or":
                choices[j] += args[i] + " "
                i += 1 
            else:
                i += 1
                j += 1
                choices.append("")
            if i == len(args):
                break
        
        await ctx.send(random.choice(choices))
    
    @commands.command(
        pass_context=True,
        no_pm=False,
        brief="Roll Dice",
        help="Roll x amount of y sided die (i.e. !roll 2 d6)"
    )
    async def roll(self, ctx, *args):
        if len(args) == 1:
            num = 1
            sides = int(args[0].strip('d'))
        else:
            num = int(args[0])
            sides = int(args[1].strip('d'))
        
        results = [random.randint(1, int(sides)) for x in range(num)]
        await ctx.send(f'You rolled: {", ".join(str(x) for x in results)}')