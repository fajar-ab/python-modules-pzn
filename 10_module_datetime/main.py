import datetime

# tanggal dan waktu
sekarang = datetime.datetime.now()

print(f"sekarang: {sekarang}")

# hanya tanggal
hari_ini = datetime.date.today()

print(f"hari ini {hari_ini}")

# hanya waktu
waktu_sekarang = datetime.datetime.now().time()

print(f"waktu sekarang: {waktu_sekarang}")

# membuat tanggal tertentu
ulang_tahun = datetime.date(2024, 12, 25)
print(f"ulang tahun {ulang_tahun}")

# membuat waktu tertentu
acara = datetime.datetime(2024, 6, 15, 14, 30, 0)
print(f"waktu acara: {acara}")

# format indonesia
print(f"format indonesia: {sekarang.strftime("%d/%m/%Y %H:%M:%S")}")

# format panjang
print(f"format panajang: {sekarang.strftime("%A, %d %B %Y")}")

# format custom
print(f"format custom: {sekarang.strftime("%d-%m-%Y jam %H:%M")}")