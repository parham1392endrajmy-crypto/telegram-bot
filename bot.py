from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "توکن_خودت_اینجا"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام 👋 به فروشگاه کانفیگ خوش اومدی!")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("ربات روشن شد...")
app.run_polling()
