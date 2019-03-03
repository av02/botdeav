import discord
from discord.ext import commands
import random
from random import randint
import asyncio
import time
import os

token = process.env.token # ton token ici

bot = commands.Bot(command_prefix= "+" ,description="de")

@bot.command() #additionner 2 nombres
async def add(ctx, left : int, right : int):
    """aditioner 2 nombres."""
    try:
        await ctx.send(left + right)
    except :
        await ctx.send("oups")

@bot.command() #comande du dé a X faces
async def de(ctx, nombre: int):
    """ ecrire : +de le_nombre max"""
   
    try:
        result = random.randint(1, nombre)
        await ctx.send(f"et le resultat est : {result} ! :papanoel:" )
    except Exception :
        await ctx.send("Une erreur inconnue est survenue.")

@bot.command()#le bot est il cool?
async def coolbot(ctx):
    """le bot est-il cool?"""
    await ctx.send('bien sur que je suis cool.')

@bot.command()#repeter après un delai
async def dire_apres(ctx ,delay , what):
    """repeter après un delai"""
    await asyncio.sleep(delay)
    await ctx.send(what)

bot.run(bot.run(os.environ['token']))
