import discord
from discord.ext import commands

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def fetch_messages(ctx):
    channel_id = 1137344013448532000  # Replace with your channel ID
    channel = bot.get_channel(channel_id)
    
    messages = await channel.history(limit=10).flatten()  # Fetch 10 recent messages
    
    for message in messages:
        print(f'Message from {message.author}: {message.content}')

bot.run('')
