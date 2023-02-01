import discord
from discord.ext import commands
import configparser
import requests
import datetime
from datetime import datetime


configParser = configparser.RawConfigParser()   
configParser.readfp(open(r'messages.ini'))
client = commands.Bot(command_prefix='/', intents=discord.Intents.all())



client.remove_command("help")


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord.')

@client.command(aliases=['BEER'])
async def beer(ctx):
    try:
        msg = (configParser.get('messages', 'beermsg'))
        sender = ctx.message.author.name
        await ctx.send(f'' + sender + ' :beers:  ' + msg)
    except:
        await ctx.send('❌ ERROR')

@client.command(aliases=['AUNTY'])
async def pivxaunty(ctx):
    try:
        msg = (configParser.get('messages', 'pivxauntymsg'))
        await ctx.send(f':boom:  ' + msg)
    except:
        await ctx.send('❌ ERROR')



@client.command(aliases=['HELP'])
async def help(ctx):
    try:
        msg = (configParser.get('messages', 'helpmsg'))
        await ctx.send(f'✅  ' + msg)
    except:
        await ctx.send('❌ ERROR')


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
        msg = (configParser.get('messages', 'toolboxmsg'))
        await ctx.send(f'✅  ' + msg)
    except:
        await ctx.send('❌ ERROR')

@client.command(aliases=['EXPLORER'])
async def explorer(ctx):
    try:
        msg = (configParser.get('messages', 'explorermsg'))
        await ctx.send(f'✅  ' + msg)
    except:
        await ctx.send('❌ ERROR')

@client.command(aliases=['MNSTATUS'])
async def mnstatus(ctx):
    try:
        msg = (configParser.get('messages', 'mnstatusmsg'))
        await ctx.send(f'✅  ' + msg)
    except:
        await ctx.send('❌ ERROR')

@client.command(aliases=['DOCS'])
async def docs(ctx):
    try:
        msg = (configParser.get('messages', 'docsmsg'))
        await ctx.send(f'✅  ' + msg)
    except:
        await ctx.send('❌ ERROR')

@client.command(aliases=['MPW'])
async def mpw(ctx):
    try:
        msg = (configParser.get('messages', 'mpwmsg'))
        await ctx.send(f'✅  ' + msg )
    except:
        await ctx.send('❌ ERROR')

@client.command(aliases=['VERSION'])
async def version(ctx):
    try:
        response = requests.get("https://api.github.com/repos/PIVX-Project/PIVX/releases/latest")
        version = (response.json()["name"])

        nLinuxDownloads = 0
        nWindowsDownloads = 0
        nMacDownloads = 0
        nSourceDownloads = 0
        nShaDownloads = 0
        nTotalDownloads = 0

        for asset in response.json()["assets"]:
            nTotalDownloads += asset["download_count"]

            if 'linux' in asset["name"]:
                nLinuxDownloads += asset["download_count"]
            elif 'osx' in asset["name"]:
                nMacDownloads += asset["download_count"]
            elif 'win' in asset["name"]:
                nWindowsDownloads += asset["download_count"]
            elif 'SHA' in asset["name"]:
                nShaDownloads += asset["download_count"]
            else:
                nSourceDownloads += asset["download_count"]

        relDate = datetime.strptime(response.json()["published_at"], '%Y-%m-%dT%H:%M:%SZ')
        await ctx.send(f'✅ PIVX latest version is: ' + version + ', was released on ' + relDate.strftime('%B %d, %Y') + ' \n:arrow_down: It has been downloaded a total of ' + str(nTotalDownloads) + ' times.')
    except:
        await ctx.send('❌ ERROR')


@client.command(aliases=['PRICE'])
async def price(ctx):
    try:
        responsepivx = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=pivx&vs_currencies=usd")
        usdPrice = (responsepivx.json()["pivx"]["usd"])
        responsebtc = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=pivx&vs_currencies=btc")
        btcPrice = (responsebtc.json()["pivx"]["btc"])
        await ctx.send(':coin: PIVX currect price is:\n   {:.8f}'.format(float(btcPrice)) + ' BTC \n   {:.3f}'.format(float(usdPrice)) + ' USD')
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

@client.command(aliases=['DMTEST2'])
async def dmtest(ctx, user : discord.User, *, mesg):
    try:
        sender = ctx.message.author.name
        await user.send(f'🕴️ ' + sender + ' sent you this message: ' + mesg)
        await ctx.send(f'✅ message sent')
    except:
        await ctx.send('❌ Member had their dm close, message not sent')


client.run('<botkeygoeshere>')
