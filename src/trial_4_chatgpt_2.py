#!/usr/bin/python3
import discord
from discord.ext import commands, tasks
import datetime

TOKEN = "your_bot_token_here"
PREFIX = "="  # You can change the command prefix to something else
GUILD_ID = 963145041105285120  # Replace with your server's ID
CHANNEL_ID = 994066689924808754  # Replace with the channel ID where you want to send the message
MESSAGE = "Hello, this is your daily message!"

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    daily_message.start()

@tasks.loop(minutes=1)
async def daily_message():
    now = datetime.datetime.now()
    target_time = datetime.time(9, 30)  # Adjust this to your desired time (9:30 AM in this example)

    current_hour, current_minute = now.hour, now.minute
    target_hour, target_minute = target_time.hour, target_time.minute

    if (current_hour, current_minute) == (target_hour, target_minute):
        guild = bot.get_guild(GUILD_ID)
        channel = guild.get_channel(CHANNEL_ID)
        await channel.send(MESSAGE)

@bot.command()
async def hello(ctx):
    await ctx.send("Hello, I am your daily message bot!")

bot.run(TOKEN)
