import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv
from os import getenv

load_dotenv("...")
BOT_AUTHOR_ID = getenv("BOT_AUTHOR_ID")

class creator(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        
    @app_commands.command(
        name="creator",
        description="Shows the creator of this bot"
    )
    async def self(self, interaction: discord.Interaction):
        embed=discord.Embed(title="The creator of this bot is...", description=f"... <@"+BOT_AUTHOR_ID+"> !", color=discord.Colour.random())
        await interaction.response.send_message(embed=embed)
        
async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        creator(bot),
        guild=discord.Object(id = 984165849868931122)
    )