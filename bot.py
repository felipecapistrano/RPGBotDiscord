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
        await message.channel.send(controller.dice(message))
        
    if message.content.startswith('$criar'):
        await message.channel.send(controller.character_template())
        def check(m):
            return m.author == message.author and m.channel == message.channel

        msg = await client.wait_for('message', check=check)
        await message.channel.send(controller.create(msg.content, str(message.author.id)))

    if message.content.startswith('$selecionar'):
        await message.channel.send(controller.select(message))
    
    if message.content.startswith('$rolar'):
        await message.channel.send(controller.roll(message))
    
    if message.content.startswith('$ficha'):
        embed = controller.embed(message, discord)
        try:
            await message.channel.send(embed=embed)
        except:
            await message.channel.send(embed)

client.run(info["token"])