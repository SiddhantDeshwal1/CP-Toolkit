import os
import subprocess
import sys

import pyperclip

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
sys.path.append(root_dir)

from config import BROWSER

DATA_DIR = os.path.join(root_dir, "data")
LOCAL_DIR = os.path.join(root_dir, "local")
LINKS_FILE = os.path.join(DATA_DIR, "saved_links.txt")
WORKSPACE_FILE = os.path.join(LOCAL_DIR, "workspace.cpp")

if not os.path.exists(LINKS_FILE) or os.stat(LINKS_FILE).st_size == 0:
    print("❌ No saved URLs.")
    exit(1)

with open(LINKS_FILE) as f:
    url_fragment = f.readline().strip()

if not url_fragment or "/" not in url_fragment:
    print("❌ Invalid saved URL.")
    exit(1)

contest_id, problem_id = url_fragment.split("/")

subprocess.run([BROWSER, f"https://codeforces.com/problemset/submit/{url_fragment}"])

if os.path.exists(WORKSPACE_FILE):
    with open(WORKSPACE_FILE, encoding="utf-8") as f:
        pyperclip.copy(f.read())
else:
    print("❌ workspace.cpp not found.")
