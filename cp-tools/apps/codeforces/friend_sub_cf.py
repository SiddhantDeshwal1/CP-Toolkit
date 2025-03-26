import os
import subprocess
import sys

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
sys.path.append(root_dir)

from config import BROWSER

DATA_DIR = os.path.join(root_dir, "data")
LINKS_FILE = os.path.join(DATA_DIR, "saved_links.txt")

if not os.path.exists(LINKS_FILE):
    print("❌ No saved URLs.")
    exit(1)

with open(LINKS_FILE) as f:
    first_link = f.readline().strip()

parts = first_link.split("/")
try:
    contest_id = parts[0]
except (ValueError, IndexError):
    print("❌ Invalid URL format in saved_links.txt.")
    exit(1)

subprocess.run(
    [BROWSER, f"https://codeforces.com/contest/{contest_id}/standings/friends/true"]
)
