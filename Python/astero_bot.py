### ---- Imports and Logger configuration ---- ###
import discord
import logging
import astero_config
from discord.ext import commands
print(discord.__version__)
#Prints logs from Discord into the terminal.
logging.basicConfig(level=logging.INFO)

### ---- The bot class ---- ###
class AsteroBot(discord.Client):
    #Print "ready" when connection with Discord is established.
    async def on_ready(self):
        print("Ready!")
    #Check for messages and respond accordingly.
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