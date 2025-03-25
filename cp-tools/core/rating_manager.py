import os
import subprocess
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from config import ENABLED_SITES

apps_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../apps"))

for site, enabled in ENABLED_SITES.items():
    if enabled:
        try:
            rating_script_path = os.path.join(apps_dir, site, "ratings.py")

            if os.path.exists(rating_script_path):
                subprocess.run(["python", rating_script_path], check=True)
            else:
                print(f"❌ {rating_script_path} not found.")
        except Exception as e:
            print(f"❌ Error running {site}: {e}")
