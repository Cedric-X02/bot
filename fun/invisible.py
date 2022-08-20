from tkinter import Button
import clipboard
import discord
from discord.ext import commands
from discord import app_commands
from discord.ui import button, View, Button

class bouton(View):
    def __init__(self):
        super().__init__(timeout=None)
        
    @button(label="Copy", custom_id="copy", style=discord.ButtonStyle.green)
    async def copy(self, interaction: discord.Interaction, button:Button):
        clipboard.copy("\u200B")
        await interaction.response.send_message("Invisible caracter copied successfully !", ephemeral=True)

class invisible(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot=bot
        
    @app_commands.command(
        name="invisible",
        description="Sends an invisible caracter"
    )
    async def self(self, interaction:discord.Interaction):
        await interaction.response.send_message("\u200B", view=bouton())
        
async def setup(bot: commands.Bot):
    await bot.add_cog(
        invisible(bot),
        guild=discord.Object(id=984165849868931122)
    )