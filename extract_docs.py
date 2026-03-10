import os
import shutil

SOURCE_REPO = "openclaw"
DEST_REPO = "openclaw-knowledge"

ALLOWED_EXTENSIONS = [".md", ".mdx", ".txt", ".rst"]

IGNORED_FOLDERS = [
".git",
"node_modules",
".vscode",
".github",
"dist",
"build",
"apps",
"packages",
"extensions"
]

if not os.path.exists(DEST_REPO):
    os.makedirs(DEST_REPO)

for root, dirs, files in os.walk(SOURCE_REPO):

    dirs[:] = [d for d in dirs if d not in IGNORED_FOLDERS]

    for file in files:
        if any(file.endswith(ext) for ext in ALLOWED_EXTENSIONS):

            source_path = os.path.join(root, file)

            relative_path = os.path.relpath(source_path, SOURCE_REPO)

            destination_path = os.path.join(DEST_REPO, relative_path)

            os.makedirs(os.path.dirname(destination_path), exist_ok=True)

            shutil.copy2(source_path, destination_path)

print("Documentation extraction complete.")
