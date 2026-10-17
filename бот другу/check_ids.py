import sqlite3
db = sqlite3.connect("games.db")
rows = db.execute("SELECT id, name, message_id FROM games LIMIT 5").fetchall()
for r in rows:
    print(r)
print("---")
rows2 = db.execute("SELECT message_id FROM games WHERE message_id != '' AND message_id IS NOT NULL LIMIT 5").fetchall()
for r in rows2:
    val = r[0]
    print(f"  {type(val).__name__}: {str(val)[:80]}")
