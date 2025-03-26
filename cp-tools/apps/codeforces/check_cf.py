import os
import subprocess
import sys

# Import the LANGUAGE from the config file

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
sys.path.append(root_dir)

from config import BROWSER  # Import from the correct path
from config import LANGUAGE

# Define correct paths
DATA_DIR = os.path.join(root_dir, "data")
LOCAL_DIR = os.path.join(root_dir, "local")

INPUT_FILE = os.path.join(DATA_DIR, "input.txt")
EXPECTED_FILE = os.path.join(DATA_DIR, "expected.txt")
WORKSPACE_CPP = os.path.join(LOCAL_DIR, "workspace.cpp")
WORKSPACE_CPP_EXEC = os.path.join(LOCAL_DIR, "workspace")
WORKSPACE_JAVA = os.path.join(LOCAL_DIR, "workspace.java")
WORKSPACE_PYTHON = os.path.join(LOCAL_DIR, "workspace.py")
WORKSPACE_PYTHON_EXEC = os.path.join(LOCAL_DIR, "workspace.py")


def compile_cpp():
    return (
        subprocess.run(
            ["g++", "-std=c++20", "-O2", "-o", WORKSPACE_CPP_EXEC, WORKSPACE_CPP]
        ).returncode
        == 0
    )


def compile_java():
    return subprocess.run(["javac", WORKSPACE_JAVA]).returncode == 0


def run_cpp():
    with open(INPUT_FILE) as fin:
        return subprocess.run(
            [WORKSPACE_CPP_EXEC], stdin=fin, capture_output=True, text=True
        )


def run_java():
    with open(INPUT_FILE) as fin:
        return subprocess.run(
            ["java", "workspace"], stdin=fin, capture_output=True, text=True
        )


def run_python():
    with open(INPUT_FILE) as fin:
        return subprocess.run(
            ["python", WORKSPACE_PYTHON_EXEC], stdin=fin, capture_output=True, text=True
        )


def compare_outputs(output, expected):
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
        "\n\033[32m✅ Passed\033[0m"
        if all_passed
        else "\n\033[31m❌ Wrong Answer\033[0m"
    )
    return all_passed


def main():
    # Decide the language to run based on the LANGUAGE variable imported from config
    if LANGUAGE == "CPP":
        if not compile_cpp():
            print("❌ Compilation failed for C++.")
            exit(1)
        proc = run_cpp()
    elif LANGUAGE == "JAVA":
        if not compile_java():
            print("❌ Compilation failed for Java.")
            exit(1)
        proc = run_java()
    elif LANGUAGE == "PYTHON":
        proc = run_python()
    else:
        print("❌ Unsupported language.")
        exit(1)

    output = [line.strip() for line in proc.stdout.splitlines()]

    if not os.path.exists(EXPECTED_FILE):
        print("❌ expected.txt not found.")
        exit(1)

    with open(EXPECTED_FILE) as f:
        expected = [line.strip() for line in f if line.strip()]

    all_passed = compare_outputs(output, expected)

    if all_passed:
        subprocess.run(["python", "apps/codeforces/submit_cf.py"])


if __name__ == "__main__":
    main()
