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
    if len(message.attachments) > 0 or 'http' in message.content:
        await client.add_reaction(message, '\U0001F44C')
    elif 'привет' in message.content:
        helloes = ('хей!', 'привет-привет', 'доброго времени суток', 'привет', 'привет', 'привет')
        msg = random.choice(helloes).format(message)
        await client.send_message(message.channel, msg)
    elif 'алоха' in message.content:
        msg = 'привет, Настя :р'.format(message)
        await client.send_message(message.channel, msg)    
    elif 'пасиб' in message.content:
        msg = 'пожалуйста'.format(message)
        await client.send_message(message.channel, msg)
    elif 'музыка жизни' in message.content:
        msg = 'Тишина, брат мой.'.format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith('вит') and 'жест' in message.content:
        msg = '( ͡° ͜ʖ ͡°)'.format(message)
        await client.send_message(message.channel, msg)
    elif 'покой' in message.content:
        msg = 'покой - это ложь, есть только страсть'.format(message)
        await client.send_message(message.channel, msg)
    elif '<@505377633622556672>' in message.content:
        msg = 'не надо тут линкать меня'.format(message)
        await client.send_message(message.channel, msg)
    elif '<@314363965125820417>' in message.content:
        msg = 'не беспокойте Вита без причины'.format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith('вит') and 'сарказм' in message.content:
        msg = 'даааа, конеееечно, я полностью точно согласен'.format(message)
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
    elif 'nooo' in message.content:
        await client.sendfile(message.channel, open('vader.jpg'))
    elif message.content.startswith('вит') and 'соглас' in message.content:
        msg = 'нет'.format(message)
        await client.send_message(message.channel, msg)        
        
    elif message.content.startswith('вит') and 'наст' in message.content:
        msg = 'предлагаю кикнуть ее'.format(message)
        await client.send_message(message.channel, msg)
        
    elif message.content.startswith('вит') and 'представс' in message.content:
        msg = 'любите меня и жалуйте'.format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith('вит') and 'не болей' in message.content:
        msg = 'я стараюсь'.format(message)
        await client.send_message(message.channel, msg)
    elif 'доктор' in message.content:
        msg = 'EXTERMINATE'.format(message)
        await client.send_message(message.channel, msg)
        await client.send_message(message.channel, msg)
        await client.send_message(message.channel, msg)
    elif message.content.startswith('вит') and 'дум' in message.content:
        msg = '¯\_(ツ)_/¯'.format(message)
        await client.send_message(message.channel, msg)  
    
    elif message.content.startswith('вит') and 'пят' in message.content:
        await client.add_reaction(message, '\U0000270B')
                
    elif message.content.startswith('вит') and 'здесь' in message.content:
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
