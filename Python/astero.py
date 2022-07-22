import astero_config
import discord
from discord.ext import commands, tasks


class AsteroBot(commands.Cog):
	def __init__(self,client):
		self.client = client

	@commands.command()
	def setup(self,ctx):
		self.client.loop.create_task(self.play_new(ctx))


	async def on_ready():
		print("We have logged in as {0.user}".format(client))


def setup(client):
    client.add_cog(AsteroBot(client))

cogs = [AsteroBot]
intents = discord.Intents.all()
intents.voice_states = True
client = commands.Bot(command_prefix='~', intents = intents)

for i in range(len(cogs)):
    cogs[i].setup(client)

client.run(astero_config.key)





'''
intents = discord.Intents.default()
intents.members = True""

client = discord.Client(intents : intents)


@client.event
#async function requires callbacks, and it is non-blocking in the sense that the main application thread will move on to the next line and comes back to the callback context after completion
#the main thread will wait on sync function to finish before moving on
async def on_ready():
	print('We have logged in as {0.user}'.format(client))

client.run(astero_config.key)
'''
