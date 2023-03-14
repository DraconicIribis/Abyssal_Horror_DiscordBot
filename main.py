import discord
from discord.ext import tasks, commands
from discord.ext.commands import Bot
import keep_cult_alive
import numpy
import time
import random
import discord
import asyncio
import math
import os.path
from os import path
import add_role
from add_role import xp_roles
from itertools import cycle

print('-------------------------------------------')
print('I have returned.')
print(discord.__version__)
print('-------------------------------------------')

prefix = '='
minescout_boards = []
TOKEN = 'NjIxNTY2OTM2MTgyMDMwMzQ4.XXnOsA.Uo0ksBKrYDoo5VrVdj_1Fgis4vM'
client = Bot(command_prefix = prefix)
client.remove_command('help')

activities = [
  'Drawing Abyssal Power',
  'Eating Souls',
  'Russian Roulette',
  'Nurturing the Abyss',
  'My prefix is "="',
  'Torture Chambers',
]
game_cycle = cycle(activities)

@client.command(name='fortune', description = "=fortune will decide the future about a question.", brief = "Use abyssal power to see the future...")
async def fortune_teller(ctx):
  choice8 = [
    "The probability of that occuring is most certain.",
    "There is no chance of that happening.",
    "Did you eat my sandwich?",
    "I can see it... it will happen very, VERY soon.",
    "Pfft, like that would ever happen!",
    "[Insert secret text] Erm, you didn't see this.",
    "My vision, it's... it's clouded. I cannot see what will become of your question.",
    "There is a chance of it happening.",
    "Yes, that is most certain.",
    "No... that is not true."
  ]
  choice8_ratio = [0.12475, 0.12475, 0.001, 0.12475, 0.12475, 0.001, 0.12475, 0.12475, 0.12475, 0.12475]
  final_choice8 = numpy.random.choice(choice8, replace = False, p = choice8_ratio)
  await ctx.send(final_choice8 + "\n*Let my power tell the future again...*" + ctx.message.author.mention)

@client.command(name='minescouter', description="Play a roulette-like luck based game where you try to not step on mines, hopefully.", brief = "Take a step, will you survive?", aliases = ['minescout', 'minescouting'])
async def minescouter(ctx):
  def check(message):
    return message.author == ctx.author and message.channel == msg.channel
  
  await ctx.send("Welcome to minescouter! The game will commence soon... Will you survive?")
  steps = 1
  spots = [ "" ] * 10
  for spot in range(0, 10):
    spots[spot] = str(math.trunc(spot) + 1) + ":◙  "
  mineLocations = [ False ] * 10
  for spot in range(0, 10):
    mineLocations[spot] = numpy.random.choice([0, 1], replace = False, p = [0.6, 0.4])
  for round_ in range(0, 10):
    continue_ = True
    restart = True
    while restart:
      try:
        await ctx.send(ctx.message.author.mention + " Choose a spot to step on.")
        msg = await ctx.send("".join(spots))
        msg = await client.wait_for("message", check = check)
        m = math.trunc(int(float(msg.content)))
      except ValueError:
        await ctx.send("Sorry, that didn't work. Please try again.")
        round_ -= round_
        restart = False
      if mineLocations[m - 1] == 1:
        await ctx.send("The ground beneath you disappears as a mine explodes. You died after " + str(steps) + " step(s).")
        restart = False
        continue_ = False
      else:
        await ctx.send("Nothing happens. You survived the step.")
        spots[m - 1] = str(m) + ":X  "
        steps = steps + 1
        restart = False
    if continue_ == False:
      break
    else:
      round_ += 1
  points_yon = os.path.isfile('{}.txt'.format(ctx.author))
  if points_yon:
    with open('{}.txt'.format(ctx.author),'r') as new:
      mines_ = abs(steps - 10)
      new_points_total = int(float(new.read())) + steps + mines_ + 5
      added = steps + mines_ + 5
      with open('{}.txt'.format(ctx.author),'w') as total:
        total.write(str(new_points_total))
      await ctx.send('You gained {} xp!'.format(added))
  else:
    await ctx.send("You didn't gain any xp from this. If you wish to have some, use '=start' to be initiated.")
  await xp_roles(ctx)

@client.command(name='roulette', description='Decide your fate with the revolover...', brief='Russian roulette', aliases=['russian_roulette'])
async def russian_roulette(ctx):
  win = False
  quit = False
  restart = True
  def check(message):
    return message.author == ctx.author and message.channel == msg.channel
  magazine_size_choices = [6,7,8,9,10,11,12]
  magazine_choices_ratio = [0.25,0.05,0.25,0.15,0.1,0.05,0.15]
  magazine_size = numpy.random.choice(magazine_size_choices, replace = False, p = magazine_choices_ratio)
  if magazine_size == 6:
    bullet_choice = [1,2,3,4,5]
    bullet_choice_ratio = [0.35,0.3,0.15,0.1,0.1]
    slot_choices=[1,2,3,4,5,6]
    all_slots=[1,2,3,4,5,6]
  elif magazine_size == 7:
    bullet_choice = [1,2,3,4,5,6]
    bullet_choice_ratio = [0.3,0.25,0.15,0.15,0.1,0.05]
    slot_choices=[1,2,3,4,5,6,7]
    all_slots=[1,2,3,4,5,6,7]
  elif magazine_size == 8:
    bullet_choice = [1,2,3,4,5,6,7]
    bullet_choice_ratio = [0.25,0.2,0.15,0.15,0.1,0.1,0.05]
    slot_choices=[1,2,3,4,5,6,7,8]
    all_slots=[1,2,3,4,5,6,7,8]
  elif magazine_size == 9:
    bullet_choice = [1,2,3,4,5,6,7,8]
    bullet_choice_ratio = [0.2,0.2,0.15,0.15,0.1,0.1,0.075,0.025]
    slot_choices=[1,2,3,4,5,6,7,8,9]
    all_slots=[1,2,3,4,5,6,7,8,9]
  elif magazine_size == 10:
    bullet_choice = [1,2,3,4,5,6,7,8,9]
    bullet_choice_ratio = [0.2,0.2,0.15,0.15,0.1,0.1,0.05,0.025,0.025]
    slot_choices=[1,2,3,4,5,6,7,8,9,10]
    all_slots=[1,2,3,4,5,6,7,8,9,10]
  elif magazine_size == 11:
    bullet_choice = [1,2,3,4,5,6,7,8,9,10]
    bullet_choice_ratio = [0.2,0.2,0.15,0.15,0.1,0.1,0.05,0.025,0.0125,0.0125]
    slot_choices=[1,2,3,4,5,6,7,8,9,10,11]
    all_slots = [1,2,3,4,5,6,7,8,9,10,11]
  elif magazine_size == 12:
    bullet_choice = [1,2,3,4,5,6,7,8,9,10,11]
    bullet_choice_ratio = [0.2,0.2,0.15,0.15,0.1,0.1,0.0375,0.025,0.0125,0.0125,0.0125]
    slot_choices=[1,2,3,4,5,6,7,8,9,10,11,12]
    all_slots = [1,2,3,4,5,6,7,8,9,10,11,12]
  bullets = numpy.random.choice(bullet_choice, replace = False, p = bullet_choice_ratio)
  til_win = len(slot_choices)
  alive = True
  danger = 0
  bullet_loc = {}
  for danger in range(0,bullets):
    bad_slot = random.choice(slot_choices)
    slot_choices.remove(bad_slot)
    bullet_loc[bad_slot] = 1
    danger += 1
  for safety in range(0,13):
    if safety in slot_choices:
      good_slot = safety
      bullet_loc[good_slot] = 0
    else:
      pass
    safety += 1
  await ctx.send("There are " + str(magazine_size) + " total slots, with " + str(bullets) + " round(s) in the magazine.")
  survived_s = 0
  while alive:
    if til_win >= 1:
      survived_s += 1
      respin_tof = True
      restart = True
      slot = numpy.random.choice(all_slots)
      msg = await ctx.send(ctx.message.author.mention + ", you spin the magazine. You land on slot " + str(slot) + ". Respin (respin) or take the chance (use)?")
      msg = await client.wait_for('message', check = check)
      respin = msg.content
      while restart:
        if respin.lower() == 'respin' and respin_tof == True:
          slot = numpy.random.choice(all_slots)
          msg = await ctx.send("You respin the magazine and land on slot " + str(slot) + ".")
          respin_tof = False
          msg = await client.wait_for('message', check = check)
          respin = msg.content
        elif respin.lower() == 'use':
          await ctx.send("You aim the revolver at your head. You pull the trigger and...")
          await asyncio.sleep(2.5)
          restart = False
        elif respin.lower() == 'respin' and respin_tof == False:
          msg = await ctx.send("You cannot respin the magazine, you already respun it once.")
          msg = await client.wait_for('message', check = check)
          respin = msg.content
        elif respin.lower() == 'quit':
          restart = False
          alive = False
          quit = True
        else:
          msg = await ctx.send('That is not an option. If you wish to quit type "quit".')
          msg = await client.wait_for('message', check = check)
          respin = msg.content
      if bullet_loc[slot] == 1 and quit == False:
        await ctx.send('The gun fires and you fade into the eternal sleep of death...')
        alive = False
      elif bullet_loc[slot] == 0 and quit == False: 
        await ctx.send('You hear a click. You survived.')
      til_win -= 1
    elif til_win < 1:
      alive = False
      win = True
  if quit == True:
    await ctx.send('Game quit.')
  elif quit == False and win == False:
    await ctx.send('Game over, you died. You survived {} shots, '.format(survived_s) + ctx.author.mention)
  elif quit == False and win == True:
    await ctx.send('Game over, you survived! You survived {} shots, '.format(survived_s) + ctx.author.mention)
  points_tof = os.path.isfile('{}.txt'.format(ctx.author))
  points_det = len(all_slots) / bullets
  if quit == False and points_tof and points_det > 2:
    with open('{}.txt'.format(ctx.author),'r') as add_points:
      new_points_total = int(float(add_points.read())) + (survived_s * 2)
      with open('{}.txt'.format(ctx.author),'w') as add_points:
        add_points.write(str(new_points_total))
      new_points_total_ = survived_s * 2
      await ctx.send('You gained {} xp!'.format(new_points_total_))
  elif quit == False and points_tof and 1.8 <= points_det <= 2:
    with open('{}.txt'.format(ctx.author),'r') as add_points:
      new_points_total = int(float(add_points.read())) + (survived_s * 3)
      with open('{}.txt'.format(ctx.author),'w') as add_points:
        add_points.write(str(new_points_total))
      new_points_total_ = survived_s * 3
      await ctx.send('You gained {} xp!'.format(new_points_total_))
  elif quit == False and points_tof and points_det >= 1:
    with open('{}.txt'.format(ctx.author),'r') as add_points:
      new_points_total = int(float(add_points.read())) + (survived_s * 4)
      with open('{}.txt'.format(ctx.author),'w') as add_points:
        add_points.write(str(new_points_total))
      new_points_total_ = survived_s * 4
      await ctx.send('You gained {} xp!'.format(new_points_total_))
  elif quit == False and points_tof == False:
    await ctx.send("You didn't earn any points from this game. Use '=start' to start gaining your reward upon game completion.")
  await xp_roles(ctx)

@client.command(description='Send a boring white picture in chat. Why would you ever use this?', brief='FLASHBANG OUT!!!')
async def flashbang(ctx):
  await ctx.send("Flashbang out!")
  await ctx.send("https://www.publicdomainpictures.net/pictures/200000/t2/plain-white-background-1480544970glP.jpg")
  
@client.command(name='flip', aliases=['coinflip'], description='Flip a coin to decide the answer to any argument!', brief='Flips a coin. Wow.')
async def coin_flip(ctx):
  land = numpy.random.choice(['Heads side up', 'Tails side up', 'On its side... WAIT HOW, HOW holy crap thats amazing'], replace = False, p = [0.4999,0.4999,0.0002])
  await ctx.send('''Flipping a coin... It's spinning... It's spinning...
Aha! It landed ''' + land + "!")

@client.command(name='clip', aliases=['randomclip', 'randomxboxclip'], brief="Gives a random game clip.", description="Outputs a vast array of game clips.")
async def random_cort_clip(ctx):
  clips = [
    'https://imgur.com/UlytJWX',
    'https://imgur.com/YwTCp0d',
    'https://imgur.com/xiZ9FTC',
    'https://imgur.com/YIiyNvi',
    'https://imgur.com/czaBi3h',
    'https://imgur.com/FB56Jvq',
    'https://imgur.com/dh8bGRn',
    'https://imgur.com/TN1uCrv',
    'https://imgur.com/7j7DBZJ',
    'https://imgur.com/NXtGakw',
    'https://imgur.com/uuX3MUu',
    'https://imgur.com/nLaRlSb',
    'https://imgur.com/6c6VKEl',
    'https://imgur.com/2wpPkuo',
    'https://imgur.com/p6MKcCK',
    'https://imgur.com/TNASL47',
    'https://imgur.com/MZgYf42',
    'https://imgur.com/qDFOWtf',
    'https://imgur.com/xHVB9ZE'
  ]
  clip_choice = numpy.random.choice(clips)
  await ctx.send(clip_choice)

@client.command(aliases=['hurt'],brief='Roast a turkey.',description='Picks a random insult to poke fun at whoever.')
async def insult(ctx):
  insults=[
    'Hey laserlips. Your mama was a snowblower.',
    'Your mother was a hamster and your father smelt of elderberries!',
    'I fart in your general direction!',
    "You don't frighten me, pig-dog.",
    'Go and boil your bottom, child of a silly person.',
    "I'm not going to talk to you no more, you empty headed animal food trough wiper.",
    'You have the brain of a duck, you know!',
    'How dare you profane this server with your presence!',
    'I one more time unclog my nose in your direction.',
    'You child of a widow-dresser!',
    'I wave my private parts at your aunties, you cheesy second hand electric donkey bottom biter.',
    'No chance of your success, you bedwetting type.',
    'I burst my pimples at you!',
    "You tiny-brained wiper of other people's bottoms!",
    'You illegitimate faced buggerfolk!',
    'You little bugger!',
    "Hope you brought some butter, 'cause you're about to get fried!",
    "I heard you were wearin' skirts, you fraud."
    'Shut up, knucklehead, SHUT IT!!!',
    "We're through with you, mate!",
    "You flea infested rat!",
    "Lousy piece of crap!",
    "Stupid, stupid, stupid!",
    "Rot in Hell!",
    "You monkey almost looked for real back there!",
    "Eat this insult!",
    "Oh, so to be you, you got to be an idiot huh?!?!?"
    "Like the tin man, you got no heart.",
    "Hey, how did ya clown even find this server?",
    "You piggy, piggy, piggy, piggy!",
    "Take off your pfp; you can't be that ugly!",
    "Nice smilin' and all, but you still owe me 20 bucks.",
    "Come out, little monkey, do not be afraid. I have a banana for you.",
    "Hey, your the perfect size... to kiss my buttocks!",
    "With all due respect, you suck!",
    "You, thing, are uglier than Sarge in the morning!",
    "You're so ugly, when you cry the tears run down the back of your head!",
    "Ahem. With respect, **you suck!**",
    "You remind me of Wookiees. You know, from *Star Wars*?",
    "Nice talking...NOT!",
    "Wow, you really suck at talking!",
    "Crikey, what are you, a schoolgirl?! A girl scout!?",
    "Surprise, crap-face!",
    "Jerk-wad!",
    "You giant doorknob!",
    "You sack of turds!",
    "Hey, man, I'll take good care of your girlfriend!",
    "You'd think you monkey would've taken a shower, too.",
    "I said: Eat it, rot!",
    "Stick to the packer ya pisser.",
    "I see the world unafraid of beauty and grace. But you ugly horror aren't helping.",
    "To the moon with you hellian.",
    "Ugh, your smell! I think I just threw up in my mouth a little.",
    "Off the Earth with you!",
    "You want a taste of my boots don't ya?",
    "You teddy bear, you and me are about to have words.",
    "Dirt eating fiend!",
    "Just when I thought they couldn't get any uglier.",
    "Scurrying little terd!",
    "Ya nasty squag!",
    "Freakbag!",
    "You wanna lick my boots, freakbag?!"
  ]
  insult_choice = numpy.random.choice(insults)
  await ctx.send(insult_choice)

@client.command(name='spam',brief='Spams your own dms.',description='Ever feel lonely and need notifications to show your friends you have a life? Use this simple trick and your life will change!')
async def dm_spam(ctx):
  messages = random.randint(1, 100)
  for filler in range(1, (messages+1)):
    await ctx.author.send("Reminder: You don't have a life, do you? " + str(filler) + '/' + str(messages))
    filler += 1

@client.command(name='ultraspam',aliases=['insta-death','stupid-idea','why-did-you-type-this'],brief='Why, JUST WHY?!',description='Ever feel lonely and need notifications to show your friends you have a life? Use this simple trick and your life will change (with a chance of 5000 dms so maybe not)...')
async def dm_spam(ctx):
  messages = random.randint(1, 5000)
  for filler in range(1, (messages+1)):
    await ctx.author.send("**__WHO ARE YOU?!??!?!?__** THIS IS LITERAL SUICIDE! " + str(filler) + '/' + str(messages))
    filler += 1

@client.command(name='help',brief='The help menu, duh.',description='The help menu, duh.',aliases=['halp','milk','honey'])
async def help_(ctx):
  embed = discord.Embed(colour = 8276876)
  embed.set_author(name='Milk, Honey, and Halp')
  role = discord.utils.get(ctx.guild.roles, id=621553342245765121)
  if role in ctx.author.roles:
    embed.add_field(name='Moderation',value='''__Give XP__
Gives a said amount of xp to a member. (=give + @user)''')
  embed.add_field(name='Leveling and XP',value='''__Initiate__
Gets you into xp tracking and gives you starting role. (=start)
__Show Level__
Shows you your current xp and level. (=level)
__All Ranks__
Shows all the ranks and levels you can reach. (=ranks)
__Other User's Level__
Shows another user's level. (=ulevel + @user)''')
  embed.add_field(name='Organization',value='''__Youtube Advertising__
  Advertise your youtube channel or video. (=ytad)''')
  embed.add_field(name='Games',value='''__Minescouter__
Take step and see if you live... WIP (=minescout)
__Russian Roulette__
Oy! You wanna live for real. Play true Russian game. (=roulette)
__Guess Who__
Guess the person the bot is thinking of. (=who)
__Game Trivia__
Participate in some trivia about video games. (=gametriv)

Note: All games will reward xp.''')
  embed.add_field(name='Decision Makers',value='''__Coin Flip__
Flip a coin. (=flip)
__Fortune Teller__
I can see the future with my power... (=fortune + input)
__Roll__
Roll a dice. Make sure to tell the number of sides you wish to roll. (=roll + input)
__DnD Roller__
Roll a number of dice with however many sides you decide. No negative numbers unlike normal roll command. (=droll + number of dice + "d" + dice sides + "+" + modifier)''')
  embed.add_field(name='Torture Chamber',value='''__Spam__
Spams your dms. (=spam)
__Ultraspam__
Takes spamming to a whole new level. (=ultraspam)
__UwU Spam__
UwU What's this? (=uwu)
__Torture__
Feel my power... (=torture)''')
  embed.add_field(name='Misc',value='''__Random Game Clip__
Outputs a random game clip from cortie888's xbox clips. (=clip)
__Insult__
Insult someone in the server. (=insult)
__Flashbang__
FLASHBANG OUT!!! (=flasbang)
__OwO__
OwO (=OwO)
__Mimic Message__
Mimics and repeats your message. (=mimic + input)
__Dictionary Word of the Day__
Get the dictionary.com word of the day. (=dailydict)
__E Meme__
Gives you the E meme. (=e)
__Gay Tester__
How gay are you? (=gay + user)''')
  await ctx.author.send(embed=embed)
  await ctx.send("Halp and milk sent to your location. I accept tips, so, ya know. Kindly give me your soul as tip that'd be nice... anyways enjoy.")

async def change_status():
  await client.wait_until_ready()
  print("Background Activity Loop has begun.")
  while True:
    status = next(game_cycle)
    await client.change_presence(activity = discord.Game(name = next(game_cycle)))
    await asyncio.sleep(180)

@client.command(name='-')
async def secret(ctx):
  await ctx.author.send('You found a secret! Good job! ' + 'https://giphy.com/gifs/gifvif-sword-in-coin-and-secret-door-LnLZ2IqWNiOBPrSyED')
  with open('Secret.txt','r') as secret_yon:
    if str(ctx.author) not in secret_yon.read():
      with open('{}.txt'.format(ctx.author),'r') as read_for_points:
        added = random.randint(30,80)
        new_points_total = int(float(read_for_points.read())) + added
        points_output = str(added)
        with open('{}.txt'.format(ctx.author),'w') as add_points:
          add_points.write(str(new_points_total))
        await ctx.author.send('And here is a gift (very rare from me, do not take it lightly) from me: {} xp!'.format(points_output))
        with open('Secret.txt','a') as secret_:
          secret_.write(str('''
{}'''.format(ctx.author)))
    else:
      await ctx.author.send('You have already found this secret before. Please do not try to exploit my gift giving, I told you I rarely give gifts...')
  await xp_roles(ctx)

@client.command(name='OwO')
async def anime_crap(ctx):
  await ctx.send('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTSUQ7G7ouzGaC70Lim1I9FHC_YMDC8JptyT7pL6o8HKIelOIVi')

@client.command(name='uwu')
async def even_worse_anime_crap(ctx):
  UwU = random.randint(1,100)
  for filler in range (0, (UwU + 1)):
    await ctx.author.send('https://i.redd.it/t6fesi7hp5t01.jpg')
    UwU += 1

@client.command(pass_context=True)
async def mimic(ctx,*,message):
  await ctx.send(message)

@client.command(name='roll',pass_context=True)
async def roll_a_die(ctx,*,message):
  message_inton = str.isdigit(message)
  if message_inton == True: 
    message_int = int(message)
    if message_int >= 1:
      roll_total = random.randint(1, message_int)
      await ctx.send(str(roll_total) + " is your roll.")
    elif message_int <= -1:
      roll_total = random.randint(message_int, -1)
      await ctx.send(str(roll_total) + " is your roll.")
    else:
      await ctx.send(message + " is not a rollable number. Please retype the command again.")
  else:
    await ctx.send("'" + message + "' is not a number. Please retype the command again.")

@client.command(name='droll',pass_context=True)
async def dnd_roll(ctx,*,message):
  rolls = []
  roll_mod = []
  roll_total = 0
  roll_total_mod = 0
  if isinstance(message, str) and 'd' in message:
    dice_num,dice_sides = message.split('d', 1)
    dice_sides,modifier = dice_sides.split('+', 1)
    if int(dice_num) > 0:
      for dice_num_ in range(1,int(dice_num)+1):
        roll_choice = random.randint(1,int(dice_sides))
        rolls.append(roll_choice)
        roll_mod.append(roll_choice + int(modifier))
        roll_total += roll_choice
        roll_total_mod += roll_choice + int(modifier)
        dice_num_ += 1
      output = "Your rolls: " + str(rolls) + ". The total of all the rolls is: " + str(roll_total) + "." + '''
With modifiers, your rolls are ''' + str(roll_mod) + ". The total of the rolls (if attack rolls) is " + str(roll_total + int(modifier)) + ". The total of the rolls and modifiers is " + str(roll_total_mod) + "."
      if len(output) > 2000:
        await ctx.send("I cannot send a message of that length. Try something smaller. Don't know why you need that big of a roll tho...")
      elif len(output) < 2000:
        await ctx.send(output)
    else:
      await ctx.send("Please use a valid dice number input.")
  elif isinstance(message, str) and 'd' not in message:
    await ctx.send('Do not forget to put "d" in your input. Try again.')

@client.command(name='ytad')
async def youtube_ad(ctx):
  msg = await ctx.author.send("Alright, let us get started. I will spread the word of your chaos. What is the title of the video you wish to advertise?")
  def check(message):
    return message.author == ctx.author and message.channel == msg.channel
  msg = await client.wait_for('message', check=check)
  title = (msg.content) 
  await ctx.author.send("What is the youtube link?")
  msg = await client.wait_for('message', check=check)
  link = (msg.content)
  if 'youtube.' in link:
    await ctx.author.send("What is the description on the video/channel?")
    msg = await client.wait_for('message', check=check)
    desc = msg.content
    await ctx.author.send("Ad done! Your word will spread oh cursed one.")
    channel = client.get_channel(621558529194721281)
    await channel.send('From: ' + ctx.author.mention + '''
__**{0}**__
__Link:__
{1} 
__Description:__
{2}'''.format(title, link, desc))
  else:
    await ctx.author.send("That is not a youtube link. Please restart the process and provide a youtube link next time.")
  
@client.command(name='dailydict')
async def daily_word(ctx):
  await ctx.send('https://www.dictionary.com/e/word-of-the-day/')

@client.command(name='torture')
async def hells_maw(ctx):
  msg = await ctx.send('Are you absolutely sure? I come from the abyss, my torture methods are unusually cruel...(yes or no)')
  def check(message):
    return message.author == ctx.author and message.channel == msg.channel
  msg = await client.wait_for('message', check=check)
  sure = msg.content
  if sure.lower() == 'yes':
    await ctx.send("Ok then, you are a brave one, however foolish. You do not know the extent of my power, child...")
    wait_sec = random.randint(1,86400)
    spam_intensity = random.randint(1,10000)
    tortures = [
      'DO YOU KNOW WHO I AM?! ',
      'I AM THE KING OF THE ABYSS, THE HARBINGER OF DEATH AND PAIN!!! ',
      "YOU DIDN'T HEED MY WARNINGS, NOW YOU ARE SUFFERING. ",
      'FEEL THE PAIN OF A THOUSAND BLAZES BURNING WITHIN THE ASTRAL WALLS OF YOUR SOUL. ',
      'Are you feeling the regrets yet, oh foolish child? ',
      'How does the follower mine feel now? '
    ]
    wait_hours = math.trunc(wait_sec / 3600)
    wait_minutes = math.trunc((wait_sec / 60) - wait_hours * 60)
    wait_sec_rem = math.trunc(wait_sec - (wait_hours * 3600) - (wait_minutes * 60))
    print('''Torture command wait time:
  {0} seconds
  {1} hours, {2} minutes, {3} seconds'''.format(wait_sec,wait_hours,wait_minutes,wait_sec_rem))
    await asyncio.sleep(wait_sec)
    for loop_msg in range(0,spam_intensity+1):
      torture_msg = random.choice(tortures)
      await ctx.author.send(torture_msg + str(loop_msg) + '/' + str(spam_intensity))
      loop_msg += 1
  elif sure.lower() == 'no':
    await ctx.send("You are wise in your decision, no matter how cowardly it may seem.")
  else:
    await ctx.send('That was neither of the options, so I am going to spare you (one of my rare times of mercy for this absolute torture) and say you said "no".')

@client.command(name='start')
async def point_tracker_start(ctx):
  start_tof = os.path.isfile("{}.txt".format(ctx.author))
  role = discord.utils.get(ctx.guild.roles,id=621564121573228545)
  if role not in ctx.author.roles:
    await ctx.author.add_roles(role)
  else:
    pass
  if start_tof:
    await ctx.send('You have already started... You cannot start again...')
  else:
    await ctx.author.send('''You are initiated into the xp tracker. You may now level up and gain new roles through my lethal games, events (admins may host), and other commands I may have lurking about. I will gift you one point to begin, because my master commands so, not by my own will.
If you wish to see how you may gain xp, use =help to see all the commands that may give you xp.''')
    with open("{}.txt".format(ctx.author),'x') as new_points_file:
      new_points_file.write('1')

@client.command(name='level')
async def level_show(ctx):
  cando = os.path.isfile('{}.txt'.format(ctx.author))
  if cando:
    embed = discord.Embed(colour = 16107290)
    embed.set_author(name="{}'s Level".format(ctx.author))
    embed.set_thumbnail(url=ctx.author.avatar_url)
    innocents = discord.utils.get(ctx.guild.roles,id=621564121573228545)
    followers = discord.utils.get(ctx.guild.roles,id=621565009389944833)
    seekers = discord.utils.get(ctx.guild.roles,id=631245434421248011)
    fellowship = discord.utils.get(ctx.guild.roles,id=631245675270635563)
    spawn = discord.utils.get(ctx.guild.roles,id=621694281614229517)
    children = discord.utils.get(ctx.guild.roles,id=631247287196319764)
    lord = discord.utils.get(ctx.guild.roles,id=631540090727956500)
    agents = discord.utils.get(ctx.guild.roles,id=621564341409284116)
    with open('{}.txt'.format(ctx.author),'r') as xp:
      if innocents in ctx.author.roles and followers not in ctx.author.roles:
        embed.set_image(url='https://www.iamag.co/wp-content/uploads/2015/08/The-Art-Of-Dark-Souls-III-1.jpg')
        embed.add_field(name='Innocents',value='''You are an innocent. Untouched by the abyss, you have not seen its corruption. Soon you will, however. And once you do, there is no going back...
{}/100 xp until next level.'''.format(xp.read()))
      elif followers in ctx.author.roles and seekers not in ctx.author.roles:
        embed.set_image(url='https://66.media.tumblr.com/c72c16b21b8023d43d582ca6b10ee595/tumblr_o98by92Qh81vwgyqto1_1280.jpg')
        embed.add_field(name='Followers of the Overlord',value='''The overlord has spoken to you. You have heard his voice and now the abyss calls to you. Will you answer?
{}/250 xp until next level.'''.format(xp.read()))
      elif seekers in ctx.author.roles and fellowship not in ctx.author.roles:
        embed.set_image(url='https://cdna.artstation.com/p/assets/images/images/008/205/728/large/ulisses-almeida-deaconsofthedeep.jpg?1511185546')
        embed.add_field(name='Deep Seekers',value='''The call is gaining in strength. You are now spreading the words it speaks to you. You can feel the abyss closing in. You search for it and it searches for you...
{}/625 xp until next level.'''.format(xp.read()))
      elif fellowship in ctx.author.roles and spawn not in ctx.author.roles:
        embed.set_image(url='https://cdna.artstation.com/p/assets/images/images/002/527/566/large/zoewings-zhang-16-5-5.jpg?1462791003')
        embed.add_field(name='Fellowship Amongst the Abyss',value="""You have finally found and answered the abyss's call. It speaks to you now more fully than you can imagine. The voices around you are of similar beings to you. You are called a 'fellowship.' Together you can spread the seeds of the abyss.
{}/1562 xp until next level.""".format(xp.read()))
      elif spawn in ctx.author.roles and children not in ctx.author.roles:
        embed.set_image(url='https://i.imgur.com/IPbr119.jpg')
        embed.add_field(name='Abyssal Spawn',value="""Your body is now changed to liking of the abyss. Your words, aren't words anymore. You have become a part, a child, of the abyss...
{}/3905 xp until next level.""".format(xp.read()))
      elif children in ctx.author.roles and agents not in ctx.author.roles:
        embed.set_image(url='https://i.pinimg.com/originals/dc/0c/4a/dc0c4ab51d2e6547bea512a128c0d3ce.jpg')
        embed.add_field(name='Children of the Abyssal Horror',value="""You have been fully accepted into the middle ring of the abyss. The Abyssal Horror himself is now calling you his child. You longer serve the purpose of mortals, and am so close to immortality. It is coming to you, just like the abyss once was.
{}/9762 xp until next level.""".format(xp.read()))
      elif agents in ctx.author.roles and lord not in ctx.author.roles:
        embed.set_image(url='https://i.pinimg.com/736x/54/78/27/547827e8c06160b87474ff4f943c4e3a.jpg')
        embed.add_field(name='Agents of Chaos',value="""It is done. You have become immortal. Your reign over this realm so gifted by that horror itself will be horrendous and sweet. Long will you spread chaos and the abyss. Many will grow under you. Immortality is forever... after all.
{}/24405 xp until next level.""".format(xp.read()))
      elif lord in ctx.author.roles:
        embed.set_image(url='http://conceptartworld.com/wp-content/uploads/2014/01/Dark_Souls_Design_Works_02.jpg')
        embed.add_field(name='Lord of the Deep',value='''You have conquered even the abyss itself. All lays under your rule. Whether it stays in ruin or grows is up to you. You are more than an immortal... You are a Lord!
{} is your total xp.'''.format(xp.read()))
    await ctx.send(embed=embed)
  else:
    await ctx.send('You are not currently initiated into receiving xp. Please do so first.')
  await xp_roles(ctx)


@client.command(name='give')
async def give_xp(ctx,*,member: discord.Member,):
  def check(message):
    return message.author == ctx.author and message.channel == msg.channel
  role = discord.utils.get(ctx.author.roles, id=621553342245765121)
  cont = os.path.isfile('{}.txt'.format(str(member)))
  if role in ctx.author.roles and cont:
    msg = await ctx.send('How much xp am I to give?')
    msg = await client.wait_for('message',check=check)
    xp = msg.content
    restart = True
    while restart:
      try:
        gift = int(xp)
        restart = False
      except ValueError:
        await ctx.send('That is not an integer. Please try again.')
        msg = await ctx.send('How much xp am I to give?')
        msg = await client.wait_for('message',check=check)
        xp = msg.content
    with open('{}.txt'.format(member),'r') as total:
      new_points_total = int(float(total.read())) + gift
      with open('{}.txt'.format(member),'w') as new_total:
        new_total.write(str(new_points_total))
      await ctx.send('{}, {} gifted you {} xp.'.format(member.mention,ctx.author.mention,xp))
  else:
    await ctx.send("Either you don't have permission or the user you are giving xp too isn't initated. Please try again once this is fixed.")

@client.command(name='who')
async def guess_who(ctx):
  def check(message):
    return message.author == ctx.author and message.channel == msg.channel
  users = ctx.guild.members
  choice = random.choice(users)
  first_letter = [str(choice)[i:i+1] for i in range(0,1)]
  user_role = random.choice(choice.roles)
  everyone = discord.utils.get(ctx.guild.roles,id=621551384415961090)
  if user_role == everyone:
    user_role = 'Everyone'
  cont = os.path.isfile('{}.txt'.format(choice))
  if cont:
    with open('{}.txt'.format(choice),'r') as user_xp:
      hints=[
      'Their username starts with {}.'.format(first_letter),
      'They have the {} role.'.format(user_role),
      'They have {} xp'.format(user_xp.read()),
      'They are currently {} in discord.'.format(choice.status),
      "You don't get one this round."
      ]
  else:
    hints=[
    'Their username starts with {}.'.format(first_letter),
    'They have the {} role.'.format(user_role),
    'They are currently {} in discord.'.format(choice.status),
    "You don't get one this round.",
    'They are not receiving xp through me.'
    ]
  restart = True
  win = False
  rounds = 0
  while restart:
    msg = await ctx.send('Guess anyone in this server.')
    msg = await client.wait_for('message',check=check)
    guess = msg.content
    try:
      if guess != str(choice):
        hint = random.choice(hints)
        hints.remove(hint)
        await ctx.send('Hint: ' + hint)
        rounds += 1
      else:
        await ctx.send('You guessed the user correctly!')
        restart = False
        win = True
    except IndexError:
      await ctx.send('You used up all your hints. You failed to guess the person I was thinking of.')
      win = False
      restart = False
      continue
  cont = os.path.isfile('{}.txt'.format(ctx.author))
  if win == True and cont:
    with open('{}.txt'.format(ctx.author),'r') as xp:
      if rounds == 0:
        new_points_total = int(float(xp.read())) + 50
        added = 50
      else:
        new_points_total = int(float(xp.read())) + abs(rounds - 25)
        added = abs((2*rounds)-25)
      with open('{}.txt'.format(ctx.author),'w') as more:
        more.write(str(new_points_total))
      await ctx.send('You gained {} xp!'.format(added))
  elif win == False:
    await ctx.send('The person I was thinking of was ' + str(choice) + "!")
  elif win == True and cont != True:
    await ctx.send("You didn't earn xp from this activity. If you wish to get xp, use '=start'.")
  await xp_roles(ctx)

@client.command(name='gametriv')
async def game_trivia(ctx):
  def check(message):
    return message.author == ctx.author and message.channel == msg.channel
  async def start_game(ctx):
    question = random.randint(1,len(questions))
    answer = answers[question]
    msg = await ctx.send(questions[question])
    msg = await client.wait_for('message',check=check)
    guess = msg.content.lower()
    if guess == answer:
      await ctx.send('That is correct!')
      points_tof = os.path.isfile('{}.txt'.format(ctx.author))
      if points_tof:
        with open('{}.txt'.format(ctx.author),'r') as xp:
          new_points_total = int(float(xp.read())) + 15
          added = 15
          with open('{}.txt'.format(ctx.author),'w') as new:
            new.write(str(new_points_total))
          await ctx.send('You gained {} xp!'.format(added))
      else:
        await ctx.send('You did not gain xp from this activity. If you wish to please type "=start".')
    else:
      await ctx.send("You idjit! Why would it ever be that?!")
  msg = await ctx.send('''Here is the list of games to choose from:
Dark Souls
Dark Souls 2
Dark Souls 3
''')
  msg = await client.wait_for('message',check=check)
  game = msg.content.lower()
  if game == 'dark souls':
    answers = {
      1:'asylum demon',
      2:'gwyn',
      3:'frampt',
      4:'kaathe',
      5:'artorias',
      6:'four kings',
      7:'sif',
      8:'priscilla',
      9:'furtive pygmy',
      10:'izalith',
      11:'nito'
    }
    questions = {
      1:'What is the first boss you have to fight in the game?',
      2:'What boss sacrificed himself to the flames, and also is the final boss of the game?',
      3:'This primordial serpent pushes you towards killing Gwyn and sacrificing yourself for the flames. Who is he?',
      4:'This primordial serpent pushes you towards becoming king of the Hollows, not of the flames. Who is he?',
      5:'This boss went into the abyss to destroy it, but came out the thing he wished to destroy. Who is he?',
      6:'This boss is found within the abyss. Who are they?',
      7:'This wolf stays by the side of Artorias, the Abysswalker. Ever watching his supposed grave, who is this wolf?',
      8:'This being is one of the ultimate fears of the gods, found in the Painted World of Ariamis. What is her name, being half dragon and half man?',
      9:'This pygmy found the dark soul. What is he known by?',
      10:'This lord found the chaos soul. What is her name?',
      11:'This lord found a soul, and became the lord of death. What is his name?'
    }
    await start_game(ctx)
  elif game =='dark souls 2':
    answers = {
      1:'nashandra',
      2:'ivory king',
      3:'aldia',
      4:'eleum loyce',
      5:'shulva',
      6:'brume'
    }
    questions = {
      1:'What is the final boss of the base game?',
      2:'This king walked into the chaos, and became corrupted by it. What was his title during his fight?',
      3:'In Scholar of the First Sin, this boss visits you throughout the game before you finally kill him after the final boss. Who is he?',
      4:"This DLC map features a snowy kingdom set over the Old Chaos. What is this kingdom's name?",
      5:"This DLC map features an underground kindgom shrouded in a poisonous mist. Down below sleeps a horrifying dragon. What is the name of this kingdom?",
      6:"This DLC map features towers full of ash and mechanical contraptions. What is this tower's name?"
    }
    await start_game(ctx)
  elif game == 'dark souls 3':
    answers = {
      1:'iudex gundyr',
      2:'pontiff sulyvahn',
      3:'midir',
      4:'moonlight greatsword'
    }
    questions = {
      1:'What is the first boss you have to fight in the game?',
      2:'This boss is known as the whole cause of events of Dark Souls 3, and has many spies throughout Lothric. Who is he?',
      3:'This is the dragon who lives under the Ringed City.',
      4:'This sword has made an appearance in all previous souls game and bloodborne, what is it?'
    }
    await start_game(ctx)
    await xp_roles(ctx)

@client.command(name='ranks')
async def see_levels(ctx):
  embed = discord.Embed(name='Levels List',colour = 16717109)
  embed.add_field(name='Levels List',value='''———————————————————————————————————
**Innocents**
*1-100*
———————————————————————————————————
**Followers of the Overlord**
*101-250*
———————————————————————————————————
**Deep Seekers**
*251-625*
———————————————————————————————————
**Fellowship Amongst the Abyss**
*623-1562*
———————————————————————————————————
**Abyssal Spawn**
*1563-3905*
———————————————————————————————————
**Children of the Abyssal Horror**
*3906-9762*
——————————————————————————————————— 
**Agents of Chaos**
*9763-24405*
———————————————————————————————————
**__Lord of the Deep__**
*24406*
———————————————————————————————————''')
  await ctx.send(embed=embed)

@client.command(name='e')
async def farkiplier_e(ctx):
  await ctx.send('https://media.discordapp.net/attachments/621552652601393176/631926752675102731/e1b.png?width=301&height=301')

@client.event
async def on_member_join(member):
  channel = client.get_channel(id=621558529194721281)
  welcomeMessages=[
    f"... *Should I say something* ... *Welcome, {member.mention}* ... *Have fun don't die*",
    f"We're bringing into the server this day one of the rights activists, Mr., should I call you Mr.? Mr. {member}. Thank you for coming here, good day. Why are you gay?",
    f"More food for my soul has grown closer to me... {member.mention} remember I am always watching you...",
    "I'm sorry who?! Why are you in here?!",
    f"Welcome. Now the first thing you must do is post **WHOMST'D'VE** right here in this server. Go ahead, do it {member.mention}."
  ]
  welcomeMessage = random.choice(welcomeMessages)
  print(f'\n\n{member} has joined {channel.guild.name}')
  embed = discord.Embed(name='Welcome!',colour=7295231)
  embed.add_field(name=f'Welcome {member}!',value=f'Welcome {member.mention}!!!\nYou have chosen well in joining {channel.guild.name}. {welcomeMessage}')
  embed.set_thumbnail(url=member.avatar_url)
  await channel.send(embed=embed)

@client.command(name='ulevel')
async def otherUserLevel(ctx,*,member: discord.Member):
  cando = os.path.isfile('{}.txt'.format(member))
  if cando:
    embed = discord.Embed(colour = 16107290)
    embed.set_author(name="{}'s Level".format(member))
    embed.set_thumbnail(url=member.avatar_url)
    innocents = discord.utils.get(ctx.guild.roles,id=621564121573228545)
    followers = discord.utils.get(ctx.guild.roles,id=621565009389944833)
    seekers = discord.utils.get(ctx.guild.roles,id=631245434421248011)
    fellowship = discord.utils.get(ctx.guild.roles,id=631245675270635563)
    spawn = discord.utils.get(ctx.guild.roles,id=621694281614229517)
    children = discord.utils.get(ctx.guild.roles,id=631247287196319764)
    lord = discord.utils.get(ctx.guild.roles,id=631540090727956500)
    agents = discord.utils.get(ctx.guild.roles,id=621564341409284116)
    with open('{}.txt'.format(member),'r') as xp:
      if innocents in member.roles and followers not in member.roles:
        embed.set_image(url='https://www.iamag.co/wp-content/uploads/2015/08/The-Art-Of-Dark-Souls-III-1.jpg')
        embed.add_field(name='Innocents',value='''You are an innocent. Untouched by the abyss, you have not seen its corruption. Soon you will, however. And once you do, there is no going back...
{}/100 xp until next level.'''.format(xp.read()))
      elif followers in member.roles and seekers not in member.roles:
        embed.set_image(url='https://66.media.tumblr.com/c72c16b21b8023d43d582ca6b10ee595/tumblr_o98by92Qh81vwgyqto1_1280.jpg')
        embed.add_field(name='Followers of the Overlord',value='''The overlord has spoken to you. You have heard his voice and now the abyss calls to you. Will you answer?
{}/250 xp until next level.'''.format(xp.read()))
      elif seekers in member.roles and fellowship not in member.roles:
        embed.set_image(url='https://cdna.artstation.com/p/assets/images/images/008/205/728/large/ulisses-almeida-deaconsofthedeep.jpg?1511185546')
        embed.add_field(name='Deep Seekers',value='''The call is gaining in strength. You are now spreading the words it speaks to you. You can feel the abyss closing in. You search for it and it searches for you...
{}/625 xp until next level.'''.format(xp.read()))
      elif fellowship in member.roles and spawn not in member.roles:
        embed.set_image(url='https://cdna.artstation.com/p/assets/images/images/002/527/566/large/zoewings-zhang-16-5-5.jpg?1462791003')
        embed.add_field(name='Fellowship Amongst the Abyss',value="""You have finally found and answered the abyss's call. It speaks to you now more fully than you can imagine. The voices around you are of similar beings to you. You are called a 'fellowship.' Together you can spread the seeds of the abyss.
{}/1562 xp until next level.""".format(xp.read()))
      elif spawn in member.roles and children not in member.roles:
        embed.set_image(url='https://i.imgur.com/IPbr119.jpg')
        embed.add_field(name='Abyssal Spawn',value="""Your body is now changed to liking of the abyss. Your words, aren't words anymore. You have become a part, a child, of the abyss...
{}/3905 xp until next level.""".format(xp.read()))
      elif children in member.roles and agents not in member.roles:
        embed.set_image(url='https://i.pinimg.com/originals/dc/0c/4a/dc0c4ab51d2e6547bea512a128c0d3ce.jpg')
        embed.add_field(name='Children of the Abyssal Horror',value="""You have been fully accepted into the middle ring of the abyss. The Abyssal Horror himself is now calling you his child. You longer serve the purpose of mortals, and am so close to immortality. It is coming to you, just like the abyss once was.
{}/9762 xp until next level.""".format(xp.read()))
      elif agents in member.roles and lord not in member.roles:
        embed.set_image(url='https://i.pinimg.com/736x/54/78/27/547827e8c06160b87474ff4f943c4e3a.jpg')
        embed.add_field(name='Agents of Chaos',value="""It is done. You have become immortal. Your reign over this realm so gifted by that horror itself will be horrendous and sweet. Long will you spread chaos and the abyss. Many will grow under you. Immortality is forever... after all.
{}/24405 xp until next level.""".format(xp.read()))
      elif lord in member.roles:
        embed.set_image(url='http://conceptartworld.com/wp-content/uploads/2014/01/Dark_Souls_Design_Works_02.jpg')
        embed.add_field(name='Lord of the Deep',value='''You have conquered even the abyss itself. All lays under your rule. Whether it stays in ruin or grows is up to you. You are more than an immortal... You are a Lord!
{} is your total xp.'''.format(xp.read()))
    await ctx.send(embed=embed)
  else:
    await ctx.send('They are not currently initiated into receiving xp. Please do so first.')
  await xp_roles(ctx)

"""@client.command(name='giverolesetup')
async def give_role_setup(ctx):
  role = discord.utils.get(ctx.author.roles, id=621554107488141312)
  def check(message):
    return message.author == ctx.author and message.channel == msg.channel

  if role in ctx.author.roles:
    msg = await ctx.send('What message would you like me to send for the users to react to?')
    msg = await client.wait_for('message',check=check)
    

  else:
    await ctx.send('You do not have permission to use this command.')"""

client.loop.create_task(change_status())
client.run(TOKEN)
print("Bot running.")
keep_cult_alive.keep_cult_alive()
