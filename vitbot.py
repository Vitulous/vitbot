import discord
import random
import os
import re
import youtube_dl
import asyncio
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
        elif 'пасиб' in message.content:
            msg = 'пожалуйста'.format(message)
        elif 'жест' in message.content:
            msg = '( ͡° ͜ʖ ͡°)'.format(message)
        elif 'покой' in message.content:
            msg = 'покой - это ложь, есть только страсть'.format(message)
        elif 'сарказм' in message.content:
            msg = 'даааа, конеееечно, я полностью точно согласен'.format(message)
        elif 'роль' in message.content:
            roles = ('танк', 'хил', 'дпс')
            msg = random.choice(roles).format(message)
        elif 'вероятн' in message.content:
            pos = str(random.randint(0,100))
            msg1 = 'считаю..'
            msg = ('вероятность данного события ' + pos + '%').format(message)
            await client.send_message(message.channel, msg1)
            await client.send_message(message.channel, msg1)
        elif 'соглас' in message.content:
            msg = 'нет'.format(message)    
        elif 'наст' in message.content:
            msg = 'предлагаю кикнуть ее'.format(message)
        elif 'представс' in message.content:
            msg = 'любите меня и жалуйте'.format(message)
        elif 'не болей' in message.content:
            msg = 'я стараюсь'.format(message)
        elif 'дум' in message.content:
            msg = '¯\_(ツ)_/¯'.format(message)
        elif 'здесь' in message.content:
            helloes = ('да-да?', 'я вместо него', 'бип-буп', 'слушаю', 'я тут', 'что?')
            msg = random.choice(helloes).format(message)
        elif 'брось' in message.content:
            nums = re.findall('\d+', message.content)
            nums = list(map(int, nums))
            if len(nums) > 2 or nums[0] > 100 or nums[0] == 0 or nums[1] == 0:
                msg = 'такое сами считайте'
            else:
                res = 0
                dice = []
                for x in range(nums[0]):
                    die = random.randint(1, nums[1])
                    dice.append(die)
                    res += die
                msg = 'Итого: ' + str(res).format(message)
                await client.send_message(message.channel, dice)
        await client.send_message(message.channel, msg)
    elif 'nooo' in message.content:
            await client.send_file(message.channel, './vader.jpg')
    elif message.content.startswith('test'):
        author = message.author
        channel = author.voice_channel
        await client.join_voice_channel(channel)
        url = 'https://www.youtube.com/watch?v=OJ2YFHRc4JU'
        server = message.server
        voice_client = client.voice_client_in(server)
        player = await voice_client.create_ytdl_player(url)
        player.start()
        while not player.is_done():
            await asyncio.sleep(1)
        await voice_client.disconnect()
    # elif 'дай пят' in message.content:
    #    await client.add_reaction(message, '\U0000270B')
    
    
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(os.getenv('TOKEN'))
