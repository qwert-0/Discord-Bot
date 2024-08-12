import discord
from discord import client
from discord import message
from discord.ext import commands
from discord.ext.commands import cog
from discord.ext.commands.cog import Cog
from gtts import gTTS, tts
import pandas as pd
import os


class textToSpeech(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def tts(self, ctx, message):
        data = pd.DataFrame(columns=['content', 'time', 'author'])
        if (ctx.voice_client):
            if len(message.content) == 0:
                return False
            else:
                data = data.append({'content': message.content, 'time': message.created_at,
                                   'author': message.author.name}, ignore_index=True)
                language = 'en'
                output = gTTS(text=data, lang=language, slow=False)
                output.save("voice.mp3")
                os.system("start voice.mp3")


def setup(client):
    client.add_cog(tts(client))
