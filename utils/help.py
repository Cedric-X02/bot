import discord
from discord import app_commands
from discord.ext import commands

embed_color=0xff7f00

em1 = discord.Embed(color=discord.Color.gold())
em1.add_field(name="<:mod:1009257872380665948> Moderation - The moderation help menu", value=">>> **kick:** Kick a member of the server.\n**ban:** Ban a member of the server.", inline=True)

em2 = discord.Embed(color=discord.Color.gold())
em2.add_field(name="<:tools:1009257246846361711> Utils - The utils help menu", value=">>> **help:** Shows this menu.\n**creator:** Shows the creator of the bot.\n**server-info:** Shows the server info.\n**avatar:** Shows avatar of a user.\n**say:** Send a message with the identity of the bot.\n**qrcode:** Generate a QRCode.\n**embed:** Generate an embed\n**search:** Search a query with google.", inline=True)

options=[
            discord.SelectOption(label="Moderation",emoji="<:mod:1009257872380665948>",description="Shows the moderation help menu", default=True),
            discord.SelectOption(label="Utils",emoji="<:tools:1009257246846361711>",description="Shows the utils help menu")
            ]

class Select(discord.ui.Select):
    def __init__(self):
        options=options
        super().__init__(max_values=1,min_values=1,options=options)
    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == "Moderation":
            await interaction.response.edit_message(embed=em1, view=SelectView1())
        elif self.values[0] == "Utils":
            await interaction.response.edit_message(embed=em2, view=SelectView2())
            
class SelectView(discord.ui.View):
    def __init__(self, *, timeout = 180):
        super().__init__(timeout=timeout)
        self.add_item(Select())
        
class Select1(discord.ui.Select):
    def __init__(self):
        options=options
        super().__init__(max_values=1,min_values=1,options=options)
    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == "Moderation":
            await interaction.response.edit_message(embed=em1, view=SelectView1())
        elif self.values[0] == "Utils":
            await interaction.response.edit_message(embed=em2, view=SelectView2())
            
class SelectView1(discord.ui.View):
    def __init__(self, *, timeout = 180):
        super().__init__(timeout=timeout)
        self.add_item(Select1())

class Select2(discord.ui.Select):
    def __init__(self):
        options=options
        super().__init__(max_values=1,min_values=1,options=options)
    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == "Moderation":
            await interaction.response.edit_message(embed=em1, view=SelectView1())
        elif self.values[0] == "Utils":
            await interaction.response.edit_message(embed=em2, view=SelectView2())
            
class SelectView2(discord.ui.View):
    def __init__(self, *, timeout = 180):
        super().__init__(timeout=timeout)
        self.add_item(Select2())

class help(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        
    @app_commands.command(
        name="help",
        description="Shows the help menu"
    )
    async def self(self, interaction: discord.Interaction):
        await interaction.response.send_message(embed=discord.Embed(title="J'attends votre réponse..."), view=SelectView())
        
async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        help(bot),
        guild=discord.Object(id = 984165849868931122)
    )