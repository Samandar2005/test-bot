import logging

from bot import bot
import handlers.start
import handlers.admin
import handlers.broadcast


def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    )
    logging.getLogger("telebot").setLevel(logging.WARNING)


if __name__ == "__main__":
    setup_logging()
    logging.info("Bot ishga tushdi...")
    bot.infinity_polling()
