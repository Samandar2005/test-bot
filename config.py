import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN", "")
if not TOKEN:
    raise RuntimeError("BOT_TOKEN is not set in the environment.")


def _parse_list(env_value: str):
    return [item.strip() for item in env_value.split(",") if item.strip()]


REQUIRED_CHANNELS = _parse_list(os.getenv("REQUIRED_CHANNELS", ""))
if not REQUIRED_CHANNELS:
    raise RuntimeError("REQUIRED_CHANNELS is not set in the environment.")


ADMIN_IDS = [int(item) for item in _parse_list(os.getenv("ADMIN_IDS", ""))]
if not ADMIN_IDS:
    raise RuntimeError("ADMIN_IDS is not set in the environment.")
