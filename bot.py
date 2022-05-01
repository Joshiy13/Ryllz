from tokenize import Token
from turtle import color
from unicodedata import name
import discord
from discord import guild, embeds, commands
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
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please pass in all requirements :rolling_eyes:.')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You dont have all the requirements :angry:")

#The below code bans player.
@client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)

#The below code unbans player.
@client.command()
@commands.has_permissions(administrator = True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return


#The below code kicks player.
@client.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, member : discord.Member, *, reason = None):
    await member.kick(reason = reason)
    

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



client.run(token)