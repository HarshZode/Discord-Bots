import discord 
from discord import guild
from discord import message
from discord.ext import commands
import random
import json
import asyncio
import os
from keep_alive import keep_alive


client =  discord.Client()
client = commands.Bot(command_prefix = '.')

reply = ['You really thought I would do that?','on my way to do your mom <:dielit:820094269074440203>','Man shut yo bitch ass up']

alex_insult =['alex sucks', 'fuck you alex']


#################################################################
@client.command()
async def ping(ctx):
  # await ctx.send(f'<:dielit:820094269074440203> Ping : {round(client.latency * 1000)}ms')
  embed = discord.Embed(description=f" {round(client.latency * 1000)}ms", colour=discord.Colour.dark_purple())
  await ctx.send(embed=embed)

###################################################################
@client.command()
@commands.has_permissions(manage_channels=True)
async def lockdown(ctx):
  await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
  await ctx.send('<:dielit:820094269074440203> ' + ctx.channel.mention + " `is now in lockdown.` <:dielit:820094269074440203> ")

@client.command()
@commands.has_permissions(manage_channels=True)
async def unlock(ctx):
  await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
  await ctx.send('<:dielit:820094269074440203> ' + ctx.channel.mention + " `is unlocked.` <:dielit:820094269074440203>") 

###################################################################

@client.command(description="Mutes the specified user.")
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason=None):

  if member.id == 837285152698400798:
       embed = discord.Embed(description=random.choice(reply), colour=discord.Colour.dark_purple())
       await ctx.send(embed=embed)
       return

  elif member.id == 837974929869111318:
       embed = discord.Embed(description=random.choice(reply), colour=discord.Colour.dark_purple())
       await ctx.send(embed=embed)
       return
  else:
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")

    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole,speak=False, send_messages=False, read_message_history=True, read_messages=False)
    embed = discord.Embed(title="Muted", description=f"{member.mention} ", colour=discord.Colour.dark_purple())
    embed.add_field(name="reason:", value=reason, inline=False)
    await ctx.send(embed=embed)
    await member.add_roles(mutedRole, reason=reason)
    await member.send(f" you have been muted from: {guild.name} reason: {reason}")

@client.command(description="Unmutes a specified user.")
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
   mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

   await member.remove_roles(mutedRole)
   await member.send(f" you have unmuted from: - {ctx.guild.name}")
   embed = discord.Embed(description=f" Unmuted-{member.mention}",colour=discord.Colour.dark_purple())
   await ctx.send(embed=embed)
        
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Alina<3"))
  while True:
        print("cleared")
        await asyncio.sleep(20)
        with open("spam_detect.txt", "r+") as file:
          file.truncate(0)

######################################################################

@client.command()
@commands.has_permissions(manage_messages=True)
async def slowmode(ctx, seconds: int):
  await ctx.channel.edit(slowmode_delay=seconds)
  await ctx.send(f"<:dielit:820094269074440203> Slowmode set to `{seconds} sec` in "+ ctx.channel.mention)

####################################################################

@client.command()
async def avatar(ctx, *,  avamember : discord.Member=None):
   userAvatarUrl = avamember.avatar_url
   embed = discord.Embed(colour=discord.Colour.dark_purple())
   embed.set_image(url=userAvatarUrl)
   await ctx.send(embed=embed)
    


keep_alive()

client.run(os.getenv('TOKEN'))