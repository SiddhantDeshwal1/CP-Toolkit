import os
import sys

import requests
from bs4 import BeautifulSoup

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from config import CC_HANDLE

url = f"https://www.codechef.com/users/{CC_HANDLE}"
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")
rating_tag = soup.find("div", class_="rating-number")

print(f"📊 CodeChef ({CC_HANDLE}):", rating_tag.text.strip() if rating_tag else None)
