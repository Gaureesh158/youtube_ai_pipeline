import os

def make_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print(f"Folder created: {folder_name}")
    else:
        print(f"Folder already exists: {folder_name}")

def read_file(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    else:
        print(f"File not found: {file_path}")
        return ""

def write_file(file_path, content):
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"File saved: {file_path}")

def split_segments(script_text, separator="---"):
    segments = [seg.strip() for seg in script_text.split(separator) if seg.strip()]
    return segments
