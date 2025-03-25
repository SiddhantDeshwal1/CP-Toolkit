import time
from datetime import datetime, timedelta

import requests

query = {
    "query": """
    query {
      allContests {
        title
        titleSlug
        startTime
        duration
      }
    }
    """
}
headers = {
    "Referer": "https://leetcode.com/contest/",
    "Content-Type": "application/json",
}

try:
    response = requests.post(
        "https://leetcode.com/graphql", json=query, headers=headers
    )
    data = response.json()
    now = int(time.time())
    print("\n📅 Upcoming LeetCode Contests:\n")

    for contest in data["data"]["allContests"]:
        if contest["startTime"] > now:
            start_time = datetime.fromtimestamp(contest["startTime"])
            duration = str(timedelta(seconds=contest["duration"]))
            alert = "\033[91m" if (contest["startTime"] - now) < 43200 else ""
            print(f"{alert}{contest['title']}\033[0m")
            print(f"  ➤ Start: {start_time}")
            print(f"  ➤ Duration: {duration}")
            print(f"  ➤ URL: https://leetcode.com/contest/{contest['titleSlug']}/\n")
except Exception as e:
    print("❌ Error fetching LeetCode contests:", e)
