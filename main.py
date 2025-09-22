import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
import openai

# Muhit o'zgaruvchilarini olish
TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_KEY = os.getenv("OPENAI_API_KEY")

openai.api_key = OPENAI_KEY

# /start komandasi
async def start(update: Update, context):
    await update.message.reply_text(
        "Salom! 👋 Men English Talk Bot 🤖\n"
        "Matn yozing yoki savol bering, men grammatikani va talaffuzni tekshirib beraman."
    )

# Oddiy xabarlarni qayta ishlash
async def handle_message(update: Update, context):
    user_text = update.message.text
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Correct this English sentence and explain mistakes:\n{user_text}",
        max_tokens=150
    )
    reply = response.choices[0].text.strip()
    await update.message.reply_text(reply)

# Asosiy funksiya
def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()

if__ name__ == "__main__":
    main()
