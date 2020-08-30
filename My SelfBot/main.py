import asyncio
import discord
import ctypes
import requests
from discord.ext import commands
from colorama import init, Fore, Back, Style

init(convert=True) # Don't delete this!!!

token = 'TOKEN-HERE' # Use an alt 

prefix = '+'

ID = 480477677569048582
# example: ID = 72756465435

bot = commands.Bot(
    description='Stealth is bae',
    command_prefix=prefix,
)
bot.remove_command('help') 

@bot.event
async def on_ready():
  game = discord.Game(name= "Stealth", type=3)
  await bot.change_presence(status=discord.Status.idle, activity=game)
  global servers 
  servers = len(list(bot.guilds))
  ctypes.windll.kernel32.SetConsoleTitleW(f'[Selfbot] By Stealth | prefix: {prefix}')
  print(f'''
  {Fore.RED}                                  ███████╗████████╗███████╗ █████╗ ██╗  ████████╗██╗  ██╗
                                    ██╔════╝╚══██╔══╝██╔════╝██╔══██╗██║  ╚══██╔══╝██║  ██║
                                    ███████╗   ██║   █████╗  ███████║██║     ██║   ███████║
                                    ╚════██║   ██║   ██╔══╝  ██╔══██║██║     ██║   ██╔══██║
                                    ███████║   ██║   ███████╗██║  ██║███████╗██║   ██║  ██║
                                    ╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝   ╚═╝  ╚═╝{Fore.RESET}
                                    Logged in as {Fore.MAGENTA}-{Fore.RESET} {Fore.GREEN}{bot.user}{Fore.RESET}
                                    Prefix {Fore.MAGENTA}-{Fore.RESET} {Fore.GREEN}{prefix}{Fore.RESET}
                                    Servers {Fore.MAGENTA}-{Fore.RESET} {Fore.GREEN}{servers}{Fore.RESET}
  
  ''')

@bot.command()
async def spam(ctx):
  if ctx.author.id == ID:
    
    for i in range(50):
      await ctx.send("Selfbot Made By Stealth")
      await asyncio.sleep(0.7)
  else:
    print('Someone tried to spam')

@bot.command()
async def guild_create(ctx, *, gname):
  if ctx.author.id == ID:
    
    headers = {
      'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
      'Content-Type': 'application/json',
      'Authorization': token,
    }
    request = requests.Session()
    guild = {
        'channels': None,
        'icon': None,
        'name': f"{gname}",
        'region': "europe"
    }

    p = requests.post('https://discordapp.com/api/v6/guilds', headers=headers, json=guild)

    if p.status_code == 201:
      await ctx.send(f'{gname} created.')
      
    elif "You are being rate limited." in p.text:
      await ctx.send('You are beign rate limited, please try again later.')

@bot.command()
async def nuke(ctx):
  if ctx.author.id == ID:
    
    for channel in ctx.guild.channels:
      await channel.delete()
    for user in list(ctx.guild.members):
      try:
        await user.kick()
      except:
        pass    
  else:
    print('Someone tried to nuke :P')

@bot.command()
async def checktoken(ctx, *, dtoken):
  checkone = {
      'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
      'Content-Type': 'application/json',
      'Authorization': dtoken,
    }
  request = requests.Session()
  checktwo = {
      'status': "dnd"
    }
  r = request.patch("https://discordapp.com/api/v6/users/@me/settings",headers=checkone, json=checktwo)
  if r.status_code == 200:
    await ctx.send('Token is valid.')
  if r.status_code == 401:
    await ctx.send('Token is invalid.')


bot.run(token, bot=False)
