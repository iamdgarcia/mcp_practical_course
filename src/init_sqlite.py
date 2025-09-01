import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "data" / "community.db"
DB_PATH.parent.mkdir(parents=True, exist_ok=True)

def init_db():
    conn = sqlite3.connect(DB_PATH.as_posix())
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS chatters;")
    cur.execute("CREATE TABLE chatters (name TEXT, messages INTEGER);")
    cur.executemany(
        "INSERT INTO chatters (name, messages) VALUES (?, ?);",
        [("Alice", 120), ("Bob", 75), ("Carlos", 50)],
    )
    conn.commit()
    conn.close()
    print(f"SQLite inicializada en {DB_PATH}")

if __name__ == "__main__":
    init_db()
