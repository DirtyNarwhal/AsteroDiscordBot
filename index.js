// Require the necessary discord.js classes
const { Client, GatewayIntentBits, Partials } = require('discord.js');
const { BOT_TOKEN } = require('./config.json');

// Create a new client instance
const client = new Client({ intents: [GatewayIntentBits.Guilds], partials: [Partials.Channel] });
// When the client is ready, run this code (only once)
client.once('ready', () => {
	console.log('Ready!');
});

// Login to Discord with the client's token
client.login(BOT_TOKEN);
