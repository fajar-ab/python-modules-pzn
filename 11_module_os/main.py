import os

# melihat informasi direktory
print(f"direktory saat ini {os.getcwd()}")

# melihat informasi system
# 'nt' untuk windows, 'posix' untuk Unix/Linux/Mac
print(f"nama sistem: {os.name}")

# cek apakah file/direktory ada
print(f"file ada: {os.path.exists("main.py")}")
print(f"folder ada: {os.path.exists("my_folder")}")

# informasi file
if os.path.exists("main.py"):
    print(f"adalah file: {os.path.isfile("main.py")}")
    print(f"adalah direktory: {os.path.isdir("main.py")}")
    print(f"ukuran file: {os.path.getsize("main.py")}")

# path operations
FILE_PATH = "home/fajar/Documents/file.txt"
print("direktori:", os.path.dirname(FILE_PATH))
print("nama file:", os.path.basename(FILE_PATH))
print("nama tanpa extensi:", os.path.splitext(FILE_PATH))
print("extensi:", os.path.splitext(FILE_PATH)[1])