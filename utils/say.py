from typing import Optional
import discord
from discord.ext import commands
from discord import app_commands

class say(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot=bot
        
    @app_commands.command(
        name="say",
        description="Send a message with the identity of the bot."
    )
    @app_commands.describe(text="Texte to send")
    async def self(self, interaction: discord.Interaction, text: str):
        await interaction.response.send_message(f"`{interaction.user.name}#{interaction.user.discriminator}` > {text}")
        
async def setup(bot: commands.Bot):
    await bot.add_cog(
        say(bot),
        guild=discord.Object(id=984165849868931122)
    )