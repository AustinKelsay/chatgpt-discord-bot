import discord
import codex
import os
import dotenv

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

dotenv.load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")


@client.event
async def on_ready():
    print("Bot is ready")


@client.event
async def on_message(message):
    # make sure the bot doesn't reply to itself
    if message.author == client.user:
        return
    # make sure this is a dm
    if message.guild is not None:
        return
    # make sure the message is not empty
    if message.content == "":
        return
    # make sure the message is not a command
    if message.content.startswith("!"):
        return
    answer = codex.ask(message.content)

    if answer:
        await message.channel.send(answer)


client.run(BOT_TOKEN)
