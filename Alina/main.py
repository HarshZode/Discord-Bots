import discord 
from discord import guild   
from discord import message
from discord.ext import commands
import json
import asyncio
import os
import random
from keep_alive import keep_alive


client =  discord.Client()
client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.online,activity=discord.Activity(type=discord.ActivityType.watching, name="over your messages"))
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Alex<3"))
  while True:
        print("cleared")
        await asyncio.sleep(20)
        with open("spam_detect.txt", "r+") as file:
          file.truncate(0)


# # # Setting `Playing ` status
# await bot.change_presence(activity=discord.Game(name="a game"))

# # Setting `Streaming ` status
# await bot.change_presence(activity=discord.Streaming(name="My Stream", url=my_twitch_url))

# # Setting `Listening ` status
# await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="a song"))

# # Setting `Watching ` status
# await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="a movie"))

greetings = ['Hey alina', 'hey alina', 'hey Alina', 'hi alina', 'hello Alina', 'Hello alina', 'hiiiiii alina', "HELLO alina"]

greetings_back = ['Hey! Hope you have a great day! :)', 'Hey sweetie! Hope you are doing good today <3', 'Hey sugar! You are looking good today, hope you have a good day!', 'Hello. Hope you are doing good :3']

what_are_you_doing_question = ['what are you doing alina?', 'what are you doing rn alina?', 'what are you doing alina', 'what are you doing Alina?']

what_are_you_doing_answer = ["I'm doing your mom", "Nothing, just looking at the cutiest person here :)", "just reading the chat here, nothing else.", "Nothing, just looking at your dumbass", 'https://tenor.com/view/eddsworld-doing-your-mom-taco-sex-omw-gif-17267337']

mee6 = ['you just advanced to level']

mee6_insult = ['SHUT UP YOU STUPID BOT! NO ONE LOVES YOU!', 'GO KILL YOURSELF YOU STOOPID BOT!', 'GO FUCK YOURSELF! NOBODY LOVES YOU!', 'SHUT UP YOU PIECE OF SHIT!', " JUST GO KYS, You stink. I'm not insulting you, I'm describing you", "If i was a bird, I know who I'd shit on.", ' Life is short, so is your penis you stoopid bot.']

ily_msg = ['ily alina', 'ily Alina', 'ILY ALINA', 'ILY ALINAAAAAAAA', 'i love you alina', 'ILY alina','i love you Alina', 'i love you ALINA','love you alina', 'Alina ily','love you alina', 'i love alina', 'love alina','alina love','Alina ily','alina is bae','Alina cute','I love you Alina']

ily_msg_reply = ['ily too! <3<3<3', 'ILY MORE!', 'ILY TOOOO!!']

tired_shit = ["I'm tired", 'tired', 'having a headache', 'head is paining', 'tired af']

tired_reply = ['You should take some rest honey <3', "you did great today, now you should take some rest :3", 'hey cutie! you should rest now']

thanks_alina = ['thanks alina', 'Thanks alina', 'Thanks Alina', 'thank you alina', 'Thank you alina', 'THANK YOU ALINA', 'THANK YOU alina','THANKS ALINA']

thanks_alina_reply = ['your most welcome :3', 'anytime 😉']

cry_about_it_msg = ['cry about it', 'CRY ABOUT IT',  'Cry about it']

cry_about_it_gif = ['https://tenor.com/view/cry-about-it-cry-about-it-meme-gif-20184012', 'https://tenor.com/view/lizard-dancing-lizard-cry-about-it-gecko-dance-gif-20175430', 'https://tenor.com/view/fat-albert-cry-about-cry-keep-crying-salty-gif-20706773', 'https://tenor.com/view/cry-about-it-amogus-among-us-sus-impostor-gif-20613035', 'https://tenor.com/view/cry-about-it-gif-20739331', 'https://tenor.com/view/cry-about-it-gif-20909236', 'https://tenor.com/view/cry-about-it-gif-21324324']

gm_msg = ["Morning", "good morning", "morning"]

gm_reply = ["Good morning sweetie! Hope you slept well <3 ",
"Morning beautiful! hope you have a good day.", "Good Morning! you looking hot today ngl <:dontstoptaken:819789611558895618>"]

night_msg = ['good night', 'night everyone', 'gn']

night_msg_reply = ['good night!!', 'sleep well dear, ly <3', 'night night :D', 'gn sweetie!', 'good night!! ly <3<3']

bye = ['cya guys', "catch y'all later", "catch yall later", "see you guys later", "bye", "cya"]

bye_reply = ['see you later!', 'Hope you have a good day!!', "cya! don't forget we all love you!", "see you later, ly<3"]

bad_word = ['nigga', 'nigger', 'faggot', 'n*gger', 'fag', 'f*ggot','Nigga',"NIGGA"]

insult_alina = ['fuck you alina', 'you suck alina', 'you suck ass alina', "kys alina", "FUCK YOU ALINA",'fuck alina', 'FUCK U ALINA', 'alina you suck','fuck u alina', 'SHUT YO BITCH ASS UP HOE', 'Alina shut the fuck up','stfu alina','alina stfu', 'fuck off alina',"ALINA YOU DUMB BITCH",'Fuck u Alina','fuck u Alina','Fuck you alina','fuck you Alina','Fuck you Alina']

alina_reply = ["imagine insulting a bot bc you have no work to do <:dielit:820094269074440203> ", "FUCK YOU! YOU PIECE OF SHIT!", "LOL kys <:dielit:820094269074440203>" , "your mom is under my table. <:dielit:820094269074440203> cry about it", "ok and? <:dielit:820094269074440203>", "sorry can't talk, I'm doing your mom <:dielit:820094269074440203>"]

balls = ['balls', 'BALLS', 'Balls']

balls_reply = ['balls', 'umm balls', 'BALLS','https://tenor.com/view/cock-dick-balling-we-cock-dick-balling-gif-17448069','https://tenor.com/view/cock-dick-balling-lowtiergod-low-gif-20633820','https://tenor.com/view/dog-toy-twerk-what-butt-gif-4580835','https://tenor.com/view/nuts-balls-hammer-cinder-block-gif-14171513','https://tenor.com/view/no-balls-labyrinth-rolling-gif-5356481','https://tenor.com/view/balls-dance-rotate-beating-gif-17433105','https://tenor.com/view/ball-bird-gif-5261625']

alina = ['watermelon','cock and ball', 'cock', 'Cock','ball', 'Ball']

emotes = ['<:dielit:820094269074440203>','🥰', '<:squid_lick:813908756102250526>', '<:slimemoment:819788846928494603>']

frog = ["frog", 'Frog','FROG']

frog_emote = ['🐸','<:when_frog3:840114036456685588>']

dielit = ['dielit']

dielit_emote = ['<:dielit:820094269074440203>']

milk = ['milk', 'Milk', 'MILK']

milk_reply = ['<:milk-1:849501740562382859>']

larry = ['larry', 'Larry','LARRY']

larry_reply =['<:hearts-1:849503588576526367>']

bee = ['bee', 'Bee', 'BEE']

bee_reply = ['🐝']

shade = ['Shade','SHADE','shade']

shade_reply = ['<:tired_shade:813922972787539978>']

cece = ['cece', 'CECE', 'Cece']

cece_reply = ['💞','<:when_cece:838642904444567563>', '<:when_cece:838642745597886522>']

taken = ['TAKEN', 'taken', 'Taken']

taken_reply = ['<:cutecat:845253380535615498>']

ily_cece = ['ily cece', 'Ily cece', 'I love you cece','I LOVE YOU CECE', 'I LOVE YOU cece', 'I love you too shade', 'ily shade', 'ILY shade', 'I love you shade', 'I LOVE YOU SHADE', 'love you too cece', 'i love you shade','I LOVE CECE', 'i love shade', 'i love damian', 'Love you shade', 'Love you cece', 'love you shade', 'love you cece', 'love you slime', 'Love you slime']

ily_cece_reply = ['<:shade_hug:813908949622718464>','<:when_love:840181777935106089>']

duck =[ 'duck', 'Duck', 'DUCK']

duck_reply= ['<:swaggin:843691392261292082>']

nathan = ['nathan', "Nathan", 'NATHAN']

# nathan_reply = ['<:nathanironman:816389944431214633>', '<:NATHAN_POG:813922497833467915>']
nathan_reply =['<:when_nathan:840112246034137118>','<:NATHAN_POG:813922497833467915>']

slime = ['slime', 'Slime', 'SLIME']

slime_reply = ['<:holupslime:834936920361402368>', '<:slimemoment:819788846928494603>','<:slime_boner:813923873631633418>', '<:baked_slime:813923467464146975>']

yander =[ 'yander', 'Yander', 'YANDER']

yander_reply = ['<:cartiwtf:836724967701479424>']

marviie = ['Marviie', 'marviie', 'marvie', 'MARVIIE', 'MARVIE']

marviie_reply = ['<:when_marviie:838638459962916864>', '<:when_marv2:838641055061901342>', '<:when_marv3:838641241624674305>']

# marviie_reply = ['<:when_marvie:650885644700090378>']

germ = ['germ', "GERM", 'Germ']

germ_reply = ['<:when_germ:838644138639097867>']

ivana = ['ivana', 'Ivana', 'IVANA']

ivana_reply = ['<:when_ivana:838643336478851072>']

raven = ['raven', 'Raven', 'RAVEN']

raven_reply =['<:when_raven:838643193876578384>']

ebic = ['ebic', 'Ebic', 'EBIC']

ebic_reply = ['<:when_ebic:838643913660563504>']

angel = ['angel', 'Angel', 'ANGEL']
angel_reply = ['<:giggle:845252823791960095>']

cat = ['cat', 'Cat', 'CAT']

cat_reply = ['🐱', "🐈" ]

benis = ['Benis', 'benis' , 'BENIS','boob', 'seggs', 'Boob', 'Seggs', 'sex', 'Sex' 'fuck', 'Fuck', 'BOOBS','SEX']

benis_reply = ['<:when_benis:838648168543289384>','<:when_benis2:838648660890746910>','<:when_benis3:838649453769654283>']

amongus = ['Amongus', 'amongus', 'amogus','among us', 'Amongus','among us', 'Among us', 'Amogus', 'Among Us','sus', 'Sus','SUS']

amongus_reply = ['<:when_amongus:838650861458030592>']

dias = ['dias', 'Dias', 'DIAS']

dias_reply = ['<:when_dias:838652496830005280>']

hbc = ['hbc', 'Hbc', 'HBC' ,'honey', 'Honey', 'HONEY']

hbc_reply = ['when_hbc:838653010590564373']

benie = ['benie', 'Benie', 'BENIE','beanie', 'Beanie','BEANIE','beanie','Beanie']

benie_reply = ['<:when_beanie:840086649618825256>']

dalene = ['dalene', 'Dalene', 'DALENE','Dalene']

dalene_reply = ['<:when_dalene:838677866514219030>', '<:when_dalene2:838677881566658580>']

glyph = ['glyph', 'Glyph', 'GLYPH']

glyph_reply = ['<:when_gylph:838762419580436497>']

gabe = ['gabe','Gabe', 'GABE']

gabe_reply = ['<:when_gabe:840090137579749376>']

arie = ['arie', 'Arie', 'ARIE']

arie_reply =['<:when_arie:840093888186155019>','<:when_arie2:840096736239157278>']

mularo = ['mularo', 'Mularo']

mularo_reply =['<:when_mularo:840107058279874620>']

mularoo = ['https://cdn.discordapp.com/attachments/821723207672922112/840184324259315752/mularo.jpg']

red = ['red robin', 'Red Robin', 'Red robin']
red_reply = ['yum']

test = ['test']

test_reply = ['<a:when_marvie:838681967649882123>']

hobby = ["what's your hobby alina","what is your hobby alina","whats your hobby alina?","Whats your hobby alina", "What's your hobby alina","whats your hobby alina","alina what's your hobby","Alina what's your hobby","alina whats your hobby","Alina whats your hobby"]

hobby_reply = ["Doing your mom <a:when_marvie:838681967649882123>"]

midget =['midget','Midget',"MIDGET"]

midget_reply = ['<:char:844880564628094996>']

tanry = [ 'tanry', 'Tanry', 'TANRY']

tanry_reply = ['<:brr:844883001426313256>']

inji = ['inji', 'Inji', 'INJI']

inji_reply = ['<:Edball:844888325881200651>']

shiva = ['shiva','Shiva', 'SHIVA']

shiva_reply = ['<:stomp:845239558786252820>','<:cathaircut:845261957857542175>']

kel = ['kel','Kel','KEL']

kel_reply = ['<:cutie:847692684377980959>']

joise = ['josie', 'Josie', 'JOSIE']

joise_reply = ['<:kiss-1:847692706171846658>']

bella = ['bella','Bella','BELLA']

bella_reply = ['<:ly:847692667479523338>']

blu =['blu', 'Blu','BLU']

blu_reply =['<:pepe_vibe:848495805140434954>']

jin =['jin', 'Jin', 'JIN']

jin_reply =['<:fedora_howdy:813908530464686091>']

pog =['pog', 'Pog', 'POG']


pog_reply =['<:catpog:848780546209480754>','<:catpog2:848781541852446740>','<a:catpog3:848782160654893066>']

dab =['dab','Dab', 'DAB']

dab_reply =['<:dab:848785556129316885>','<a:dabcrazy3:849395998891311134>','<a:dabcrazy2:849395782775472168>']

alex_insult =['fuck you alex', 'Alex is a bitch',"you're ugly alex","you're ugly Alex",'Fuck you alex', 'Alex a bitch','fuck you alex','Shut up Alex', 'shut up alex', 'shut up Alex','stfu alex', 'alex stfu','Alex stfu', 'alex stfu']

matt= ['matt','Matt','MATT']

matt_reply = ['<:stab:875620208579055636>']

stud =['stud','Stud','STUD']

stud_reply =['<:drum2:849537773961609236>','<:drum-1:849536701730521109>']

bispy = ['spy','Spy','SPY']

bispy_reply =['<:Rainbowcat:854938973540974622>', '<:yeahcute:854938954452041729>']

@client.event
async def on_message(message):
  counter = 0
  with open("spam_detect.txt", "r+") as file:
        for lines in file:
            if lines.strip("\n") == str(message.author.id):
                counter+=1

        file.writelines(f"{str(message.author.id)}\n")
        if counter > 7:
            
            if message.author.id == 837285152698400798:
              return
            elif message.author.id == 837974929869111318:
              return
            else:
              var = discord.utils.get(message.guild.roles, name = "Muted")
              if var in message.author.roles or message.author.bot == True:
               return
              else:
             
               embed = discord.Embed(title="Muted", description=f"{message.author.mention} was muted for 60 sec (`spamming`)", colour=discord.Colour.dark_purple())
               await message.channel.send(embed=embed)
            
               await message.author.add_roles(var)
               await asyncio.sleep(60)
               embed = discord.Embed(title="Unmuted", description=f"{message.author.mention} ", colour=discord.Colour.dark_purple())
               await message.channel.send(embed=embed)
               await message.author.remove_roles(var)
  
  if message.author == client.user:
    return
  
  if message.guild.id == 790495293069459466 or 838637875636600862 or 844851417830260756 or 813894466036957184 :
   if message.content.startswith('$hello'):
    await message.channel.send("Hello!")

   if message.content.startswith('showlist'):
     var = discord.utils.get(message.guild.roles, name = "Muted")
     if var in message.author.roles:
       await message.channel.send('has rolse homies')
     else:
       await message.channel.send('Does not have the role')
    
   if any (word in message.content for word in greetings):
    await message.channel.send(random.choice(greetings_back))
  
   if any (word in message.content for word in what_are_you_doing_question):
    await message.channel.send(random.choice(what_are_you_doing_answer))

   if any (word in message.content for word in mee6):
    # await message.delete()
    await message.reply(random.choice(mee6_insult))

   if any (word in message.content for word in ily_msg):
    await message.channel.send(random.choice(ily_msg_reply))

   if any (word in message.content for word in tired_shit):
    await message.channel.send(random.choice(tired_reply))

   if any (word in message.content for word in cry_about_it_msg):
    await message.channel.send(random.choice(cry_about_it_gif))
  
   # if any (word in message.content for word in gm_msg):
   #   await message.channel.send(random.choice(gm_reply))
  
   # if any (word in message.content for word in night_msg):
   #   await message.channel.send(random.choice(night_msg_reply))

   if any (word in message.content for word in bye):
    await message.channel.send(random.choice(bye_reply))

   if any (word in message.content for word in pog):
    await message.channel.send(random.choice(pog_reply))

   if message.content.startswith('!hello'):
        msg = 'Hi {0.author.mention}'.format(message)
        await message.channel.send(msg)

   if any (word in message.content for word in bad_word):
    await message.delete()
    # await message.channel.send("DON'T SAY THAT YOU DUMB DUMB! {0.author.mention}".format(message))
    await message.channel.send(":regional_indicator_n::regional_indicator_o: `{0.author}` <:dielit:820094269074440203>".format(message))
  
   if any (word in message.content for word in insult_alina):
    await message.channel.send(random.choice(alina_reply))

   if any (word in message.content for word in balls):
    await message.channel.send(random.choice(balls_reply))

   if any (word in message.content for word in dab):
    await message.channel.send(random.choice(dab_reply))

   if any (word in message.content for word in alina):
     await message.add_reaction(random.choice(emotes))

   if any (word in message.content for word in frog):
     await message.add_reaction(random.choice(frog_emote))

   if any (word in message.content for word in dielit):
     await message.add_reaction(random.choice(dielit_emote))

   if any (word in message.content for word in thanks_alina):
      await message.channel.send(random.choice(thanks_alina_reply))

   if any (word in message.content for word in milk):
     await message.add_reaction(random.choice(milk_reply))

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

   if any (word in message.content for word in marviie):
     await message.add_reaction(random.choice(marviie_reply))

   if any (word in message.content for word in angel):
     await message.add_reaction(random.choice(angel_reply))

   if any (word in message.content for word in taken):
     await message.add_reaction(random.choice(taken_reply))

   if any (word in message.content for word in ily_cece):
     await message.add_reaction(random.choice(ily_cece_reply))

   if any (word in message.content for word in duck):
     await message.add_reaction(random.choice(duck_reply))

   if any (word in message.content for word in germ):
     await message.add_reaction(random.choice(germ_reply))

   if any (word in message.content for word in cat):
     await message.add_reaction(random.choice(cat_reply))

   if any (word in message.content for word in ivana):
     await message.add_reaction(random.choice(ivana_reply))

   if any (word in message.content for word in raven):
     await message.add_reaction(random.choice(raven_reply))

   if any (word in message.content for word in ebic):
     await message.add_reaction(random.choice(ebic_reply))

   if any (word in message.content for word in benis):
       await message.add_reaction(random.choice(benis_reply))

   if any (word in message.content for word in amongus):
     await message.channel.send(random.choice(amongus_reply))

   if any (word in message.content for word in dias):
     await message.add_reaction(random.choice(dias_reply))

   if any (word in message.content for word in hbc):
     await message.add_reaction(random.choice(hbc_reply))

   if any (word in message.content for word in benie):
     await message.add_reaction(random.choice(benie_reply))

   if any (word in message.content for word in dalene):
     await message.add_reaction(random.choice(dalene_reply))

   if any (word in message.content for word in glyph):
     await message.add_reaction(random.choice(glyph_reply))

   if any (word in message.content for word in red):
    await message.channel.send(random.choice(red_reply))

   if any (word in message.content for word in gabe):
     await message.add_reaction(random.choice(gabe_reply))

   if any (word in message.content for word in arie):
     await message.add_reaction(random.choice(arie_reply))

   if any (word in message.content for word in mularo):
     await message.add_reaction(random.choice(mularo_reply))
     await message.channel.send('https://media.discordapp.net/attachments/821723207672922112/840184945569169429/ezgif-2-15fbe5adf5f0.gif')

   if any (word in message.content for word in test):
     await message.channel.send(random.choice(test_reply))

   if any (word in message.content for word in germ):
     await message.add_reaction('💗')
  
   if any (word in message.content for word in germ):
     await message.add_reaction('💘')

   if any (word in message.content for word in hobby):
     await message.channel.send(random.choice(hobby_reply))
     await message.channel.send("<a:laugh:844783191189356575>")

   if any (word in message.content for word in midget):
     await message.add_reaction(random.choice(midget_reply))
    
   if any (word in message.content for word in tanry):
     await message.add_reaction(random.choice(tanry_reply))

   if any (word in message.content for word in inji):
    await message.add_reaction(random.choice(inji_reply))

   if any (word in message.content for word in shiva):
    await message.add_reaction(random.choice(shiva_reply))

   if any (word in message.content for word in kel):
     await message.add_reaction(random.choice(kel_reply))

   if any (word in message.content for word in joise):
     await message.add_reaction(random.choice(joise_reply))

   if any (word in message.content for word in bella):
     await message.add_reaction(random.choice(bella_reply))

   if any (word in message.content for word in blu):
     await message.add_reaction(random.choice(blu_reply))

   if any (word in message.content for word in larry):
     await message.add_reaction(random.choice(larry_reply))

   if any (word in message.content for word in bispy):
     await message.add_reaction(random.choice(bispy_reply))

   if any (word in message.content for word in matt):
     await message.add_reaction(random.choice(matt_reply))

   if any (word in message.content for word in stud):
     await message.add_reaction("<:drum-1:849536701730521109>")
     await message.add_reaction("<:ddrums:849539509019607080>")
     await message.add_reaction('<:drum2:849537773961609236>')

   if any (word in message.content for word in jin):
     await message.add_reaction(random.choice(jin_reply))
    
   if any (word in message.content for word in alex_insult):
     embed = discord.Embed(description='really?', colour=discord.Colour.dark_purple())
     await message.channel.send(embed=embed)

     embed = discord.Embed(description=f"{message.author.mention} was muted.  (`ENJOY!`)", colour=discord.Colour.dark_purple())
     await message.channel.send(embed=embed)


     var = discord.utils.get(message.guild.roles, name = "Muted")

     await message.author.add_roles(var)
     
     
     await asyncio.sleep(30)
     embed = discord.Embed(title="Unmuted", description=f"{message.author.mention} ", colour=discord.Colour.dark_purple())
     await message.channel.send(embed=embed)
     await message.author.remove_roles(var)

verify_emote = "✅"

@client.event
async def on_reaction_add(reaction, user):
  ChID = '761174269144727572'
  if reaction.message.channel.id != ChID:
    return
  if reaction.emoji == "🏃":
    CSGO = discord.utils.get(user.server.roles, name="✪ Homies")
    await client.add_roles(user, CSGO)
      # Role = discord.utils.get(user.server.roles, name = "✪ Homies")
      # await client.add_role(user,Role)
      

  

  
  





  
     
    


keep_alive()

client.run(os.getenv('TOKEN'))
