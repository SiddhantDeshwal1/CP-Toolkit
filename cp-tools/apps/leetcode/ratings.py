import os
import sys

import requests

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from config import LC_HANDLE

query = {
    "query": """
    query getUserContestRanking($username: String!) {
      userContestRanking(username: $username) {
        rating
      }
    }
    """,
    "variables": {"username": LC_HANDLE},
}

res = requests.post("https://leetcode.com/graphql", json=query)
data = res.json()
rating = data["data"]["userContestRanking"]

print(f"📊 LeetCode ({LC_HANDLE}):", rating["rating"] if rating else None)
