from bot import bot
from database import load_users
from config import ADMIN_IDS

broadcast_data = set()


@bot.callback_query_handler(func=lambda call: call.data == "admin_broadcast")
def start_broadcast(call):
    if call.from_user.id not in ADMIN_IDS:
        return
    broadcast_data.add(call.from_user.id)
    bot.send_message(call.message.chat.id, "📣 Reklama matnini yuboring yoki rasm yuboring.")


@bot.message_handler(func=lambda m: m.from_user.id in ADMIN_IDS, content_types=['text', 'photo'])
def collect_broadcast(message):
    if message.content_type == "text" and message.text.startswith("/"):
        return

    uid = message.from_user.id
    if uid not in broadcast_data:
        return

    text = None
    photo = None

    if message.photo:
        photo = message.photo[-1].file_id
        text = message.caption or ""
    else:
        text = message.text or ""

    send_broadcast(uid, text, photo)
    broadcast_data.discard(uid)


def send_broadcast(admin_id, text, photo=None):
    users = load_users()
    sent = 0
    failed = 0
    for user in users:
        try:
            if photo:
                bot.send_photo(user, photo, caption=text or None)
            else:
                bot.send_message(user, text)
            sent += 1
        except:
            failed += 1

    bot.send_message(
        admin_id,
        f"📨 Reklama yuborildi!\n✅ {sent} foydalanuvchiga yetdi"
        + (f"\n❌ {failed} foydalanuvchiga yuborib bo'lmadi" if failed else "")
    )
