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

    if message.content.startswith('$adicionar_dinheiro'):
        await message.channel.send(controller.add(message))
        embed = controller.character_embed(message, discord)
        try:
            await message.channel.send(embed=embed)
        except:
            await message.channel.send(embed)

    if message.content.startswith('$adicionar_item'):
        await message.channel.send(controller.add(message))
        embed = controller.character_embed(message, discord)
        try:
            await message.channel.send(embed=embed)
        except:
            await message.channel.send(embed)

    if message.content.startswith('$adicionar_elemento'):
        await message.channel.send(controller.add(message))
        embed = controller.character_embed(message, discord)
        try:
            await message.channel.send(embed=embed)
        except:
            await message.channel.send(embed)

    if message.content.startswith('$adicionar_maestria'):
        await message.channel.send(controller.add(message))
        embed = controller.character_embed(message, discord)
        try:
            await message.channel.send(embed=embed)
        except:
            await message.channel.send(embed)

    if message.content.startswith('$adicionar_tecnica'):
        await message.channel.send(controller.add(message))
        embed = controller.character_embed(message, discord)
        try:
            await message.channel.send(embed=embed)
        except:
            await message.channel.send(embed)

    if message.content.startswith('$alterar_imagem'):
        await message.channel.send(controller.change_image(message))

    if message.content.startswith('$comandos'):
        await message.channel.send(controller.commands())

    if message.content.startswith('$criar'):
        await message.channel.send(controller.character_template())
        def check(m):
            return m.author == message.author and m.channel == message.channel

        msg = await client.wait_for('message', check=check)
        await message.channel.send(controller.create(msg.content, str(message.author.id)))

    if message.content.startswith('$d'):
        await message.channel.send(controller.dice(message))

    if message.content.startswith('$ficha'):
        embed = controller.character_embed(message, discord)
        try:
            await message.channel.send(embed=embed)
        except:
            await message.channel.send(embed)

    if message.content.startswith('$rolar'):
        await message.channel.send(controller.roll(message))

    if message.content.startswith('$remover_dinheiro'):
        await message.channel.send(controller.subtract_money(message))
        embed = controller.character_embed(message, discord)
        try:
            await message.channel.send(embed=embed)
        except:
            await message.channel.send(embed)

    if message.content.startswith('$remover_item'):
        await message.channel.send(controller.remove_item(message))
        embed = controller.character_embed(message, discord)
        try:
            await message.channel.send(embed=embed)
        except:
            await message.channel.send(embed)

    if message.content.startswith('$selecionar'):
        await message.channel.send(controller.select(message))

    if message.content.startswith('$upar'):
        await message.channel.send(controller.up_stat(message))
        embed = controller.character_embed(message, discord)
        try:
            await message.channel.send(embed=embed)
        except:
            await message.channel.send(embed)

client.run(info["token"])