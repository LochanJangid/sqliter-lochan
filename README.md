# sqliter

A simple, clean SQLite database wrapper for Python. No dependencies. No complexity. Just works.

## Installation

```bash
pip install sqliter
```

## Quick Start

```python
from sqliter import Database

db = Database("myapp.db")

# Create table
db.query("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")

# Insert
db.query("INSERT INTO users (name, age) VALUES (?, ?)", ("Elone", 21))

# Fetch one
user = db.query("SELECT * FROM users WHERE name = ?", ("Elone",), operation="fetchone")
print(dict(user))  # {'id': 1, 'name': 'Elone', 'age': 21}

# Fetch all
users = db.query("SELECT * FROM users", operation="fetchall")
for u in users:
    print(dict(u))
```

## Operations

| Operation | Description | Returns |
|-----------|-------------|---------|
| `"commit"` | INSERT, UPDATE, DELETE, CREATE | `True` |
| `"fetchone"` | SELECT single row | `Row` or `None` |
| `"fetchall"` | SELECT all rows | `list[Row]` |

## Error Handling

```python
from sqliter import Database, DatabaseError

db = Database("myapp.db")

try:
    db.query("INSERT INTO users (name) VALUES (?)", ("Elone",))
except DatabaseError as e:
    print(f"Something went wrong: {e}")
```

## Why sqliter-lochan?

- Zero dependencies — only uses Python's built-in `sqlite3`
- One method for all operations — simple and predictable
- Returns dict-like rows — easy to work with
- Proper exceptions — errors never go unnoticed

## Running Tests

```bash
pip install pytest
pytest tests/
```

## License

MIT
