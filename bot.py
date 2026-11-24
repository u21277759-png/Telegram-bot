from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

BOT_TOKEN = "9129539104:AAHm42hIe43jyP72c3zRyzbA4uGc_YW9ups"
SECRET_KEY = "Lucky proxy"

async def check_key(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text.strip()
    if user_text.lower() == SECRET_KEY.lower():
        await update.message.reply_text("VALID")
    else:
        await update.message.reply_text("INVALID")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT, check_key))
app.run_polling()
