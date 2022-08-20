from pydoc import describe
from typing import Optional
import discord
from discord.ext import commands
from discord import app_commands

class avatar(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @app_commands.command(
        name="avatar",
        description="Shows avatar of a user"
    )
    @app_commands.describe(user="The user you want to send the avatar to")
    async def self(self, interaction: discord.Interaction, user: Optional[discord.User]):
        if user == None:
            await interaction.response.send_message(embed=discord.Embed(color=discord.Color.dark_gold()).set_image(url=interaction.user.avatar).add_field(name="Here is your avatar", value=interaction.user.mention))
        else:
            await interaction.response.send_message(embed=discord.Embed(color=discord.Color.dark_gold()).set_image(url=user.avatar).add_field(name=f"Here is the avatar of", value=user.mention))
            
async def setup(bot: commands.Bot):
    await bot.add_cog(
        avatar(bot),
        guild=discord.Object(id=984165849868931122)
    )