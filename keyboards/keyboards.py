from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import REQUIRED_CHANNELS


def channels_keyboard(channels=None):
    kb = InlineKeyboardMarkup()
    channels = channels if channels else REQUIRED_CHANNELS
    for ch in channels:
        kb.add(InlineKeyboardButton(
            f"➕ {ch} obuna bo‘lish",
            url=f"https://t.me/{ch.replace('@','')}"
        ))
    kb.add(InlineKeyboardButton("✅ Tekshirish", callback_data="check_subs"))
    return kb


def main_menu():
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton("ℹ️ Asosiy bo‘lim", callback_data="menu"))
    return kb


def admin_menu():
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton("👥 Foydalanuvchilar soni", callback_data="admin_users"))
    kb.add(InlineKeyboardButton("📣 Reklama yuborish", callback_data="admin_broadcast"))
    return kb


def confirm_button():
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton("▶️ Yuborishni boshlash", callback_data="send_broadcast"))
    return kb
