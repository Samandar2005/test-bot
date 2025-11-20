import logging
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
                logging.info("User %s is not subscribed to %s (status=%s)", user_id, channel, member.status)
                return False
        except Exception as exc:
            logging.error("Subscription check failed for user %s channel %s: %s", user_id, channel, exc)
            return False
    return True


@bot.message_handler(commands=['start'])
def start(message):
    add_user(message.from_user.id)
    logging.info("User %s triggered /start", message.from_user.id)
    bot.send_message(
        message.chat.id,
        "👋 Salom!\nQuyidagi kanallarga obuna bo‘ling va so‘ngra tekshiring:",
        reply_markup=channels_keyboard()
    )


@bot.callback_query_handler(func=lambda call: call.data == "check_subs")
def check_subs(call):
    user_id = call.from_user.id
    if check_subscription(user_id):
        logging.info("User %s subscription confirmed", user_id)
        bot.edit_message_text(
            "🎉 Obuna tasdiqlandi! Endi botdan foydalanishingiz mumkin.",
            call.message.chat.id,
            call.message.message_id,
            reply_markup=main_menu()
        )
    else:
        logging.info("User %s subscription rejected", user_id)
        bot.answer_callback_query(call.id, "❌ Hali barcha kanallarga obuna qilmagansiz!", show_alert=True)
        bot.edit_message_text(
            "❌ Siz hali barcha kanallarga obuna qilmagansiz. Iltimos, obuna bo‘ling va qayta tekshiring:",
            call.message.chat.id,
            call.message.message_id,
            reply_markup=channels_keyboard()
        )