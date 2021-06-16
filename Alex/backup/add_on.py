import discord 
from discord import guild
from discord import message
from discord.ext import commands
import json
import asyncio
import os
import random

client =  discord.Client()
client = commands.Bot(command_prefix = '.')

greetings = ['Hey alina', 'hey alina', 'hey Alina', 'hi alina', 'hello Alina', 'Hello alina', 'hiiiiii alina', "HELLO alina"]

greetings_back = ['Hey! Hope you have a great day! :)', 'Hey sweetie! Hope you are doing good today <3', 'Hey sugar! You are looking good today, hope you have a good day!', 'Hello. Hope you are doing good :3']

what_are_you_doing_question = ['what are you doing alina?', 'what are you doing rn alina?', 'what are you doing alina', 'what are you doing Alina?']

what_are_you_doing_answer = ["I'm doing your mom", "Nothing, just looking at the cutiest person here :)", "just reading the chat here, nothing else.", "Nothing, just looking at your dumbass", 'https://tenor.com/view/eddsworld-doing-your-mom-taco-sex-omw-gif-17267337']

mee6 = ['you just advanced to level']

mee6_insult = ['SHUT UP YOU STUPID BOT! NO ONE LOVES YOU!', 'GO KILL YOURSELF YOU STOOPID BOT!', 'GO FUCK YOURSELF! NOBODY LOVES YOU!', 'SHUT UP YOU PIECE OF SHIT!', " JUST GO KYS, You stink. I'm not insulting you, I'm describing you", "If i was a bird, I know who I'd shit on.", ' Life is short, so is your penis you stoopid bot.']

ily_msg = ['ily aline', 'ily Alina', 'ILY ALINA', 'ILY ALINAAAAAAAA', 'i love you alina', 'ILY alina', 'i love you ALINA']

ily_msg_reply = ['ily too! <3<3<3', 'ILY MORE!', 'ILY TOOOO!!']

tired_shit = ["I'm tired", 'tired', 'having a headache', 'head is paining', 'tired af']

tired_reply = ['You should take some rest honey <3', "you did great today, now you should take some rest :3", 'hey cutie! you should rest now']

thanks_alina = ['thanks alina', 'Thanks alina', 'Thanks Alina', 'thank you alina', 'Thank you alina', 'THANK YOU ALINA', 'THANK YOU alina','THANKS ALINA']

thanks_alina_reply = ['your most welcome :3', 'anytime 😉']

cry_about_it_msg = ['cry about it', 'cry', 'CRY ABOUT IT', 'CRY', 'Cry about it']

cry_about_it_gif = ['https://tenor.com/view/cry-about-it-cry-about-it-meme-gif-20184012', 'https://tenor.com/view/lizard-dancing-lizard-cry-about-it-gecko-dance-gif-20175430', 'https://tenor.com/view/fat-albert-cry-about-cry-keep-crying-salty-gif-20706773', 'https://tenor.com/view/cry-about-it-amogus-among-us-sus-impostor-gif-20613035', 'https://tenor.com/view/cry-about-it-gif-20739331', 'https://tenor.com/view/cry-about-it-gif-20909236', 'https://tenor.com/view/cry-about-it-gif-21324324']

gm_msg = ["Morning", "good morning", "morning"]

gm_reply = ["Good morning sweetie! Hope you slept well <3 ",
"Morning beautiful! hope you have a good day.", "Good Morning! you looking hot today ngl <:dontstoptaken:819789611558895618>"]

night_msg = ['good night', 'night everyone', 'gn']

night_msg_reply = ['good night!!', 'sleep well dear, ly <3', 'night night :D', 'gn sweetie!', 'good night!! ly <3<3']

bye = ['cya guys', "catch y'all later", "catch yall later", "see you guys later", "bye", "cya"]

bye_reply = ['see you later!', 'Hope you have a good day!!', "cya! don't forget we all love you!", "see you later, ly<3"]

bad_word = ['nigga', 'nigger', 'faggot', 'n*gger', 'fag', 'f*ggot']

insult_alina = ['fuck you alina', 'you suck alina', 'you suck ass alina', "kys alina", "FUCK YOU ALINA",'fuck alina', 'FUCK U ALINA', 'alina you suck','fuck u alina', 'SHUT YO BITCH ASS UP HOE', 'Alina shut the fuck up']

alina_reply = ["imagine insulting a bot bc you have no work to do <:dielit:820094269074440203> ", "FUCK YOU! YOU PIECE OF SHIT!", "LOL kys <:dielit:820094269074440203>" , "your mom is under my table. <:dielit:820094269074440203> cry about it", "ok and? <:dielit:820094269074440203>", "sorry can't talk, I'm doing your mom <:dielit:820094269074440203>"]

balls = ['balls', 'BALLS', 'Balls']

balls_reply = ['balls', 'umm balls', 'BALLS','https://tenor.com/view/cock-dick-balling-we-cock-dick-balling-gif-17448069','https://tenor.com/view/dog-toy-twerk-what-butt-gif-4580835']

alina = ['watermelon','cock and ball', 'cock', 'Cock','ball', 'Ball']

emotes = ['<:dielit:820094269074440203>','🥰', '<:squid_lick:813908756102250526>', '<:slimemoment:819788846928494603>']

frog = ["frog", 'Frog','FROG']

frog_emote = ['🐸']

dielit = ['dielit']

dielit_emote = ['<:dielit:820094269074440203>']

milk = ['milk', 'Milk', 'milker']

milk_reply = ['https://tenor.com/view/milk-cat-car-cat-milk-stupid-gif-18439761', 'https://tenor.com/view/milk-cat-drinking-milk-my-milk-gif-15557059']

bee = ['bee', 'Bee', 'BEE']

bee_reply = ['🐝']

shade = ['Shade']

shade_reply = ['<:tired_shade:813922972787539978>']

cece = ['cece', 'CECE', 'Cece']

cece_reply = ['💞']

taken = ['TAKEN', 'taken', 'Taken']

taken_reply = ['<:dontstoptaken:819789611558895618>']

ily_cece = ['ily cece', 'Ily cece', 'I love you cece','I LOVE YOU CECE', 'I LOVE YOU cece', 'I love you too shade', 'ily shade', 'ILY shade', 'I love you shade', 'I LOVE YOU SHADE', 'love you too cece', 'i love you shade','I LOVE CECE', 'i love shade', 'i love damian', 'Love you shade', 'Love you cece', 'love you shade', 'love you cece', 'love you slime', 'Love you slime']

ily_cece_reply = ['<:shade_hug:813908949622718464>']

duck =[ 'duck', 'Duck', 'DUCK']

duck_reply= ['🦆']

nathan = ['nathan', "Nathan", 'NATHAN']

nathan_reply = ['<:nathanironman:816389944431214633>', '<:NATHAN_POG:813922497833467915>']

slime = ['slime', 'Slime', 'SLIME']

slime_reply = ['<:holupslime:834936920361402368>', '<:slimemoment:819788846928494603>','<:slime_boner:813923873631633418>', '<:baked_slime:813923467464146975>']

yander =[ 'yander', 'Yander', 'YANDER']

yander_reply = ['<:cartiwtf:836724967701479424>']

test = ['germ', "GERM", 'Germ']

test_alina_reply = ['<:holupslime:834936920361402368>', '<:slimemoment:819788846928494603>','<:slime_boner:813923873631633418>', '<:baked_slime:813923467464146975>']

angel = ['angel', 'Angel', 'ANGEL']
angel_reply = ['🤩']



@client.event
async def on_message(message):
  
  if message.author == client.user:
    return
  

  if message.content.startswith('$hello'):
    await message.channel.send("Hello!")
  
  if any (word in message.content for word in greetings):
    await message.channel.send(random.choice(greetings_back))
  
  if any (word in message.content for word in what_are_you_doing_question):
    await message.channel.send(random.choice(what_are_you_doing_answer))

  if any (word in message.content for word in mee6):
   await message.channel.send(random.choice(mee6_insult))

  if any (word in message.content for word in ily_msg):
    await message.channel.send(random.choice(ily_msg_reply))

  if any (word in message.content for word in tired_shit):
    await message.channel.send(random.choice(tired_reply))

  if any (word in message.content for word in cry_about_it_msg):
    await message.channel.send(random.choice(cry_about_it_gif))
  
  if any (word in message.content for word in gm_msg):
    await message.channel.send(random.choice(gm_reply))
  
  if any (word in message.content for word in night_msg):
    await message.channel.send(random.choice(night_msg_reply))

  if any (word in message.content for word in bye):
    await message.channel.send(random.choice(bye_reply))

  if message.content.startswith('!hello'):
        msg = 'Hi {0.author.mention}'.format(message)
        await message.channel.send(msg)

  if any (word in message.content for word in bad_word):
    await message.delete()
    await message.channel.send("DON'T SAY THAT YOU DUMB DUMB! {0.author.mention}".format(message))
  
  if any (word in message.content for word in insult_alina):
    await message.channel.send(random.choice(alina_reply))

  if any (word in message.content for word in balls):
    await message.channel.send(random.choice(balls_reply))

  if any (word in message.content for word in alina):
     await message.add_reaction(random.choice(emotes))

  if any (word in message.content for word in frog):
     await message.add_reaction(random.choice(frog_emote))

  if any (word in message.content for word in dielit):
     await message.add_reaction(random.choice(dielit_emote))

  if any (word in message.content for word in thanks_alina):
     await message.channel.send(random.choice(thanks_alina_reply))

  if any (word in message.content for word in milk):
     await message.channel.send(random.choice(milk_reply))

  if any (word in message.content for word in bee):
     await message.add_reaction(random.choice(bee_reply))

  if any (word in message.content for word in slime):
     await message.add_reaction(random.choice(slime_reply))

  if any (word in message.content for word in shade):
     await message.add_reaction(random.choice(shade_reply))

  if any (word in message.content for word in cece):
     await message.add_reaction(random.choice(cece_reply))

  if any (word in message.content for word in nathan):
     await message.add_reaction(random.choice(nathan_reply))

  if any (word in message.content for word in yander):
     await message.add_reaction(random.choice(yander_reply))

  if any (word in message.content for word in angel):
     await message.add_reaction(random.choice(angel_reply))

  if any (word in message.content for word in taken):
     await message.add_reaction(random.choice(taken_reply))

  if any (word in message.content for word in ily_cece):
     await message.add_reaction(random.choice(ily_cece_reply))

  if any (word in message.content for word in duck):
     await message.add_reaction(random.choice(duck_reply))

  if any (word in message.content for word in test):
     await message.add_reaction('💖')

  if any (word in message.content for word in test):
     await message.add_reaction('💗')
  
  if any (word in message.content for word in test):
     await message.add_reaction('💘')
