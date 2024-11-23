import discord
from discord import app_commands
from discord.ext import commands

import dotenv; from dotenv import load_env
import os; from os import getenv

load_env()
dToken = getenv("DISCORD_AUTH_TOKEN")

client = commands.Bot()

client.run(dToken)