import os
import time
import subprocess
from datetime import datetime

# ---- CONFIG ----
CHECK_INTERVAL = 5  # seconds
REPO_PATH = r"D:\GitProject\DjangoLearning"   # <-- apna repo path daalein

def run_command(command):
    result = subprocess.run(command, shell=True, cwd=REPO_PATH, capture_output=True, text=True)
    return result.stdout.strip(), result.stderr.strip()

def has_changes():
    stdout, _ = run_command("git status --porcelain")
    return bool(stdout)

def get_changed_files():
    stdout, _ = run_command("git diff --name-only")
    return stdout.splitlines()

def generate_commit_message():
    files = get_changed_files()
    if not files:
        return None
    if len(files) == 1:
        return f"Updated {files[0]}"
    elif len(files) <= 3:
        return "Modified " + ", ".join(files)
    else:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"Updated {len(files)} files on {timestamp}"

def auto_commit_and_push():
    commit_msg = generate_commit_message()
    if not commit_msg:
        return

    print(f"\n🔍 Changes detected. Committing: '{commit_msg}'")
    run_command("git add .")
    run_command(f'git commit -m "{commit_msg}"')
    stdout, stderr = run_command("git push")

    if "error" in stderr.lower() or "fatal" in stderr.lower():
        print(f"⚠️ Push error: {stderr}")
    else:
        print(f"✅ Pushed successfully!\n{stdout}")

def main():
    print(f"🚀 Auto Git Push started for repo: {REPO_PATH}")
    while True:
        if has_changes():
            auto_commit_and_push()
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n🛑 Auto Git Push stopped manually.")
