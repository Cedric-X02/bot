import discord
from discord.ext import commands
from discord  import app_commands

class calc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @app_commands.command(
        name="calc",
        description="Calculate an operation"
    )
    @app_commands.describe(
        operation="The operation to calculate"
    )
    async def self(self, interaction: discord.Interaction, operation: str):
        try:
            result=eval(operation)
            await interaction.response.send_message(f"`{operation}` > `{result}`")
        except:
            await interaction.response.send_message(f"I can't calculate your operation(`{operation}`).")
            
async def setup(bot: commands.Bot):
    await bot.add_cog(
        calc(bot),
        guild=discord.Object(id=984165849868931122)
    )