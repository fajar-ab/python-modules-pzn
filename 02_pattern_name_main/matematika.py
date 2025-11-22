def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        return "Error: bilangan tidak boleh 0"

    return a / b

PI = 3.14159
NAMA_PEMBUAT = "Tim Matematika"

if __name__ == "__main__":
    print("Program ini tidak bisa dijalankan sebagai modul")