import os

def load_java_files(repo_path):
    java_files = []
    for root, _, files in os.walk(repo_path):
        for file in files:
            if file.endswith(".java"):
                full_path = os.path.join(root, file)
                with open(full_path, "r", errors="ignore") as f:
                    java_files.append({
                        "path": full_path,
                        "content": f.read()
                    })
    return java_files
