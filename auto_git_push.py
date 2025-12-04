import os
import time
import subprocess
from datetime import datetime

# ------------ CONFIG ------------
REPO_PATH = r"D:\GitProject\DjangoLearning"  # your repo path
CHECK_INTERVAL = 600  # seconds
# --------------------------------

def run(cmd):
    """Run a git command and return stdout, stderr."""
    result = subprocess.run(
        cmd,
        cwd=REPO_PATH,
        text=True,
        capture_output=True,
        shell=True
    )
    return result.stdout.strip(), result.stderr.strip()

def get_changed_files():
    """Detect staged + unstaged + untracked files."""
    stdout, _ = run("git status --porcelain")
    files = []
    for line in stdout.splitlines():
        if line.strip():
            files.append(line[3:])
    return files

def generate_commit_message(files):
    c = len(files)
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if c == 1:
        return f"Updated {files[0]}"
    if c <= 3:
        return "Modified: " + ", ".join(files)
    return f"Updated {c} files on {ts}"

def get_current_branch():
    stdout, _ = run("git rev-parse --abbrev-ref HEAD")
    return stdout.strip()

def commit_and_push():
    files = get_changed_files()
    if not files:
        print("⏳ No changes found.")
        return

    print(f"🔍 {len(files)} change(s) detected.")

    # Stage all changes
    print("📌 Staging files...")
    run("git add -A")

    # Prepare commit message
    commit_msg = generate_commit_message(files)
    print("📝 Commit message:", commit_msg)

    # Commit
    stdout, stderr = run(f'git commit -m "{commit_msg}"')
    if "nothing to commit" in stdout.lower():
        print("⚠ Nothing new to commit.")
        return
    print("✅ Commit done.")

    # Detect branch
    branch = get_current_branch()
    if not branch:
        print("❌ Could not detect branch.")
        return

    # Push
    print(f"🚀 Pushing to origin/{branch} ...")
    stdout, stderr = run(f"git push origin {branch}")

    if stderr:
        print("⚠ Git Error:", stderr)
    else:
        print("🎉 Push successful!")

def main():
    print("🚀 Auto Git Sync Started (checks every 1 minute)...")
    while True:
        commit_and_push()
        print("⏲ Waiting 1 minute...\n")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n🛑 Stopped manually.")
