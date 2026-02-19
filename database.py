import os
import hashlib

SNAPSHOT_DIR = "snapshots"

os.makedirs(SNAPSHOT_DIR, exist_ok=True)

def get_hash(text):
    return hashlib.md5(text.encode()).hexdigest()

def save_snapshot(name, text):
    file = f"{SNAPSHOT_DIR}/{name}.txt"
    with open(file, "w", encoding="utf-8") as f:
        f.write(text)

def load_snapshot(name):
    file = f"{SNAPSHOT_DIR}/{name}.txt"
    if not os.path.exists(file):
        return None
    with open(file, "r", encoding="utf-8") as f:
        return f.read()
