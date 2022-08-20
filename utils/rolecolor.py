import discord
from discord.ext import commands
from discord import app_commands

class rolecolor(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot=bot
        
    @app_commands.command(
        name="rolecolor",
        description="Change the color of a role."
    )
    @app_commands.describe(
        role="The role",
        color="The color of the role"
    )
    async def self(self, interaction: discord.Interaction, role: discord.Role, color: str):
        try:
            rgb=tuple(int(color.lstrip("#")[i:i+2], 16) for i in (0, 2, 4))
            await interaction.response.send_message(f"The color of the role {role.mention} as now {color}.", ephemeral=True)
            await role.edit(color=discord.Color.from_rgb(rgb[0], rgb[1], rgb[2]))
        except:
            await interaction.response.send_message(f"The color `{color}` is not an hex color.\nExample of hex color: `#a52222`")
        
async def setup(bot: commands.Bot):
    await bot.add_cog(
        rolecolor(bot),
        guild=discord.Object(id=984165849868931122)
    )