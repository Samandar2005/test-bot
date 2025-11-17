from telebot import types
from bot import bot
from config import REQUIRED_CHANNELS
from database import add_user
from keyboards import channels_keyboard, main_menu

def check_subscription(user_id):
    for channel in REQUIRED_CHANNELS:
        try:
            member = bot.get_chat_member(channel, user_id)
            if member.status not in ["member", "administrator", "creator"]:
                return False
        except:
            return False
    return True


@bot.message_handler(commands=['start'])
def start(message):
    add_user(message.from_user.id)
    bot.send_message(
        message.chat.id,
        "👋 Salom!\nQuyidagi kanallarga obuna bo‘ling va so‘ngra tekshiring:",
        reply_markup=channels_keyboard()
    )


@bot.callback_query_handler(func=lambda call: call.data == "check_subs")
def check_subs(call):
    user_id = call.from_user.id
    if check_subscription(user_id):
        bot.edit_message_text(
            "🎉 Obuna tasdiqlandi! Endi botdan foydalanishingiz mumkin.",
            call.message.chat.id,
            call.message.message_id,
            reply_markup=main_menu()
        )
    else:
        bot.answer_callback_query(call.id, "❌ Hali barcha kanallarga obuna qilmagansiz!", show_alert=True)
        bot.edit_message_text(
            "❌ Siz hali barcha kanallarga obuna qilmagansiz. Iltimos, obuna bo‘ling va qayta tekshiring:",
            call.message.chat.id,
            call.message.message_id,
            reply_markup=channels_keyboard()
        )