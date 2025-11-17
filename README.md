# Telegram Subscription Bot

A simple Telegram bot built with `pyTelegramBotAPI` that enforces channel subscriptions and provides admin tooling for user stats and broadcasts.

## Features
- `/start` prompts users to join required channels and verifies membership.
- Admins (`/admin`) can view total users and initiate broadcasts.
- Broadcasts support plain text or photo+caption; delivery stats are reported per send.
- Users are stored in `users.json` via a lightweight JSON database helper.

## Setup
1. Create a virtual environment (optional but recommended) and install dependencies:
   ```
   python -m venv env
   env\Scripts\activate
   pip install -r requirements.txt
   ```
2. Copy your bot token and channel/admin config into `config.py`.
3. Run the bot:
   ```
   python main.py
   ```

## Structure
- `bot.py` – initializes the shared `TeleBot` instance.
- `handlers/` – command, callback and broadcast logic.
- `keyboards/` – inline keyboard factories.
- `database.py` – simple JSON-based user storage.

## Notes
- Keep your virtual environment, cache folders, and `users.json` out of version control (already covered in `.gitignore`).
- When testing broadcasts, use a separate admin account to avoid spamming general users.

