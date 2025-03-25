import subprocess
import sys


def main():
    if len(sys.argv) < 2:
        print("Usage: python cf.py <command> [link]")
        return

    cmd = sys.argv[1]
    arg = sys.argv[2] if len(sys.argv) > 2 else None

    match cmd:
        case "load" if arg:
            script_path = "./apps/codeforces/load_samples_cf.py"
            subprocess.run(["python", script_path, arg])
        case "check":
            script_path = "./apps/codeforces/check_cf.py"
            subprocess.run(["python", script_path])
        case "submit":
            script_path = "./apps/codeforces/submit_cf.py"
            subprocess.run(["python", script_path])
        case "contest":
            script_path = "./core/contest_manager.py"
            subprocess.run(["python", script_path])
        case "last":
            script_path = "./apps/codeforces/last_sub_cf.py"
            subprocess.run(["python", script_path])
        case "friends":
            script_path = "./apps/codeforces/friend_sub_cf.py"
            subprocess.run(["python", script_path])
        case "rating":
            script_path = "./core/rating_manager.py"
            subprocess.run(["python", script_path])
        case _:
            print(f"❓ Unknown or incomplete command '{cmd}'")


if __name__ == "__main__":
    main()
