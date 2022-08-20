import discord
from discord import app_commands
from discord.ext import commands

embed_color=0xff7f00

class ban(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        
    @app_commands.command(
        name="ban",
        description="Ban a member"
    )
    @app_commands.describe(user="The user you want to ban", reason="The reason you want to ban the user")
    @commands.has_permissions(ban_members=True)
    async def self(self, interaction: discord.Interaction, user: discord.User, reason:str=None):
        if reason==None:
            reason="No reason provided."
        await interaction.guild.ban(user)
        
async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        ban(bot),
        guild=discord.Object(id = 984165849868931122)
    )