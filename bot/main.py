import discord 
from discord.ext import commands
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time 
import requests

bot = commands.Bot(command_prefix= '.', self_bot = True)
gods = [ur discord id]
token = "token here "



@bot.event
async def on_ready():
    print("Loaded")

@bot.command()
async def graph(ctx):
 if ctx.author.id in gods:
    options = Options()
    options.add_argument( "--headless" )
    driver = webdriver.Firefox(options=options, executable_path="gecko drive path")
    driver.get('https://2b2t.io/')
    time.sleep(2)
    driver.save_screenshot('test.png')
    driver.quit()
    file = discord.File("test.png")
    embed = discord.Embed(title="2B2T Queue Graph", url="https://2b2t.io/", description="test", color=0x000)
    embed.set_image(url="attachment://test.png")
    await ctx.send(embed=embed, file=file)

@bot.command()
async def stats (ctx, player):
 if ctx.author.id in gods:
    r = requests.get(f'https://api.2b2t.dev/stats?username={player}')
    embed = discord.Embed(title="2B2T", description="Stats", color=0x000)
    embed.set_image(url=f'https://minecraftskinstealer.com/api/v1/skin/render/fullbody/{player}/700')
    embed.add_field(name="ID", value=r.json()[0]['id'], )
    embed.add_field(name="username", value=r.json()[0]['username'], )
    embed.add_field(name="uuid", value=r.json()[0]['uuid'], )
    embed.add_field(name="kills", value=r.json()[0]['kills'], )
    embed.add_field(name="deaths", value=r.json()[0]['deaths'], )
    embed.add_field(name="joins", value=r.json()[0]['joins'], inline=True)
    embed.add_field(name="leaves", value=r.json()[0]['leaves'], inline=True)
    embed.add_field(name="adminlevel", value=r.json()[0]['adminlevel'], inline=True)

    # embed.set_footer(text="Developed by tWIX")
    # embed.set_thumbnail(url= 'https://cdn.discordapp.com/attachments/796057406505353229/796105496946802708/Screenshot_55.png')

    await ctx.channel.send(embed=embed)


@bot.command()
async def seen (ctx, player):
 if ctx.author.id in gods:
    r = requests.get(f'https://api.2b2t.dev/seen?username={player}')
    embed = discord.Embed(title="2B2T", description="Stats", color=0x000)
    embed.set_image(url=f'https://minecraftskinstealer.com/api/v1/skin/render/fullbody/{player}/700')
    embed.add_field(name="seen", value=r.json()[0]['seen'], )
    await ctx.channel.send(embed=embed)


@bot.command()
async def status (ctx, ):
 if ctx.author.id in gods:
    r = requests.get(f'https://api.2b2t.dev/status')
    embed = discord.Embed(title="2B2T", description="Status", color=0x000)
    embed.add_field(name="TPS", value=r.json()[0][0], )
    embed.add_field(name="Players", value=r.json()[0][1], )
    embed.add_field(name="Uptime", value=r.json()[0][3], )
    embed.set_image(url= 'https://tab.2b2t.dev/')
    await ctx.channel.send(embed=embed)



@bot.command()
async def prioq (ctx):
 if ctx.author.id in gods:
    r = requests.get(f'https://api.2b2t.dev/prioq')
    embed = discord.Embed(title="2B2T", description="Priority Queue", color=0x000)
    embed.add_field(name="Queue", value=r.json()[1], )
    embed.add_field(name="Wait time", value=r.json()[2], )
    await ctx.channel.send(embed=embed)

@bot.command()
async def q (ctx):
 if ctx.author.id in gods:
    r = requests.get(f'https://2b2t.io/api/queue')
    embed = discord.Embed(title="2B2T", description="Queue", color=0x000)
    embed.add_field(name="Queue", value=r.json()[0][1], )
    await ctx.channel.send(embed=embed)


bot.run(token, bot = False)