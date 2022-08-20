from typing import Optional
import discord
from discord import app_commands
from discord.ext import commands
from discord.ui import TextInput, Modal
from os import listdir

class MyModal(Modal, title='Search'):
    search = TextInput(label='Search a query with google.', placeholder="Your search")

    async def on_submit(self, interaction: discord.Interaction):
        embed = discord.Embed(color=discord.Color.dark_gold())
        search=str(self.search)
        search=search.replace(" ", "+")
        embed.add_field(name="🔎Search🔍", value=f"https://google.com/search?q={search}", inline=True)
        await interaction.response.send_message(embed=embed)

class search(commands.Cog):
    def __init__(self, bot:commands.Bot) -> None:
         self.bot=bot
         
    @app_commands.command(
        name="search",
        description="Search a query with google."
    )
    @app_commands.describe(query="Search query")
    async def self(self, interaction: discord.Interaction, query: Optional[str] = None):
        if query == None:
            embed = discord.Embed(color=discord.Color.dark_gold())
            search=query.replace(" ", "+")
            embed.add_field(name="🔎Search🔍", value=f"https://google.com/search?q={search}", inline=True)
            await interaction.response.send_message(embed=embed)
        else:
            modal=MyModal()
            await interaction.response.send_modal(modal)

async def setup(bot):
    await bot.add_cog(
        search(bot),
        guild=discord.Object(id = 984165849868931122)
    )