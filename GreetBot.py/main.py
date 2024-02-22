import discord
from discord.ext import commands
from typing import Final
import os
from discord import Intents, Client, File
from easy_pil import Editor, load_image_async, Font

bot = commands.Bot(command_prefix='>', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'{bot.user} is now running!')

@bot.event
async def on_member_join(member):

    channel = member.guild.system_channel

    background = Editor("GreetBot.py\pic1.jpg")
    profile_image = await load_image_async(str(member.avatar.url))

    profile = Editor(profile_image).resize((1200,1200)).circle_image()
    poppins = Font.poppins(size=200, variant="bold")
    poppins_small = Font.poppins(size=100, variant="light")

    background.paste(profile, (1175,150))

    background.text((1775,1350), f"llego un/a gei al server!", color="white", font=poppins, align='center')
    background.text((1775,1600), f"{member.name}#{member.discriminator}", color="white", font = poppins_small, align='center')

    file = File(fp=background.image_bytes, filename="GreetBot.py\pic1.jpg")
    await channel.send(f"llego un/a gei {member.mention}!")
    await channel.send(file=file)

@bot.event
async def on_member_leave(member):

    channel = member.guild.system_channel

    background = Editor("GreetBot.py\pic1.jpg")
    profile_image = await load_image_async(str(member.avatar.url))

    profile = Editor(profile_image).resize((1200,1200)).circle_image()
    poppins = Font.poppins(size=200, variant="bold")
    poppins_small = Font.poppins(size=100, variant="light")

    background.paste(profile, (1175,150))

    background.text((1775,1350), f"se fue un/a gei del server", color="white", font=poppins, align='center')
    background.text((1775,1600), f"{member.name}#{member.discriminator}", color="white", font = poppins_small, align='center')

    file = File(fp=background.image_bytes, filename="GreetBot.py\pic1.jpg")
    await channel.send(f"llego un/a gei {member.mention}!")
    await channel.send(file=file)

bot.run("MTIxMDA3MzQ4MDY3MDc0NDYxNg.G_Qq_V.mQO059SEPBHRKgLlTmuwoDb6cJ3kYKNi99kFCc")
