import ipaddress
import math
import discord
from discord import user
from discord.ext import commands
import random


client = commands.Bot(command_prefix = "")

@client.event
async def on_ready():
    print("THE BOIS")
    print("----------------------")


@client.command()
async def BOIS(ctx):
    await ctx.send("bot made by fondzz")



@client.command()
async def kids(ctx):
    await ctx.send("im a bot?")


@client.command()
async def  ban(ctx):
    await ctx.send("i can't ban")



@client.command()
async def whoareyou(ctx):
    await ctx.send("idk who am i?")


@client.command()
async def twomad(ctx):
    await ctx.send("waht")


@client.command()
async def bugs(ctx):
    await ctx.send("huh")


@client.command()
async def MEE6(ctx):
    await ctx.send("i ain't MEE6 bro")



@client.command()
async def hey(ctx):
    await ctx.send("what")



@client.command()
async def gg(ctx):
    await ctx.send("ez")


@client.command()
async def nword(ctx):
    await ctx.send("ayo that's racist")





@client.command()
async def whomadeyou(ctx):
    await ctx.send("twomad#1073")


@client.command()
async def hi(ctx):
    await ctx.send("hey")



@client.command()
async def howdy(ctx):
    await ctx.send("engineer?")



@client.command()
async def whatup(ctx):
    await ctx.send("the roof")



@client.command()
async def pog(ctx):
    await ctx.send("POG")


@client.command()
async def poggers(ctx):
    await ctx.send("POGGERS")



@client.command()
async def Poggers(ctx):
    await ctx.send("POGGERS")


@client.command()
async def Pog(ctx):
    await ctx.send("POG")




@client.command()
async def hello(ctx):
    await ctx.send("Hello")

@client.command()
async def Hello(ctx):
    await ctx.send("hey")


@client.command()
async def youtube(ctx):
    await ctx.send("https://www.youtube.com/channel/UCmwAtRymqcdu5t-Rnz-TkZQ")



@client.command()
async def fnaf(ctx):
    await ctx.send("five night at freddys")



@client.command()
async def fondzz(ctx):
    await ctx.send("DAD??")


@client.command()
async def cmds(ctx):
    await ctx.send("idk ")


@client.command()
async def num(ctx):
    await ctx.send("idk ")




@client.command()
async def kill(ctx):
    await ctx.send("ight the time has come ")

@client.command()
async def whatsyourname(ctx):
    await ctx.send("i'm a bot ")


@client.command()
async def w(ctx):
    await ctx.send("you good?")


@client.command()
async def cap(ctx):
    await ctx.send("nah")

@client.command()
async def broh(ctx):
    await ctx.send("you mean bruh?")



@client.command()
async def bruh(ctx):
    await ctx.send("BRUH")


@client.command()
async def capofSwit(ctx):
    await ctx.send("Bern")


@client.command()
async def howareyou(ctx):
    await ctx.send("im good")
    if howareyou:
        print("great")


@client.command()
async def yo(ctx):
    await ctx.send("YO")


@client.command()
async def s(ctx):
    await ctx.send("what?")


@client.command()
async def hlp(ctx):
    await ctx.send("ALL CMDS.kids ban whoareyou twomad bugs MEE6 hey gg nword whomadeyou hi howdy whatup pog poggers Poggers Pog hello Hello youtube fnaf fondzz")



@client.command()
async def stroke(ctx):
    await ctx.send("nice")


@client.command()
async def lostmytoes(ctx):
    await ctx.send("you know who else")

@client.command()
async def nice(ctx):
    await ctx.send("Kneecaps")


@client.command()
async def black(ctx):
    await ctx.send(" WAIT WHAT?")


@client.command()
async def fortnite(ctx):
    await ctx.send("EWWW?")


@client.command()
async def cod(ctx):
    await ctx.send("the game or the fish??")

@client.command()
async def fish(ctx):
    await ctx.send("damn nice")

@client.command()
async def thegame(ctx):
    await ctx.send("poggggggers")

@client.command()
async def hack(ctx):
    await ctx.send("HACKING INTO ACC. GG")

client.run('token')
