from typing import Optional
import discord
from discord.ext import commands
from discord import app_commands

class embed(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @app_commands.command(
        name="embed",
        description="Generate an embed."
    )
    @app_commands.describe(
        title="Title of the embed.",
        description="Description of the embed."
    )
    async def self(self, interaction: discord.Interaction, title: str, description: Optional[str]=None):
        if description==None:
            await interaction.response.send_message(embed=discord.Embed(title=title, color=discord.Color.dark_gold()).set_footer(icon_url=interaction.guild.icon, text=interaction.guild.name))
        else:
            await interaction.response.send_message(embed=discord.Embed(title=title, description=description,color=discord.Color.dark_gold()).set_footer(icon_url=interaction.guild.icon, text=interaction.guild.name))
            
async def setup(bot: commands.Bot):
    await bot.add_cog(
        embed(bot),
        guild=discord.Object(id=984165849868931122)
    )