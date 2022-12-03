from discord.ext import commands
import discord
import OpenAi
import os
import keep_alive

intents = discord.Intents().all()
client = commands.Bot(command_prefix="!", intents=intents)

BOT_TOKEN = os.getenv("BOT_TOKEN")


@client.event
async def on_ready():
    print("Bot is ready")


@client.command()
async def hello(ctx):
    await ctx.send("Hi")

responses = 0
list_user = []


@client.event
async def on_message(message):
    if message.channel.id == message.author.dm_channel.id:  # dm only
        # await message.channel.send('ping')
        chat_log = ""
        list_user.append(message.author.id)
        question = message.content
        answer = OpenAi.ask(question, chat_log)
        await message.channel.send(answer)


@client.command()
@commands.is_owner()
async def shutdown(context):
    exit()


keep_alive.keep_alive()
client.run(BOT_TOKEN)
