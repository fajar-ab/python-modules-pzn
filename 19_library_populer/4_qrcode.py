import qrcode

# membuat qrcode
img = qrcode.make("https://youtu.be/dIeKPJcI2NM?list=PL-CtdCApEFH98kBk72926663HfuFULMk5&t=6468")

# menyimpan qrcode
img.save("demo_qrcode.png")