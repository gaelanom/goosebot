# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Import required packages
import discord
from discord.ext import commands

import os
from dotenv import load_dotenv

import goose_bot_utils

# Load the bot token

load_dotenv('environment.env')
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Set up constants
GOOSE_BOT_COMMAND_PREFIX = '.'
GOOSE_BOT_DESCRIPTION = "A bot for basic server utilities."

# Set up required intents
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.members = True

# Initialize the client
client = discord.Client()

# Initialize the bot
goose_bot = commands.Bot(command_prefix=GOOSE_BOT_COMMAND_PREFIX, description=GOOSE_BOT_DESCRIPTION, intents=intents)


# Log readiness
@goose_bot.event
async def on_ready():
    print('Logged in as ' + goose_bot.user.name)
    print(goose_bot.user.id)
    print('------')


# Roll a die
@goose_bot.command()
async def roll(ctx, dice: str):
    print("Rolling dice...")
    """Roll dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except (Exception,):
        await ctx.send('Format has to be NdN!')
        return
    result = await goose_bot_utils.roll_result(limit, rolls)

    await ctx.send(result)


# List the roles of the server and the command author.
@goose_bot.command()
async def roles(ctx):
    server_roles = ctx.author.guild.roles
    prettified_member_roles = await goose_bot_utils.prettify_roles(ctx.author.roles, "Your roles:")
    prettified_server_roles = await goose_bot_utils.prettify_roles(server_roles, "All roles:")
    await ctx.send(prettified_server_roles)
    await ctx.send(prettified_member_roles)


# Add the desired role to the command author or a specific user.
@goose_bot.command()
async def role(ctx, role_name: discord.Role = "", user_name: discord.Member = "author"):
    if role_name == "":
        await ctx.send("Specify a role to add or remove.")
    else:
        if user_name == "author":
            if role_name in ctx.author.roles:
                await ctx.author.remove_roles(role_name)
                await ctx.send("Relieved you of the role `" + role_name.name + "`.")
            else:
                await ctx.author.add_roles(role_name)
                await ctx.send("Granted you the role `" + role_name.name + "`.")
        else:
            if role_name in user_name.roles:
                await ctx.author.remove_roles(role_name)
                await ctx.send("Removed `" + role_name.name + "` from " + user_name.display_name + ".")
            else:
                await ctx.author.add_roles(role_name)
                await ctx.send("Granted `" + role_name.name + "` to " + user_name.display_name + ".")


goose_bot.run(BOT_TOKEN)
