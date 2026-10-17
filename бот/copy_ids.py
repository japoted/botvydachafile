import sqlite3

old = sqlite3.connect(r"C:\Users\User\Downloads\Telegram Desktop\cheat_bot.db").cursor()
new = sqlite3.connect("games.db").cursor()

old_files = old.execute("SELECT cheat_key, file_id FROM files").fetchall()
ok = 0
for key, fid in old_files:
    r = new.execute("SELECT id FROM games WHERE name=? OR deep_link=?", (key, key)).fetchone()
    if r:
        new.execute("UPDATE games SET message_id=? WHERE id=?", (fid, r[0]))
        ok += 1
    else:
        new.execute(
            "INSERT INTO games (name,category,description,chat_id,message_id,file_name,file_size,downloads,deep_link) VALUES (?,?,?,?,?,\"\",0,0,?)",
            (key, "Other", "", 0, fid, key, key),
        )
        ok += 1

new.connection.commit()
total = new.execute('SELECT COUNT(*) FROM games WHERE message_id != "" AND message_id IS NOT NULL').fetchone()[0]
print(f"Updated: {ok}, Total with file_id: {total}")
