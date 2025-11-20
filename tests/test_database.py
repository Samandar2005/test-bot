import importlib

import pytest


@pytest.fixture
def db_module(tmp_path, monkeypatch):
    db_path = tmp_path / "users_test.db"
    monkeypatch.setenv("DB_FILE", str(db_path))
    import database
    importlib.reload(database)
    return database


def test_init_creates_table(db_module):
    users = db_module.load_users()
    assert users == []


def test_add_user_inserts_once(db_module):
    db_module.add_user(123)
    db_module.add_user(123)
    db_module.add_user(456)
    users = db_module.load_users()
    assert sorted(users) == [123, 456]

