import discord
from discord import app_commands
from discord.ext import commands

embed_color=0xff7f00

class server_info(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        
    @app_commands.command(
        name="server-info",
        description="Shows the server infos"
    )
    async def self(self, interaction: discord.Interaction):
        server=interaction.guild
        tc=len(server.text_channels)
        vc=len(server.voice_channels)
        desc=server.description
        nbmembers=server.member_count
        srvname=server.name
        embed=discord.Embed(title="Server-Infos", description="Under this message you can view the server infos.", color=embed_color)
        embed.add_field(name="Server Name", value=srvname, inline=True)
        embed.add_field(name="Server Description", value=desc, inline=True)
        embed.add_field(name="Member Count", value=nbmembers, inline=True)
        embed.add_field(name="Number of Text Channels", value=tc, inline=True)
        embed.add_field(name="Number of Voice Channels", value=vc, inline=True)
        await interaction.response.send_message(embed=embed)
        
async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        server_info(bot),
        guild=discord.Object(id = 984165849868931122)
    )