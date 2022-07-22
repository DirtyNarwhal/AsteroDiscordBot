// Require the necessary discord.js classes
const { Client, GatewayIntentBits, Partials } = require('discord.js');
const { ApplicationCommandType, ApplicationCommandOptionType } = require('discord.js');
const { BOT_TOKEN } = require('./config.json');

// Create a new client instance
const client = new Client({ intents: [GatewayIntentBits.Guilds], partials: [Partials.Channel] });
// When the client is ready, run this code (only once)
client.once('ready', () => {
	console.log('Ready!');
});

//Listen for commands:
client.on('interactionCreate', async interaction => {
	if (!interaction.type === InteractionType.ApplicationCommand) return;

	const { commandName } = interaction;

	if (commandName === 'ping') {
		await interaction.reply('Pong!');
	} else if (commandName === 'server') {
		await interaction.reply('Server info.');
	} else if (commandName === 'user') {
		await interaction.reply('User info.');
	}
});
// Login to Discord with the client's token
client.login(BOT_TOKEN);
