import os
import sys

import httpx

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
sys.path.append(root_dir)
from config import CF_HANDLE

# API URL
URL = f"https://codeforces.com/api/user.status?handle={CF_HANDLE}&from=1&count=1"

try:
    response = httpx.get(URL, timeout=10).json()
except httpx.HTTPError:
    print("❌ Failed to fetch data from Codeforces API.")
    exit(1)

if response.get("status") != "OK" or not response.get("result"):
    print("❌ API error or no submissions found.")
    exit(1)

submission = response["result"][0]
problem = submission.get("problem", {})

print(
    f"📘 Problem: {problem.get('contestId', '?')}{problem.get('index', '?')} - {problem.get('name', 'Unknown')}"
)
print(f"🧪 Verdict: {submission.get('verdict', 'N/A')}")
print(f"✅ Passed: {submission.get('passedTestCount', 'N/A')}")
print(f"⚡ Time: {submission.get('timeConsumedMillis', 0)} ms")
print(f"📦 Memory: {submission.get('memoryConsumedBytes', 0)} bytes")
