from tokenize import Token
from turtle import color
from unicodedata import name
import discord
from discord import guild
import asyncio
import os


token = os.getenv("TOKEN")
client = discord.Client()

help = discord.Embed(title="Help-List of Ryllz-Bot", description="Here is a list of commands", color=0x00ff00)
help.add_field(name="!help", value="Shows this page", inline=False)
help.add_field(name="!dev", value="Shows the Developer of this Bot", inline=False)
help.add_field(name="!ping", value="Shows the Latency of this Bot", inline=False)
help.add_field(name="!avatar", value="Shows your Avatar", inline=False)
help.add_field(name="!say", value="Sends a message trough the Bot", inline=False)
help.add_field(name="!code", value="Shows the Source Code to this Bot", inline=False)
help.add_field(name="!telldev", value="Pings the Dev of this Bot", inline=False)

code = discord.Embed(title="Source Code", description="Here is the Source Code of this Bot", color=0x00ff00)
code.add_field(name="GitHub", value="https://github.com/Joshiy13/Ryllz", inline=False)

dev = 841613559870914580


@client.event 
async def on_ready():
    client.loop.create_task(status_task())
    print("Bot is ready!")
async def status_task():
    while True:
        await client.change_presence(activity=discord.Game("Coded by joshiy13#7277"), status=discord.Status.online)
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Game("https://discord.gg/PPjDtEYRnn"), status=discord.Status.online)
        await asyncio.sleep(10)


@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content.startswith("!help"):
        await message.channel.send(help)
    if message.content.startswith("!ping"):
        await message.channel.send(f"Pong! ({round(client.latency * 1000)}ms)")
    if message.content.startswith("!avatar"):
        await message.channel.send(f"{message.author.avatar_url}")
    if message.content.startswith("!say"):
        await message.channel.send(message.content[5:])
    if message.content.startswith("!telldev"):
        await message.channel.send(f"<@{dev}>")
    if message.content.startswith("!code"):
        await message.channel.send(code)


client.run(token)