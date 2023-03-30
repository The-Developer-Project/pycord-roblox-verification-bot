import discord
from discord import option
from replit import db
from discord.ext import commands
import keepalive
import os, requests
import traceback
keepalive.keep_alive()

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix='+', intents=intents)

@bot.slash_command(name="verify", description="use THIS command to verify roblox account")
async def verify2(ctx, code):
    arg = code
    try:
        key = arg + '+temp'
        rname = db[key]
        dname = ctx.author.id
        db[rname] = str(dname)
        key2 = str(dname) + '+rbx'
        db[key2] = rname
        del db[key]
        r = requests.get(f'https://users.roblox.com/v1/users/{rname}')
        roname = r.json()['name']
        await ctx.respond("Successfully Connected to " + roname)
        guild = bot.get_guild(939026663629525022)
        role = discord.utils.get(guild.roles, name="Verified")
        await ctx.author.add_roles(role)
    except Exception as e:
        await ctx.respond(e.message + ' ' + e.args)

discordkey = os.environ['discordkey']
try:
    bot.run(discordkey)
except:
    os.system("kill 1")
