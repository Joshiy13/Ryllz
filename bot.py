from tokenize import Token
from turtle import color
from unicodedata import name
import discord
from discord import guild, embeds, errors, utils
import asyncio
import os


token = os.getenv("TOKEN")
client = discord.Client()

help = discord.Embed(title="Help-List of Ryllz-Bot", description="Here is a list of commands", color=800080)
help.add_field(name="!help", value="Shows this page", inline=False)
help.add_field(name="!dev", value="Shows the Developer of this Bot", inline=False)
help.add_field(name="!ping", value="Shows the Latency of this Bot", inline=False)
help.add_field(name="!avatar", value="Shows your Avatar", inline=False)
help.add_field(name="!say", value="Sends a message trough the Bot", inline=False)
help.add_field(name="!code", value="Shows the Source Code to this Bot", inline=False)
help.add_field(name="!telldev", value="Pings the Dev of this Bot", inline=False)
help.add_field(name="!ban", value="Bans a User", inline=False)
help.add_field(name="!kick", value="Kicks a User", inline=False)


code = discord.Embed(title="Source Code:", description="https://github.com/Joshiy13/Ryllz", color=800080)

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
        await message.channel.send(embed=help)
    if message.content.startswith("!ping"):
        await message.channel.send(f"Pong! ({round(client.latency * 1000)}ms)")
    if message.content.startswith("!avatar"):
        await message.channel.send(f"{message.author.avatar_url}")
    if message.content.startswith("!say"):
        await message.channel.send(message.content[5:])
    if message.content.startswith("!telldev"):
        await message.channel.send(f"<@{dev}>" + " " + message.content[9:])
    if message.content.startswith("!code"):
        await message.channel.send(embed=code)
    if message.content.startswith("!ban"):
        if message.author.guild_permissions.ban_members:
            user = message.mentions[0]
            await user.ban()
            await message.channel.send(f"Banned {user.mention}")
    if message.content.startswuth("!unban"):
        if message.author.guild_permissions.ban_members:
            user = message.mentions[0]
            await user.unban()
            await message.channel.send(f"Unbanned {user.mention}")
    if message.content.startswith("!kick"):
        if message.author.guild_permissions.kick_members:
            user = message.mentions[0]
            await user.kick()
            await message.channel.send(f"Kicked {user.mention}")


client.run(token)