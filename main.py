import os

import dotenv
import discord
from discord.ext import commands, tasks

dotenv.load_dotenv()

bot = commands.Bot("meigen#", intents=discord.Intents.all())


@bot.event
async def setup_hook():
    await bot.load_extension("cogs.embed")
    await bot.load_extension("cogs.admin")


@bot.event
async def on_ready():
    game = discord.Game("作者: 台風の目名言bot")
    await bot.change_presence(activity=game, status=discord.Status.idle)


bot.run(os.getenv("discord"))
