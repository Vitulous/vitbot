import discord
import random
import os
client = discord.Client()
@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    message.content = message.content.lower()
    # if len(message.attachments) > 0 or 'http' in message.content:
    #    await client.add_reaction(message, '\U0001F44C')
    if message.content.startswith('вит'):
        if 'привет' in message.content:
            helloes = ('хей!', 'привет-привет', 'доброго времени суток', 'привет', 'привет', 'привет')
            msg = random.choice(helloes).format(message)
            await client.send_message(message.channel, msg)
        elif 'пасиб' in message.content:
            msg = 'пожалуйста'.format(message)
            await client.send_message(message.channel, msg)
        elif 'жест' in message.content:
            msg = '( ͡° ͜ʖ ͡°)'.format(message)
            await client.send_message(message.channel, msg)
        elif 'покой' in message.content:
            msg = 'покой - это ложь, есть только страсть'.format(message)
            await client.send_message(message.channel, msg)
        elif 'сарказм' in message.content:
            msg = 'даааа, конеееечно, я полностью точно согласен'.format(message)
            await client.send_message(message.channel, msg)
        elif 'роль' in message.content:
            roles = ('танк', 'хил', 'дпс')
            msg = random.choice(roles).format(message)
            await client.send_message(message.channel, msg)
        elif 'nooo' in message.content:
            await client.send_file(message.channel, './vader.jpg')
        elif 'вероятн' in message.content:
            pos = str(random.randint(0,100))
            msg1 = 'считаю..'
            msg2 = ('вероятность данного события ' + pos + '%').format(message)
            await client.send_message(message.channel, msg1)
            await client.send_message(message.channel, msg1)
            await client.send_message(message.channel, msg2)
        elif 'соглас' in message.content:
            msg = 'нет'.format(message)
            await client.send_message(message.channel, msg)        
        elif 'наст' in message.content:
            msg = 'предлагаю кикнуть ее'.format(message)
            await client.send_message(message.channel, msg)
        elif 'представс' in message.content:
            msg = 'любите меня и жалуйте'.format(message)
            await client.send_message(message.channel, msg)
        elif 'не болей' in message.content:
            msg = 'я стараюсь'.format(message)
            await client.send_message(message.channel, msg)
        elif 'дум' in message.content:
            msg = '¯\_(ツ)_/¯'.format(message)
            await client.send_message(message.channel, msg)  
        elif 'пят' in message.content:
            await client.add_reaction(message, '\U0000270B')
        elif 'здесь' in message.content:
            helloes = ('да-да?', 'я вместо него', 'бип-буп', 'слушаю', 'я тут', 'что?')
            msg = random.choice(helloes).format(message)
            await client.send_message(message.channel, msg)
        
    
    
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(os.getenv('TOKEN'))
