#!/usr/bin/python3
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)

@bot.command(pass_context=True)
async def ping(ctx):
    channel = bot.get_channel(0)
    await channel.send('pong')

@bot.command(pass_context=True)
async def daily_message(ctx):
    channel = bot.get_channel(0)
    await channel.send("@ everyone this is a test, plz ignore")

bot.run("blank")
