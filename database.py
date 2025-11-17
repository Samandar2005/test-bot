import json
import os

DB_FILE = "users.json"

if not os.path.exists(DB_FILE):
    with open(DB_FILE, "w") as f:
        json.dump({"users": []}, f)


def load_users():
    with open(DB_FILE, "r") as f:
        return json.load(f)["users"]


def save_users(users):
    with open(DB_FILE, "w") as f:
        json.dump({"users": users}, f, indent=4)


def add_user(user_id):
    users = load_users()
    if user_id not in users:
        users.append(user_id)
        save_users(users)
