import discord
import json
from RPG.controller import Controller

controller = Controller()

with open('botinfo.json') as info:
    info = json.load(info)

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$d'):
        msg = controller.roll(message)
        await message.channel.send(msg)
        

client.run(info["token"])