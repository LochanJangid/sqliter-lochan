# ⚡ sqliter

A simple, clean, and ridiculously fast SQLite database wrapper for Python. **Zero dependencies. No boilerplate. Just queries.**

Stop writing the same database setup code over and over. `sqliter` abstracts away connections, cursors, and commits so you can focus on your application logic.

## 🚀 The Difference: Why use sqliter?

Working with standard `sqlite3` requires a lot of repetitive typing. `sqliter` fixes that.

### ❌ The Old Way (Standard `sqlite3`)
```python
import sqlite3

# 1. Open connection
# 2. Create cursor
# 3. Execute query
# 4. Remember to commit!
# 5. Remember to close!
conn = sqlite3.connect('myapp.db')
cursor = conn.cursor()
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Elone", 21))
conn.commit()
conn.close()
```

### ✅ The Clean Way (Using `sqliter`)
```python
from sqliter import Database

db = Database("myapp.db")

# Automatically connects, executes, commits, and closes securely behind the scenes.
db.query("INSERT INTO users (name, age) VALUES (?, ?)", ("Elone", 21))
```

---

## ✨ Features at a Glance

- **Zero dependencies** — Built entirely on Python's native `sqlite3`. No bulky external packages.
- **No repetitive boilerplate** — You never have to type `sqlite3.connect()` or `conn.cursor()` again.
- **One method for all operations** — A simple and predictable `db.query()` API for everything.
- **Dict-like rows by default** — Fetches results as dictionaries out of the box, making your data instantly accessible.
- **Proper exceptions** — Strict error handling ensures database failures never go unnoticed.
- **Built for "Us," not Enterprise** — This package was created for our own personal projects to solve real annoyances, not to be a bloated corporate framework. It's lightweight, easy to understand, and belongs to the community.

---

## 📦 Installation

Install the package via PyPI using the distribution name `sqliter-lochan`:

```bash
pip install sqliter-lochan
```
*(Note: You will import it in your code simply as `sqliter`)*

---

## 💻 Quick Start

```python
from sqliter import Database

# Initialize database (creates the file if it doesn't exist)
db = Database("myapp.db")

# Create a table
db.query("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")

# Insert data (Default operation is 'commit')
db.query("INSERT INTO users (name, age) VALUES (?, ?)", ("Elone", 21))

# Fetch a single row
user = db.query("SELECT * FROM users WHERE name = ?", ("Elone",), operation="fetchone")
print(dict(user))  
# Output: {'id': 1, 'name': 'Elone', 'age': 21}

# Fetch multiple rows
users = db.query("SELECT * FROM users", operation="fetchall")
for u in users:
    print(dict(u))
```

---

## 🛠 Operations Reference

The `operation` parameter in `db.query()` determines what you get back.

| `operation=` | Use Case | Returns |
|--------------|----------|---------|
| `"commit"` *(Default)* | `INSERT`, `UPDATE`, `DELETE`, `CREATE` | `True` on success |
| `"fetchone"` | `SELECT` a single row | `Row` object (dict-like) or `None` |
| `"fetchall"` | `SELECT` multiple rows | `list[Row]` |

---

## 🛡️ Error Handling

`sqliter` comes with custom exceptions so you can catch database failures predictably without crashing your main application.

```python
from sqliter import Database, DatabaseError

db = Database("myapp.db")

try:
    # Attempting an operation with a typo in the table name
    db.query("INSERT INTO bad_table (name) VALUES (?, ?)", ("Elone", 21))
except DatabaseError as e:
    print(f"Database operation failed: {e}")
```

---

## 🤝 Contributing

Because this is a personal-use tool and not a massive enterprise project, the codebase is incredibly easy to jump into. We actively welcome contributions! 

If you want to add a feature, fix a bug, or just make the code cleaner for everyone, feel free to submit a pull request. This is *our* tool now.

### Running Tests locally:
```bash
pip install pytest
pytest tests/
```

---

## 📄 License
⚖️ MIT License
