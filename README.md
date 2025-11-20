# Telegram Subscription Bot 🚀

Modern Telegram assistant built with `pyTelegramBotAPI` that keeps your audience subscribed to required channels, provides an admin dashboard, and ships broadcasts (text or photo) with live delivery stats.

## Highlights
- `/start` detects which channels a user still needs to join and hides the subscription screen if everything is already complete.
- Inline keyboards dynamically list only the missing channels, so users always know what’s left.
- `/admin` exposes user count, broadcast launcher, and automatic logging for easier maintenance.
- Broadcasts go out immediately (no extra `/send` confirmation) and support text, photo + caption, plus per-user error tracking.
- SQLite storage (`users.db`) keeps the bot lightweight while enabling safe concurrent access.

## Quick Start
```bash
python -m venv env
env\Scripts\activate        # or source env/bin/activate on Linux/macOS
pip install -r requirements.txt
```

Create a `.env` file in the project root:
```
BOT_TOKEN=123456:ABCDEF...
REQUIRED_CHANNELS=@channel1,@channel2,@channel3
ADMIN_IDS=111111111,222222222
```

Then launch the bot:
```bash
python main.py
```

## Project Map
- `main.py` – boots the bot, configures logging, and starts `infinity_polling`.
- `config.py` – loads secrets from `.env`, validates required settings.
- `handlers/` – `/start`, admin tools, and broadcast logic.
- `keyboards/` – builders for subscription, main menu, and admin inline keyboards.
- `database.py` – SQLite helpers (auto-creates `users` table).
- `users.db` – generated automatically; ignored by Git.

## Tips & Next Steps
- When adding new channels or admins, just update `.env` and restart the bot.
- Consider batching broadcasts or adding rate-limiting if the user base grows large.
- Logging already captures subscription failures and broadcast errors—watch the console while testing.
- For production hosting, run the bot inside a supervisor or systemd service so it restarts automatically.

Enjoy building your community bot! 💬

