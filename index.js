// Require the necessary discord.js classes
const { Client, Events, GatewayIntentBits } = require('discord.js');
const { joinVoiceChannel, createAudioPlayer, createAudioResource, entersState, VoiceConnectionStatus, getVoiceConnection } = require('@discordjs/voice');
const { token } = require('./config.json');
const prefix = '!';
const notInVCMessage = 'hey bozo you arent in a vc';
const notInVc = 'im not in a vc + ratio';
const notPlaying = 'im not even playing audio ya cunt + bozo + l + ratio';
// Create a new client instance
const client = new Client({ intents: [
    GatewayIntentBits.Guilds,
    GatewayIntentBits.GuildMessages,
    GatewayIntentBits.MessageContent,
    GatewayIntentBits.GuildMembers,
    GatewayIntentBits.GuildVoiceStates,
] });

async function connectToChannel(channel) {
    const connection = joinVoiceChannel({
        channelId: channel.id,
        guildId: channel.guild.id,
        adapterCreator: channel.guild.voiceAdapterCreator,
        selfDeaf: false,
        selfMute: false,
    });

    try {
		await entersState(connection, VoiceConnectionStatus.Ready, 30e3);
		return connection;
	} catch (error) {
		connection.destroy();
		throw error;
	}
}

async function audioCommandHandler(command, connection, player) {
    try {
        player.play(createAudioResource(`./audio/${command}.wav`));
        connection.subscribe(player);
    } catch (error) {
        console.error(error);
    }
}

// When the client is ready, run this code (only once)
// We use 'c' for the event parameter to keep it separate from the already defined 'client'
client.once(Events.ClientReady, c => {
	console.log(`Ready! Logged in as ${c.user.tag}`);
});


client.on(Events.MessageCreate, async message => {
    console.log(message.content);
    if (!message.content.startsWith(prefix) || message.author.bot) return;
    const preProcess = message.content.slice(prefix.length).split(/ + /);
    const preProceess0 = preProcess.shift().toLowerCase();
    const messageArray = preProceess0.split(' ');
    const command = messageArray[0];
    const connection = getVoiceConnection(message.guild.id);
    const channel = message.member.voice.channel;
    const player = createAudioPlayer();
    if (connection) {
        audioCommandHandler(command, connection, player);
    } else if (command !== 'join') {
        await message.reply(notInVc);
    }
    switch (command) {
        case 'join':
            if (channel) {
                try {
                    await connectToChannel(channel);
                    // Plays the first audio
                    const preConnection = getVoiceConnection(message.guild.id);
                    const prePlayer = createAudioPlayer();
                    prePlayer.play(createAudioResource('./audio/here.wav'));
                    preConnection.subscribe(prePlayer);
                } catch (error) {
                    console.error(error);
                }
            } else {
                await message.reply(notInVCMessage);
            }
            break;
        case 'leave':
            if (connection) {
                try {
                    player.play(createAudioResource('./audio/goner.wav'));
                    connection.subscribe(player);
                    setTimeout(() => connection.destroy(), 1_500);
                } catch (error) {
                    console.error(error);
                }
            } else {
                await message.reply(notInVc);
            }
            break;
        case 'stop':
            if (player) {
                player.stop();
            } else {
                await message.reply(notPlaying);
            }
            break;
    }
});

// Log in to Discord with your client's token
client.login(token);
