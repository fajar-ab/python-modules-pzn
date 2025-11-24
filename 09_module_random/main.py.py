import random

# angk integer random
print(f"random 1-10: {random.randint(1, 10)}")
print(f"random 1-100: {random.randint(1, 100)}")

# angka random float
print(f"random 0.0-0.1: {random.random()}")
print(f"random 1.5-10.5: {random.uniform(1.5, 10.5)}")

# pilih satu item
buah = ["apel", "jeruk", "mangga", "pisang", "anggur"]
pilihan = random.choice(buah)
print(f"buah yang terpilih: {pilihan}")