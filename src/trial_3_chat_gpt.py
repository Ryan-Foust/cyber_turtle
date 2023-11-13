#!/usr/bin/python3
import discord
import asyncio
import datetime
import os
from kubernetes import client, config

# part below was from chat gpt
def read_kubernetes_secret(secret_name, namespace=None):
    # Load in-cluster configuration
    config.load_incluster_config()

    # Create Kubernetes API client
    v1 = client.CoreV1Api()

    # If the namespace is not provided, use the default namespace of the cluster
    if not namespace:
        namespace = v1.read_namespace().metadata.name

    try:
        # Get the secret
        secret = v1.read_namespaced_secret(name=secret_name, namespace=namespace)
        return secret.data
    except client.rest.ApiException as e:
        if e.status == 404:
            print(f"Secret '{secret_name}' not found in namespace '{namespace}'.")
        else:
            print(f"Error reading secret: {e}")
        return None


# part above is from chat gpt

debug = True
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = 0
CHANNEL_ID = 0

if debug:
    MESSAGE = "@everyone this is a test message"
else:
    MESSAGE = "@everyone :sparkles:Good Morning, Hoodies:sparkles: Today is a new day with new opportunities. What opportunities do you have today?"


intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = discord.Client(intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

    async def send_daily_message():
        await bot.wait_until_ready()
        guild = bot.get_guild(GUILD_ID)
        channel = guild.get_channel(CHANNEL_ID)

        while not bot.is_closed():
            now = datetime.datetime.now()
            target_time = datetime.time(10, 00)  # regular message time

            # Extract the hours and minutes from the current time and target time
            current_hour, current_minute = now.hour, now.minute
            target_hour, target_minute = target_time.hour, target_time.minute

            if (current_hour, current_minute) == (target_hour, target_minute):
                await channel.send(MESSAGE)

            await asyncio.sleep(60)  # Check every 60 seconds

    bot.loop.create_task(send_daily_message())

bot.run(TOKEN)
