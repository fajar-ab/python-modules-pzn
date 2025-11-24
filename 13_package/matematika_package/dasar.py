# matematika_package/dasar.py

PI = 3.14159
NAMA_PEMBUAT = "Tim Matematika"

def tambah(a, b):
    """
    menambahkan dua angka
    """
    return a + b

def kurang(a, b):
    """
    mengurangi dua angka
    """
    return a - b

def kali(a, b):
    """
    mengkalikan dua angka
    """
    return a * b

def bagi(a, b):
    """
    membagi dua angka
    """
    if b == 0:
        return "Error: bilangan tidak boleh 0"

    return a / b


if __name__ == "__main__":
    print("Program ini tidak bisa dijalankan sebagai modul")