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
    if 'привет' in message.content:
        msg = 'хей!'.format(message)
        await client.send_message(message.channel, msg)
    elif 'алоха' in message.content:
        msg = 'привет, Настя'.format(message)
        await client.send_message(message.channel, msg)    
    elif 'спасиб' in message.content:
        msg = 'пожалуйста'.format(message)
        await client.send_message(message.channel, msg)
    elif 'пожалуйста' in message.content:
        msg = 'спасибо'.format(message)
        await client.send_message(message.channel, msg)
    elif 'жест' in message.content:
        msg = '( ͡° ͜ʖ ͡°)'.format(message)
        await client.send_message(message.channel, msg)
    elif '<@505377633622556672>' in message.content:
        msg = 'не надо тут линкать меня'.format(message)
        await client.send_message(message.channel, msg)
    elif '<@314363965125820417>' in message.content:
        msg = 'не беспокойте Вита без причины'.format(message)
        await client.send_message(message.channel, msg)

    elif message.content.startswith('вит') and 'роль' in message.content:
        roles = ('танк', 'хил', 'дпс')
        msg = random.choice(roles).format(message)
        await client.send_message(message.channel, msg)
        
    elif message.content.startswith('вит') and 'вероятн' in message.content:
        pos = str(random.randint(0,100))
        msg1 = 'считаю..'
        msg2 = ('вероятность данного события ' + pos + '%').format(message)
        await client.send_message(message.channel, msg1)
        await client.send_message(message.channel, msg1)
        await client.send_message(message.channel, msg2)
        
    elif message.content.startswith('вит') and 'соглас' in message.content:
        msg = 'нет'.format(message)
        await client.send_message(message.channel, msg)        
        
    elif message.content.startswith('вит') and 'наст' in message.content:
        msg = 'предлагаю кикнуть ее'.format(message)
        await client.send_message(message.channel, msg)
    
    elif message.content.startswith('вит') and 'беспокоить' in message.content:
        msg1 = 'EXTERMINATE'.format(message)
        msg2 = 'кхм, извините, вырвалось'.format(message)
        await client.send_message(message.channel, msg1)
        await client.send_message(message.channel, msg1)
        await client.send_message(message.channel, msg2)

    elif message.content.startswith('вит'):
        msg = 'да-да?'.format(message)
        await client.send_message(message.channel, msg)
    
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(os.getenv('TOKEN'))
