import discord
from discord.ext import commands

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    channel = bot.get_channel(1047208199146721374)  # Replace with your channel ID
    async for message in channel.history(limit=10):  # Fetch 10 recent messages
        print(f'Message from {message.author}: {message.content}')

bot.run('MTE0MDI0MDEwMDAwNjA1MTk1MQ.GK_aYX.w0uBUeVXHUugd31cXrbxrv-EB3822boVXIjarQ')
