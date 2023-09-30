import discord
import random
import not_untitled


# Переменная intents - хранит привилегии бота
intents = discord.Intents.all()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('generate password'):
        if len(message.content) > 17:
            count = int(message.content[17:])
        else:
            count = 10
        await message.channel.send(not_untitled.pas_gen(count))
    elif message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\\U0001f642")
    elif message.content.startswith('battle'):
            player = client.get_user
            await message.channel.send("who wins red or blue")
            if message.content.startswith('red'):
                battle_exodus = random.randint(1 , 2)
                if battle_exodus == 1:
                    await message.channel.send("red team wins your , prediction was sucseful")
                else:
                    await message.channel.send("you lost , enemy team win")
            elif message.content.startswith('blue'):
                battle_exodus = random.randint(1 , 2)
                if battle_exodus == 1:
                    await message.channel.send("blue team wins your , prediction was sucseful")
                else:
                    await message.channel.send("you lost , enemy team win")

client.run("")
