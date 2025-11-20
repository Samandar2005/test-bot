import logging
from bot import bot
from config import REQUIRED_CHANNELS
from database import add_user
from keyboards import channels_keyboard, main_menu


def check_subscription(user_id):
    missing_channels = []
    for channel in REQUIRED_CHANNELS:
        try:
            member = bot.get_chat_member(channel, user_id)
            if member.status not in ["member", "administrator", "creator"]:
                logging.info(
                    "User %s is not subscribed to %s (status=%s)",
                    user_id,
                    channel,
                    member.status
                )
                missing_channels.append(channel)
        except Exception as exc:
            logging.error(
                "Subscription check failed for user %s channel %s: %s",
                user_id,
                channel,
                exc
            )
            missing_channels.append(channel)
    return missing_channels


@bot.message_handler(commands=['start'])
def start(message):
    add_user(message.from_user.id)
    logging.info("User %s triggered /start", message.from_user.id)

    missing_channels = check_subscription(message.from_user.id)
    if not missing_channels:
        logging.info("User %s already subscribed to all channels", message.from_user.id)
        bot.send_message(
            message.chat.id,
            "✅ Siz allaqachon barcha shartli kanallarga obuna bo‘lgansiz!",
            reply_markup=main_menu()
        )
        return

    missing_text = "\n".join(f"• {ch}" for ch in missing_channels)
    bot.send_message(
        message.chat.id,
        "👋 Salom!\nQuyidagi kanallarga obuna bolishingiz kerak:\n"
        f"{missing_text}\nObuna bo‘lgach, \"Tekshirish\" tugmasini bosing.",
        reply_markup=channels_keyboard(missing_channels)
    )


@bot.callback_query_handler(func=lambda call: call.data == "check_subs")
def check_subs(call):
    user_id = call.from_user.id
    missing_channels = check_subscription(user_id)
    if not missing_channels:
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
        missing_text = "\n".join(f"• {ch}" for ch in missing_channels)
        bot.edit_message_text(
            "❌ Siz hali barcha kanallarga obuna qilmagansiz.\n"
            "Quyidagi kanallarga obuna bo‘ling va qayta tekshiring:\n"
            f"{missing_text}",
            call.message.chat.id,
            call.message.message_id,
            reply_markup=channels_keyboard(missing_channels)
        )