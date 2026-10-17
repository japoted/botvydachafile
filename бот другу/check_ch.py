import httpx
import json
from pathlib import Path

_env = {}
for line in Path("env.txt").read_text(encoding="utf-8").splitlines():
    if "=" in line:
        k, v = line.strip().split("=", 1)
        _env[k.strip()] = v.strip()

TOKEN = _env["BOT_TOKEN"]
API = f"https://api.telegram.org/bot{TOKEN}"

r = httpx.get(f"{API}/getChat", params={"chat_id": "https://t.me/+hYr2gR1f7mw5ZDhi"}, timeout=15)
chat = r.json()
print(json.dumps(chat, ensure_ascii=False, indent=2))
