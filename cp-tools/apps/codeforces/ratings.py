import os
import sys

import httpx

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
sys.path.append(root_dir)
from config import CF_HANDLE

url = f"https://codeforces.com/api/user.info?handles={CF_HANDLE}"
try:
    res = httpx.get(url, timeout=5).json()
    rating = res["result"][0].get("rating", "N/A") if res["status"] == "OK" else "N/A"
except Exception:
    rating = "❌ API Error"

print(f"📊 Codeforces ({CF_HANDLE}):", rating)
