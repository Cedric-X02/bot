import discord
from discord.ext import commands
from discord import app_commands

class roleembedadd(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot=bot
        
    @app_commands.command(
        name="roleembedadd",
        description="Add a field to the role embed."
    )
    @app_commands.describe(
        role="Role to add.",
        description="Description of the role"
    )
    @commands.has_role(discord.Object(id=984332818081521724))
    async def self(self, interaction: discord.Interaction, role: discord.Role, description: str):
        with open("roleembed.txt", "r+") as file:
            content=file.read()
        open("roleembed.txt", "w").close()
        file = open("roleembed.txt", "w")
        file.write(f'{content}.add_field(title="{role.mention}", value="{description}")')
        file.close()
            
        await interaction.response.send_message("Terminé avec succès.")
        
async def setup(bot: commands.Bot):
    await bot.add_cog(
        roleembedadd(bot),
        guild=discord.Object(id=984165849868931122)
    )