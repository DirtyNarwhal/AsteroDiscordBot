### ---- Imports and Logger configuration ---- ###
import discord
import logging
import astero_config
import random
from discord.ext import commands, tasks

### ---- Useful information & logging. ---- ###
print(f"\n-------------------------------\nDiscord Version {discord.__version__}\n-------------------------------")
#Prints logs from Discord into the terminal.
logging.basicConfig(level=logging.INFO)

### ------------------------------- The bot class ------------------------------- ###
class AsteroBot(commands.Bot):
    #Print "ready" when connection with Discord is established
    async def on_ready(self):
        print(f"\n-------------------------------\n{bot.user.name} #{bot.user.id} is ready!\n-------------------------------")

        @bot.command(name="choose")
        async def choice(ctx, *choices):
            await ctx.send(random.choice(choices))

        @bot.command(name="author")
        async def author(ctx):
            await ctx.send(ctx.author)

        @bot.command(name="greet")
        async def greet_me(ctx):
            await ctx.send("Hello!")

        @bot.command(name="join")
        async def join_channel(ctx):
            voice_client = ctx.voice_client
            if not ctx.message.author.voice:
                await ctx.send("You are not connected to a voice channel. Join one and try again.")
                return
            elif voice_client and voice_client.is_connected():
                await ctx.send(f"Already connected to #{voice_client.channel}.", mention_author=True)
                await ctx.message.add_reaction('\N{WHITE EXCLAMATION MARK ORNAMENT}')
                return
            else:
                channel = ctx.message.author.voice.channel
                await channel.connect()
                await ctx.message.add_reaction('✅')

        @bot.command(name="leave")
        async def leave_channel(ctx):
            voice_client = ctx.voice_client
            if voice_client and voice_client.is_connected():
                await voice_client.disconnect()
                await ctx.message.add_reaction('✅')
            else:
                await ctx.send("Currently not in any voice channel. Type ' ;join ' to summon.")
                await ctx.message.add_reaction("⛔")
                

### ---- Intents ---- ###
intents = discord.Intents.all()
intents.members = True

### ---- Initialize bot ---- ###
bot = AsteroBot(command_prefix=';')
bot.run(astero_config.key)
