import os

# Browser settings
BROWSER = "librewolf"

# Compilation settings

# Enable/Disable sites
ENABLED_SITES = {
    "leetcode": True,
    "codeforces": True,
    "codechef": True,
}

# Choose your language
# CPP , JAVA , PYTHON
LANGUAGE = "JAVA"

# User handles
CF_HANDLE = "siddhantdeshwal"
LC_HANDLE = "siddhantdeshwal1"
CC_HANDLE = "just_lie"

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# File paths
WORKSPACE_FILE = os.path.join(ROOT_DIR, "local", "workspace.cpp")
INPUT_FILE = os.path.join(ROOT_DIR, "data", "input.txt")
EXPECTED_FILE = os.path.join(ROOT_DIR, "data", "expected.txt")
LINKS_FILE = os.path.join(ROOT_DIR, "data", "links.txt")


# Function to get the absolute path of a file
def get_abs_path(filename):
    return os.path.abspath(filename)
