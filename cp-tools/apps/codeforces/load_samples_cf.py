import os
import re
import sys

import httpx
from bs4 import BeautifulSoup

# Define paths
DATA_DIR = os.path.join(os.path.dirname(__file__), "../../data")
LINKS_FILE = os.path.join(DATA_DIR, "saved_links.txt")
INPUT_FILE = os.path.join(DATA_DIR, "input.txt")
EXPECTED_FILE = os.path.join(DATA_DIR, "expected.txt")

os.makedirs(DATA_DIR, exist_ok=True)


def extract_problem_data(url):
    if not url:
        print("❌ No URL provided.")
        return

    url_segment = "/".join(url.strip().split("/")[-2:])
    with open(LINKS_FILE, "w", encoding="utf-8") as f:
        f.write(url_segment + "\n")

    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = httpx.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except httpx.HTTPError:
        print("❌ Failed to fetch problem page.")
        return

    soup = BeautifulSoup(response.text, "html.parser")

    inputs = []
    for div in soup.find_all("div", class_="input"):
        pre = div.find("pre")
        if pre:
            inputs.append(pre.get_text("\n", strip=True))

    outputs = []
    for div in soup.find_all("div", class_="output"):
        pre = div.find("pre")
        if pre:
            outputs.append(pre.get_text("\n", strip=True))

    with open(INPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n\n".join(inputs) + "\n")

    with open(EXPECTED_FILE, "w", encoding="utf-8") as f:
        f.write("\n\n".join(outputs) + "\n")

    print("✅ Test cases extracted successfully.")


if len(sys.argv) > 1:
    problem_url = sys.argv[1]
    extract_problem_data(problem_url)
else:
    print("❌ No URL provided as command-line argument.")
