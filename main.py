import discord
import os

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print("Bot is alive!")
    print(f"🤖 Logged in as {bot.user}")

bot.run(TOKEN)
