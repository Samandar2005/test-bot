from bot import bot
from database import load_users
from config import ADMIN_IDS

broadcast_data = {}

@bot.callback_query_handler(func=lambda call: call.data == "admin_broadcast")
def start_broadcast(call):
    if call.from_user.id not in ADMIN_IDS:
        return
    broadcast_data[call.from_user.id] = {"text": None, "photo": None}
    bot.send_message(call.message.chat.id, "📣 Reklama matnini yuboring yoki rasm yuboring.")


@bot.message_handler(func=lambda m: m.from_user.id in ADMIN_IDS)
def collect_broadcast(message):
    uid = message.from_user.id
    if uid not in broadcast_data:
        return

    if message.photo:
        broadcast_data[uid]["photo"] = message.photo[-1].file_id
        broadcast_data[uid]["text"] = message.caption
    else:
        broadcast_data[uid]["text"] = message.text

    bot.send_message(uid, "Tasdiqlaysizmi? /send_reklama")


@bot.message_handler(commands=['send_reklama'])
def send_broadcast(message):
    uid = message.from_user.id
    if uid not in broadcast_data:
        bot.send_message(uid, "❌ Avval reklama matnini yuboring.")
        return

    data = broadcast_data[uid]
    users = load_users()
    for user in users:
        try:
            if data["photo"]:
                bot.send_photo(user, data["photo"], caption=data["text"])
            else:
                bot.send_message(user, data["text"])
        except:
            pass
    bot.send_message(uid, "📨 Reklama yuborildi!")
    broadcast_data.pop(uid)
