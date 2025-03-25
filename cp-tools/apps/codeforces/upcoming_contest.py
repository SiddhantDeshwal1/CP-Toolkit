import time
from datetime import datetime, timedelta, timezone

import httpx

url = "https://codeforces.com/api/contest.list?gym=false"

try:
    res = httpx.get(url).json()
    if res["status"] != "OK":
        print("❌ Failed:", res.get("comment", "No message"))
        exit(1)

    upcoming = [c for c in res["result"] if c["phase"] == "BEFORE"]
    if not upcoming:
        print("📭 No upcoming Codeforces contests.")
        exit(0)

    print("\n📅 Upcoming Codeforces Contests (IST):\n")
    for c in sorted(upcoming, key=lambda x: x["startTimeSeconds"]):
        name = c["name"]
        ist = datetime.fromtimestamp(c["startTimeSeconds"], timezone.utc) + timedelta(
            hours=5, minutes=30
        )
        alert = "\033[91m" if (c["startTimeSeconds"] - time.time()) < 43200 else ""
        print(
            f"{alert}📌 {name} | 🕒 {ist.strftime('%Y-%m-%d %H:%M')} IST | ⏱️ {c['durationSeconds'] // 3600}h\033[0m"
        )
except Exception as e:
    print("❌ Error fetching Codeforces contests:", e)
