from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
import re

# 🔐 Токен от BotFather (временно в коде)
TOKEN = "7934050267:AAGteJFHVm1108ffap66G84dXIsVQUWSfUo"

# ❌ Плохие слова (можно расширить)
BAD_WORDS = ["мат1", "мат2", "плохое", "ругательство"]

# 🔗 Шаблон для поиска ссылок
URL_PATTERN = r"(http[s]?://|t\.me|telegram\.me|www\.)"

async def censor(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.text:
        text = update.message.text.lower()

        has_bad_word = any(word in text for word in BAD_WORDS)
        has_link = re.search(URL_PATTERN, text)

        if has_bad_word or has_link:
            try:
                await update.message.delete()
                print(f"Удалено: {update.message.text}")
            except Exception as e:
                print(f"Ошибка при удалении: {e}")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, censor))
    print("Бот запущен.")
    app.run_polling()

if __name__ == "__main__":
    main()
