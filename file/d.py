import discord
from discord.ext import commands

# Define the intents you need
intents = discord.Intents.all()
intents.typing = True  # You can adjust this based on your needs

# Create a bot instance with intents
bot = commands.Bot(command_prefix='!', intents=intents)

# Event: Bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Command: Extract Messages
@bot.command()
async def extract_messages(ctx, channel: discord.TextChannel):
    messages = await channel.history(limit=None).flatten()
    with open('messages.txt', 'w', encoding='utf-8') as file:
        for message in messages:
            file.write(f"{message.author.name}: {message.content}\n")

# Run the bot
bot.run('')