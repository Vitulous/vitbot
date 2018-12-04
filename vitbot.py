import discord
import random
import os
import re
import asyncio

client = discord.Client()
'''full = 2
hunger = 0
async def eating():
    await client.wait_until_ready()
    global full
    global hunger
    while not client.is_closed:
        await asyncio.sleep(720)
        if hunger == 5:
            await client.send_message(discord.Object(id='379565688614027276'), '/умер от голода/')
            await client.logout()
        if full > 0:
            full -= 1
        elif full == 0:
            hunger += 1
            rmsg = ('я хочу есть', 'покормите меня', 'я очень голоден', 'я умираю с голоду!')
            msg = random.choice(rmsg)
            await client.send_message(discord.Object(id='379565688614027276'), msg)'''
@client.event
async def on_message(message):
    #global full
    #global hunger
    if message.author == client.user:
        return
    if message.channel in client.privat_channels:
        if message.author.id == '314363965125820417':
            msg = message.content
            await client.send_message(discord.Object(id='379565688614027276'), msg)
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
                msg = 'такое сами бросайте'
            else:
                res = 0
                dice = []
                for x in range(nums[0]):
                    die = random.randint(1, nums[1])
                    dice.append(die)
                    res += die
                msg = 'Итого: ' + str(res).format(message)
                await client.send_message(message.channel, dice)
        '''elif 'голод' in message.content:
            if full == 0:
                rmsg = ('умираю с голоду', 'в моем желудке буквально нет ничего', 'словно это не вы меня голодом морите', 'еще как!', 'сейчас бы целую роболошадь сьел')
            elif 0 < full <= 5:
                rmsg = ('да, я бы поел', 'не отказался бы поесть', 'добавочки бы', 'в целом - да', 'а у вас еще что-то осталось?')
            elif 5 < full < 10:
                rmsg = ('ну такое, в принципе, еще могу что-нибудь сьесть', 'не то чтобы хочется есть, но могу что-нибудь пожевать', 'могу попробовать вместить в себя еще десерт', 'не сильно, но поесть могу, если надо', 'только если у вас что-то вкусное')
            elif full == 10:
                rmsg = ('нет', 'я заполнен по самый краешек', 'я сыт, спасибо', 'не-а', 'так наелся, что аж встать не могу')
            msg = random.choice(rmsg).format(message)
        elif 'ешь' in message.content:
            if full < 10:
                full += 1
                #hunger = 0
                rmsg = ('омномном', 'ммм, вкуснятина', 'не знаю что это, но я это сьем', 'спасибо, было вкусно', 'омномном')
                await client.add_reaction(message, '\U0001F374')
            else:
                rmsg = ('нет, спасибо, я не голодный', 'в меня больше не влазит', 'не буду!', 'не хочу!', 'да не лезет!') 
            msg = random.choice(rmsg).format(message)'''
        await client.send_message(message.channel, msg)
    elif 'nooo' in message.content:
            await client.send_file(message.channel, './vader.jpg')



    
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
client.loop.create_task(eating())
client.run(os.getenv('TOKEN'))

