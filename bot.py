from tokenize import Token
from turtle import color
from unicodedata import name
import discord
from discord import guild, embeds, errors, utils
import asyncio
import os


token = os.getenv("TOKEN")
client = discord.Client()

help = discord.Embed(title="Help-List of Ryllz-Bot", description="", color=800080)
help.add_field(name="!help", value="Shows this page", inline=True)
help.add_field(name="!dev", value="Shows the Developer of this Bot", inline=True)
help.add_field(name="!ping", value="Shows the Latency of this Bot", inline=True)
help.add_field(name="!say", value="Sends a message trough the Bot", inline=True)
help.add_field(name="!code", value="Shows the Source Code to this Bot", inline=True)
help.add_field(name="!telldev", value="Pings the Dev of this Bot", inline=True)
help.add_field(name="!ban", value="Bans a User", inline=True)
help.add_field(name="!kick", value="Kicks a User", inline=True)
help.add_field(name="!userinfo", value="Shows infos about a user", inline=True)
help.add_field(name="!serverinfo", value="Shows infos about the Server", inline=True)


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
async def on_member_join(member):
    channel = client.get_channel(737008700230108416)
    await channel.send(f"Welcome {member.mention}! CAN I GET A HOYEAHHHH?!")
async def on_member_remove(member):
    channel = client.get_channel(737008700230108416)
    await channel.send(f"{member.mention} is not willing to give us a HOYEAHHHHH... Fuck you!")



@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content.startswith("!help"):
        await message.channel.send(embed=help)
    if message.content.startswith("!ping"):
        await message.channel.send(f"Pong! ({round(client.latency * 1000)}ms)")
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
            ban = discord.Embed(title="", description=f"Banned {user.mention}!", color=800080)
            await message.channel.send(embed=ban)  
    if message.content.startswith("!kick"):
        if message.author.guild_permissions.kick_members:
            user = message.mentions[0]
            await user.kick()
            kick = discord.Embed(title="", description=f"Kicked {user.mention}!", color=800080)
            await message.channel.send(embed=kick)
    if message.content.startswith("!userinfo"):
        user = message.mentions[0]
        userinfo = discord.Embed(title="", description=f"{user.name}#{user.discriminator}", color=800080)
        userinfo.set_thumbnail(url=user.avatar_url)
        userinfo.add_field(name="ID", value=user.id)
        userinfo.add_field(name="Created at", value=user.created_at)
        userinfo.add_field(name="Joined at", value=user.joined_at)
        userinfo.add_field(name="Roles", value=len(user.roles))
        await message.channel.send(embed=userinfo)
    if message.content.startswith("!guildinfo"):
        guild = message.guild
        guildinfo = discord.Embed(title="Name", description=f"{guild.name}", color=800080)
        guildinfo.set_thumbnail(url=guild.icon_url)
        guildinfo.add_field(name="ID", value=guild.id)
        guildinfo.add_field(name="Created at", value=guild.created_at)
        guildinfo.add_field(name="Members", value=guild.member_count)
        await message.channel.send(embed=guildinfo)
    if "Ryllz" in message.content:
        await message.channel.send("HOYEAHHHHH")
    if "Hypixel" in message.content:
        await message.channel.send("oeeeeeerrghggggg")




client.run(token)