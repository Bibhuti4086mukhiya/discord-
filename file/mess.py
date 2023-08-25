import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True  # Enable message content in intents

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')


@bot.event
async def on_message(message):
    if message.author == bot.user:  # Ignore messages from the bot itself
        return

    print(f'Message from {message.author}: {message.content}')
    
    await bot.process_commands(message)

bot.run('')
