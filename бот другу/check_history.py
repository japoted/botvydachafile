import httpx
import json
from pathlib import Path

_env = {}
for line in Path("env.txt").read_text(encoding="utf-8").splitlines():
    if "=" in line:
        k, v = line.strip().split("=", 1)
        _env[k.strip()] = v.strip()

TOKEN = _env["BOT_TOKEN"]
ADMIN_ID = int(_env["ADMIN_ID"])
API = f"https://api.telegram.org/bot{TOKEN}"

r = httpx.get(f"{API}/getHistory", params={
    "chat_id": ADMIN_ID,
    "limit": 100
}, timeout=15)
print(json.dumps(r.json(), ensure_ascii=False, indent=2))
