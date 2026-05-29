"""Create SQLite test DB with sample users table."""
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DB_PATH = ROOT / "data" / "app.db"


def main() -> None:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.executescript(
        """
        DROP TABLE IF EXISTS users;

        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL,
            name TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'active',
            created_at TEXT NOT NULL DEFAULT (datetime('now'))
        );

        INSERT INTO users (email, name, status, created_at) VALUES
            ('kim@example.com', '김민수', 'active', '2026-01-15 10:00:00'),
            ('lee@example.com', '이지은', 'active', '2026-03-20 14:30:00'),
            ('park@example.com', '박서준', 'inactive', '2025-11-01 09:00:00'),
            ('choi@example.com', '최유나', 'active', '2026-05-10 18:45:00'),
            ('jung@example.com', '정하늘', 'active', '2026-05-28 11:20:00');
        """
    )

    conn.commit()
    count = cur.execute("SELECT COUNT(*) FROM users").fetchone()[0]
    conn.close()
    print(f"OK: {DB_PATH} ({count} users)")


if __name__ == "__main__":
    main()
