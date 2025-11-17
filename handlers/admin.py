from bot import bot
from database import load_users
from keyboards import admin_menu
from config import ADMIN_IDS

@bot.message_handler(commands=['admin'])
def admin_panel(message):
    if message.from_user.id in ADMIN_IDS:
        bot.send_message(message.chat.id, "🔐 Admin panel:", reply_markup=admin_menu())
    else:
        bot.send_message(message.chat.id, "❌ Siz admin emassiz.")


@bot.callback_query_handler(func=lambda call: call.data == "admin_users")
def show_users(call):
    if call.from_user.id not in ADMIN_IDS:
        return
    users = load_users()
    bot.send_message(call.message.chat.id, f"👥 Jami foydalanuvchilar: {len(users)} ta")
