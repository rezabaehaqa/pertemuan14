# string
txt = "Hello World"

# menghitung jumlah banyaknya karakter
print("* menghitung jumlah banyaknya karakter\t\t\t:",len(txt))
# mengambil karkter terakhir
print("* mengambil karkter terakhir\t\t\t\t:",txt[-1])
# mengambil karakter index ke-2 sampai index ke-4
print("* mengambil karakter index ke-2 sampai index ke-4\t:",txt[2:5])
# Hilangkan spasi pada text tersebut
print("* Hilangkan spasi pada text tersebut\t\t\t:",txt.replace("",""))
# mengubah text menjadi huruf besar
print("* mengubah text menjadi huruf besar\t\t\t:",txt.upper())
# mengubah text menjadi huruf kecil
print("* mengubah text menjadi huruf kecil\t\t\t:",txt.lower())
# Ganti karakter H dengan karakter J
print("* Ganti karakter H dengan karakter J\t\t\t:",txt.replace("H","J"))

# melengkapi code
umur = 24
txt = '\n\nHello, nama saya jhon, dan umur saya adalah  %d tahun\n'%(umur)
print(txt.format(umur))
