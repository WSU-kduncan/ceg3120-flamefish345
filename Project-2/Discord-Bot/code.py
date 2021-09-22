import os

import discord
import random
from dotenv import load_dotenv

load_dotenv()
#print(os.getenv('DISCORD_TOKEN'))
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    mst3k_quotes = [
        'There! I think Ive taught you not to rebuff my wiener innuendo.',
        'Uh, genocide has a "C" in it.',
        '[about a man who just had his arm ripped off] And ironically he collapses into an arm chair',
        'Hey, theyre doctors, but they do puppet shows, too!',
    ]

    if message.content == 'moviesign!':
        #response = random.choice(brooklyn_99_quotes)
        response = random.choice(mst3k_quotes)
        await message.channel.send(response)

client.run(TOKEN)
