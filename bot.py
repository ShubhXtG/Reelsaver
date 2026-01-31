from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import requests

# ⚠️ User provided token (replace later for safety)
BOT_TOKEN = "8542334527:AAEMdJ4GQLaF4fF8VfYIgwZEdISHUlDKjwk"

API = "https://saveig.app/api/ajaxSearch?url="

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Send me any Instagram Reel link 👇")

async def reel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text.strip()

    # invalid link check
    if "instagram.com" not in url:
        await update.message.reply_text("❌ Please send a valid Instagram Reel link.")
        return

    try:
        # API call
        r = requests.get(API + url).json()

        # direct MP4 reel link
