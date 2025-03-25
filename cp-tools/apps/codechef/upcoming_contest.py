from datetime import datetime

import requests

url = "https://www.codechef.com/api/list/contests/all"
try:
    response = requests.get(url)
    data = response.json()
    print("\n📅 Upcoming CodeChef Contests:\n")

    for contest in data["future_contests"]:
        name = contest["contest_name"]
        code = contest["contest_code"]
        start = datetime.strptime(contest["contest_start_date"], "%d %b %Y  %H:%M:%S")
        end = datetime.strptime(contest["contest_end_date"], "%d %b %Y  %H:%M:%S")
        duration_minutes = int(contest["contest_duration"])
        contest_url = f"https://www.codechef.com/{code}"
        alert = "\033[91m" if (start - datetime.now()).total_seconds() < 43200 else ""

        print(f"{alert}🟢 {name}\033[0m")
        print(f"   🗓  Start   : {start.strftime('%A, %d %B %Y %I:%M %p')}")
        print(f"   🛑 End     : {end.strftime('%A, %d %B %Y %I:%M %p')}")
        print(f"   ⏱  Duration: {duration_minutes} minutes")
        print(f"   🔗 Link    : {contest_url}\n")

except Exception as e:
    print("❌ Error fetching CodeChef contests:", e)
