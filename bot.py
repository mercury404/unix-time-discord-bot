import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
token = os.environ["DISCORD_TOKEN"]
bot = commands.Bot(command_prefix="unix.")

@bot.event
async def on_ready():
    print("Ready!")

@bot.command()
async def end(ctx):
    await ctx.send("Unix time ends <t:2147483647:R> or on <t:2147483647>")

@bot.command()
async def start(ctx):
    await ctx.send("Unix time started <t:1:R> or on <t:1>")

@bot.command()
async def unix(ctx, arg):
    await ctx.send("That number in unix time: <t:"+arg+":R> or on <t:"+arg+">")

bot.run(token)
