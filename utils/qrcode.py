import discord
from discord.ext import commands
from discord import app_commands
from os import remove
import qrcode as qrcodecreator
from qrcode.constants import *
from PIL import Image, ImageOps, ImageDraw
import requests

class qrcode(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot=bot
    
    @app_commands.command(
        name="qrcode",
        description="Create a qrcode."
    )
    @app_commands.describe(value="Value of the qrcode to generate.")
    async def self(self, interaction: discord.Interaction, value: str):
        qr = qrcodecreator.QRCode(
            version=6,
            error_correction=ERROR_CORRECT_H,
            box_size=10,
            border=3
        )
        qr.add_data(value)
        qr.make(fit=True)

        qrcodeimage = qr.make_image(fill_color=(194, 124, 14), back_color="white")
        
        qrcodeimage.save("qrcode.png")

        # save des fichiers et tout
        
        avatar_image = str(interaction.user.avatar).split("=")
        avatar_image = avatar_image[0]+"=80"
        avatar_image = requests.get(avatar_image).content
        with open('image.png', 'wb') as image:
            image.write(avatar_image)
    
        mask = Image.open('mask.png').convert('L')
        im = Image.open('image.png')

        output = ImageOps.fit(im, mask.size, centering=(0.5, 0.5))
        output.putalpha(mask)

        print(qrcodeimage.size[1])
        
        draw = ImageDraw.Draw(qrcodeimage)
        
        x=output.size[1]-1
        x = qrcodeimage.size[1]//2 - x//2
        y=output.size[1]-1
        y = qrcodeimage.size[1]//2 + y//2

        draw.rectangle([(x, x), (y, y)], fill="white")

        back_qr=qrcodeimage.copy()
        back_qr.paste(output, ((x, x)), output)

        back_qr.save('new_image.png')
    
async def setup(bot: commands.Bot):
    await bot.add_cog(
        qrcode(bot),
        guild=discord.Object(id=984165849868931122)
    )