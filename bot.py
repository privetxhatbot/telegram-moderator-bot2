import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("BOT_TOKEN")
BAD_WORDS = ["мат1", "мат2", "плохое", "ругательство"]

async def censor(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.text:
        text = update.message.text.lower()
        if any(word in text for word in BAD_WORDS):
            try:
                await update.message.delete()
            except Exception as e:
                print(f"Ошибка: {e}")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, censor))
    print("Бот работает.")
    app.run_polling()

if __name__ == "__main__":
    main()
