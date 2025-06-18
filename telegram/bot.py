import os
from dotenv import load_dotenv
load_dotenv()

import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

API_URL = os.getenv('API_ENDPOINT')
BOT_TOKEN = os.getenv('BOT_TOKEN')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    data = {
        'user_id' : user.id,
        'username': user.username if user.username else user.first_name or None
    }
    try:
        res = requests.post(API_URL, json=data)
        print(res.json())
    except Exception as e:
        print("Error sending to Django:", e)

    await update.message.reply_text(f"Welcome {user.first_name}!")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
