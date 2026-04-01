import sqlite3

DB_PATH = "lsd.db"

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # allows dict(row) later
    return conn

def init_db():
    conn = get_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS categories (
            id   INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS businesses (
            id         INTEGER PRIMARY KEY AUTOINCREMENT,
            name       TEXT NOT NULL,
            category   TEXT,
            location   TEXT,
            rating     REAL DEFAULT 0.0,
            is_active  INTEGER DEFAULT 1
        )
    """)

    # Seed some categories so the dropdown has real options
    categories = ["Restaurant", "Salon", "Hardware Store", "Pharmacy", "Gym"]
    for cat in categories:
        conn.execute(
            "INSERT OR IGNORE INTO categories (name) VALUES (?)", (cat,)
        )

    # Seed some businesses so you have data to see immediately
    sample_businesses = [
        ("Chai Stop",        "Restaurant",     "City Centre", 4.5),
        ("Glow Salon",       "Salon",          "Benachity",   4.2),
        ("BuildRight",       "Hardware Store", "Durgapur",    3.8),
        ("MedPlus Pharmacy", "Pharmacy",       "City Centre", 4.7),
        ("IronZone Gym",     "Gym",            "Bidhan Nagar",4.1),
    ]
    conn.executemany(
        "INSERT OR IGNORE INTO businesses (name, category, location, rating) VALUES (?,?,?,?)",
        sample_businesses
    )

    conn.commit()
    conn.close()