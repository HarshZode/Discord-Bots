from discord import guild
from discord import embeds
from discord import message
from discord.ext import commands
import os
import random

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
  print("the Lockdown command is functional.")


@client.command()
@commands.has_permission(manage_channels = True)
async def lockdown(ctx):
  await ctx.channel.set_permissions(ctx.guild.default_role, send_messages = False)
  await message.channel.send(' <:dielit:820094269074440203> message.channel.mention is now in lockdown')




keep_alive()

client.run(os.getenv('TOKEN'))
