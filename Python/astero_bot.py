import discord
import astero_config
import logging
from discord.ext import commands

print(discord.__version__)
logging.basicConfig(level=logging.INFO)

class AsteroBot(discord.Client):
    async def on_ready(self):
        print("Ready!")

    async def on_message(self,message):
        if message.author.id == self.user.id:
            return
        if message.content.startswith('hello'):
            await message.reply('Hello there monka!!', mention_author=True)

        if message.content.startswith('congrats'):
            await message.reply('yay!', mention_author=False)



### ---- Intents ---- ###
intents = discord.Intents.default()
intents.members = True

### ---- Initialize bot ---- ###
client = AsteroBot(intents=intents)
client.run(astero_config.key)