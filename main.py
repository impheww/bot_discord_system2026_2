import discord
from flask import Flask
import os
import threading

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = discord.Client(intents=intents)

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is alive!"

def run_web():
    app.run(host="0.0.0.0", port=10000)

@bot.event
async def on_ready():
    print(f"🤖 Logged in as {bot.user}")

# รันเว็บใน thread แยก
threading.Thread(target=run_web).start()

# รันบอท
bot.run(TOKEN)
