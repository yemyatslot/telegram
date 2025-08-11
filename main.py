import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Get token from environment variable
TELEGRAM_TOKEN = os.getenv("7965313840:AAFy_gGeS7tk9n9ObfpMiJAKLmJKZ8oC9hU")

# Command: /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I am your reply bot. Send me any message!")

# Reply to all text messages
async def reply_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    reply_message = f"You said: {user_message}\n\nThis is an auto-reply!"
    await update.message.reply_text(reply_message)

def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_text))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
