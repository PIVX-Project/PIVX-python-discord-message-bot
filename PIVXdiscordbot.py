import discord
from discord.ext import commands
import configparser
configParser = configparser.RawConfigParser()   
configParser.readfp(open(r'messages.ini'))
client = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord.')

@client.command(aliases=['SNAPSHOT'])
async def snapshot(ctx):
    try:
        msg = (configParser.get('messages', 'snapshotmsg'))
        await ctx.send(f'✅  ' + msg)
    except:
        await ctx.send('❌ ERROR')

@client.command(aliases=['FORKED'])
async def forked(ctx):
    try:
        msg = (configParser.get('messages', 'forkedmsg'))
        await ctx.send(f'✅  ' + msg)
    except:
        await ctx.send('❌ ERROR')

@client.command(aliases=['TOOLBOX'])
async def toolbox(ctx):
    try:
        msg = (configParser.get('messages', 'snapshotmsg'))
        await ctx.send(f'✅  ' + msg)
    except:
        await ctx.send('❌ ERROR')


@client.command(aliases=['DMTEST'])
async def dm(ctx):
    try:
        user = ctx.author
        await user.send('this will DM the tageed user')
        await ctx.send(f'✅ message sent')
    except:
        await ctx.send('❌ Member had their dm close, message not sent')

import discord
from discord.ext import commands
import configparser
configParser = configparser.RawConfigParser()   
configParser.readfp(open(r'messages.ini'))
client = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord.')

@client.command(aliases=['SNAPSHOT'])
async def snapshot(ctx):
    try:
        msg = (configParser.get('messages', 'snapshotmsg'))
        await ctx.send(f'✅  ' + msg)
    except:
        await ctx.send('❌ ERROR')

@client.command(aliases=['FORKED'])
async def forked(ctx):
    try:
        msg = (configParser.get('messages', 'forkedmsg'))
        await ctx.send(f'✅  ' + msg)
    except:
        await ctx.send('❌ ERROR')

@client.command(aliases=['TOOLBOX'])
async def toolbox(ctx):
    try:
        msg = (configParser.get('messages', 'snapshotmsg'))
        await ctx.send(f'✅  ' + msg)
    except:
        await ctx.send('❌ ERROR')


@client.command(aliases=['DMTEST'])
async def dm(ctx):
    try:
        user = ctx.author
        await user.send('this will DM the tageed user')
        await ctx.send(f'✅ message sent')
    except:
        await ctx.send('❌ Member had their dm close, message not sent')

import discord
from discord.ext import commands
import configparser
configParser = configparser.RawConfigParser()   
configParser.readfp(open(r'messages.ini'))
client = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord.')

@client.command(aliases=['SNAPSHOT'])
async def snapshot(ctx):
    try:
        msg = (configParser.get('messages', 'snapshotmsg'))
        await ctx.send(f'✅  ' + msg)
    except:
        await ctx.send('❌ ERROR')

@client.command(aliases=['FORKED'])
async def forked(ctx):
    try:
        msg = (configParser.get('messages', 'forkedmsg'))
        await ctx.send(f'✅  ' + msg)
    except:
        await ctx.send('❌ ERROR')

@client.command(aliases=['TOOLBOX'])
async def toolbox(ctx):
    try:
        msg = (configParser.get('messages', 'snapshotmsg'))
        await ctx.send(f'✅  ' + msg)
    except:
        await ctx.send('❌ ERROR')


@client.command(aliases=['DMTEST'])
async def dm(ctx):
    try:
        user = ctx.author
        await user.send('this will DM the tageed user')
        await ctx.send(f'✅ message sent')
    except:
        await ctx.send('❌ Member had their dm close, message not sent')

client.run('<botkeygoeshere>')
