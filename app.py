from telegram.ext import ApplicationBuilder, CommandHandler

import os

# توکن رو از متغیر محیطی بگیر (در Railway هم همینو تعریف می‌کنی)
BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update, context):
    await update.message.reply_text("سلام! ربات با موفقیت ران شد.")

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("ربات فعال شد...")
    app.run_polling()
