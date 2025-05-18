import telebot
from telebot import types

TOKEN = '8009662996:AAE--kt4q_cEfp17-SPuAkeYndKFspi0QpMا'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("📲 هک تلگرام", "📞 هک واتساپ")
    markup.row("📷 هک اینستا", "🎮 هک روبیکا")
    markup.row("🧑‍💻 پشتیبانی", "🔗 دعوت دوستان")
    bot.send_message(message.chat.id, "سلام خوش اومدی به ربات «هک‌بمر»", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_all(message):
    chat_id = message.chat.id
    if message.text == "📲 هک تلگرام":
        bot.send_message(chat_id, "♨️قیمت هک تلگرام: 850,000 تومان می‌باشد.\n❇️ابتدا مبلغ 150,000 تومان را واریز کنید.\n🔰در صورت تایید روی دکمه زیر بزنید:")
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("موافقم", callback_data="agree_telegram"))
        bot.send_message(chat_id, "آیا مایل به ادامه هستید؟", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "agree_telegram")
def process_agreement(call):
    bot.send_message(call.message.chat.id, "✅مبلغ 150,000 تومان را به کارت زیر واریز کنید و عکس رسید را ارسال کنید:\n6037 9915 4749 9222\nبه نام جواد عباسی")

bot.infinity_polling()
