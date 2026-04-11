import pytest
from sqliter import Database, DatabaseError


@pytest.fixture
def db(tmp_path):
    database = Database(str(tmp_path / "test.db"))
    database.query("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
    return database


def test_commit_insert(db):
    result = db.query("INSERT INTO users (name, age) VALUES (?, ?)", ("Rahul", 21))
    assert result == True


def test_fetchone(db):
    db.query("INSERT INTO users (name, age) VALUES (?, ?)", ("Rahul", 21))
    user = db.query("SELECT * FROM users WHERE name = ?", ("Rahul",), operation="fetchone")
    assert dict(user)["name"] == "Rahul"


def test_fetchall(db):
    db.query("INSERT INTO users (name, age) VALUES (?, ?)", ("Rahul", 21))
    db.query("INSERT INTO users (name, age) VALUES (?, ?)", ("Priya", 22))
    users = db.query("SELECT * FROM users", operation="fetchall")
    assert len(users) == 2


def test_invalid_operation(db):
    with pytest.raises(ValueError):
        db.query("SELECT * FROM users", operation="invalid")


def test_bad_query_raises_database_error(db):
    with pytest.raises(DatabaseError):
        db.query("SELECT * FROM nonexistent_table", operation="fetchall")


def test_repr(db):
    assert "Database(" in repr(db)
