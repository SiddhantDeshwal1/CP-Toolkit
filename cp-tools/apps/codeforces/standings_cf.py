import os
import subprocess
import sys

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
sys.path.append(root_dir)
from config import BROWSER

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
sys.path.append(root_dir)

DATA_DIR = os.path.join(root_dir, "data")
LINKS_FILE = os.path.join(DATA_DIR, "saved_links.txt")

if not os.path.exists(LINKS_FILE) or os.stat(LINKS_FILE).st_size == 0:
    print("❌ No saved URLs.")
    exit(1)

with open(LINKS_FILE) as f:
    first_line = f.readline().strip()
    if "/" not in first_line:
        print("❌ Invalid contest URL.")
        exit(1)
    contest_id = first_line.split("/")[0]

subprocess.run(
    [BROWSER, f"https://codeforces.com/contest/{contest_id}/standings/friends/true"]
)
