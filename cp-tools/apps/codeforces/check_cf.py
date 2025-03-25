import os
import subprocess
import sys

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
sys.path.append(root_dir)

from config import BROWSER  # Import from the correct path

# Define correct paths
DATA_DIR = os.path.join(root_dir, "data")
LOCAL_DIR = os.path.join(root_dir, "local")

INPUT_FILE = os.path.join(DATA_DIR, "input.txt")
EXPECTED_FILE = os.path.join(DATA_DIR, "expected.txt")
WORKSPACE_CPP = os.path.join(LOCAL_DIR, "workspace.cpp")
WORKSPACE_EXEC = os.path.join(LOCAL_DIR, "workspace")

compilation = (
    subprocess.run(
        ["g++", "-std=c++20", "-O2", "-o", WORKSPACE_EXEC, WORKSPACE_CPP]
    ).returncode
    == 0
)

if not compilation:
    print("❌ Compilation failed.")
    exit(1)

if not os.path.exists(INPUT_FILE):
    print("❌ input.txt not found.")
    exit(1)

with open(INPUT_FILE) as fin:
    proc = subprocess.run([WORKSPACE_EXEC], stdin=fin, capture_output=True, text=True)

output = [line.strip() for line in proc.stdout.splitlines()]

if not os.path.exists(EXPECTED_FILE):
    print("❌ expected.txt not found.")
    exit(1)

with open(EXPECTED_FILE) as f:
    expected = [line.strip() for line in f if line.strip()]

# Display output
print("\n📤 Output:\n")
for line in output:
    print(line)

print("\n✅ Checking output...\n")

all_passed = True

for i in range(max(len(output), len(expected))):
    out = output[i] if i < len(output) else ""
    exp = expected[i] if i < len(expected) else ""

    if out == exp:
        print(f"\033[32m+ Case {i + 1}: {out}\033[0m")
    else:
        print(f"\033[31m- Case {i + 1}: {out}\033[0m")
        print(f"\033[33m  Expected: {exp}\033[0m")
        all_passed = False

print(
    "\n\033[32m✅ Passed\033[0m" if all_passed else "\n\033[31m❌ Wrong Answer\033[0m"
)

if all_passed:
    subprocess.run(["python", "apps/codeforces/submit_cf.py"])
