import discord
import random
import os
from discord.ext import commands
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions

client = commands.Bot(command_prefix = '=')

@client.command()
@has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
  await member.kick(reason=reason)
  await ctx.send(f'User {member} has been kicked')

@kick.error
async def kick_error(ctx, error):
  if isinstance(error, commands.MissingPermissions):
    await ctx.send("```You do not have the required permissions to kick users.```")

@client.command()
@has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
  await member.ban(reason=reason)
  await ctx.send(f'User {member} has been banned')

@ban.error
async def ban_error(ctx, error):
  if isinstance(error, commands.MissingPermissions):
    await ctx.send("```You do not have the required permissions to ban users.```")

@client.command()
@has_permissions(ban_members=True)
async def unban(ctx, user: discord.User, *, reason=None):
  await ctx.guild.unban(user, reason=reason)
  await ctx.send(f'User {user} has been unbanned')

@client.command(pass_context=True)
async def hug(ctx, *, member):
    author_name = ctx.message.author.name
    await ctx.send(f'{author_name} has hugged {member}')
    hugs = ['https://tenor.com/view/hug-cuddle-comfort-love-friends-gif-5166500' , 'https://tenor.com/view/a-whisker-away-hug-love-anime-embrace-gif-17694740' , 'https://tenor.com/view/anime-hug-gif-15249774' , 'https://tenor.com/view/anime-hug-sweet-love-gif-14246498' , 'https://tenor.com/view/hug-anime-love-sweet-tight-hug-gif-7324587' , 'https://tenor.com/view/anime-hug-manga-cuddle-japan-gif-10522729' , 'https://tenor.com/view/horimiya-izumi-miyamura-hori-kyoko-couple-hug-gif-14539121' , 'https://tenor.com/view/sakura-quest-anime-animes-hug-hugging-gif-14721541']
    hugsrandom = random.choice(hugs)
    await ctx.send(hugsrandom)

@client.command(pass_context=True)
async def slap(ctx, *, member):
    author_name = ctx.message.author.name
    await ctx.send(f'{author_name} slapped {member}')
    slaps = ['https://tenor.com/view/girl-slap-anime-mad-student-gif-17423278' , 'https://tenor.com/view/anime-slap-mad-gif-16057834' , 'https://tenor.com/view/naruto-anime-slap-slapping-sakura-gif-17897216' , 'https://tenor.com/view/powerful-head-slap-anime-death-tragic-gif-14358509' , 'https://tenor.com/view/butt-slap-hunterxhunter-anime-slap-ouch-gif-12178034' , 'https://tenor.com/view/gintama-gintoki-sakata-sadaharu-dog-big-dog-gif-17670982']
    slapsrandom = random.choice(slaps)
    await ctx.send(slapsrandom)


client.run('ODU3OTkzOTI2NTE0MzExMjMw.YNXrHA.MDQ1fyW4nMdkbt0G06ct-BOwAlY')