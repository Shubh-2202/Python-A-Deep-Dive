from pathlib import Path

file_path = Path("practice.txt")
print("Current folder:", Path.cwd()) 
print("File exists:", file_path.exists())
print("File name:", file_path.name)
print("File size:", file_path.stat().st_size, "bytes")