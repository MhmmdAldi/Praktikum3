a = input("masukan nilai a : ")
b = input("masukan nilai b : ")

print("variable a : ", a)
print("variable b : ", b)

print("hasil penggabungan {1} & {0} = ".format(a, b), (a+b))
# konversi nilai variable
a = int(a)
b = int(b)
print("hasil Penjumlahan {0} + {1}=%d ".format(a, b) % (a+b))
print("hasil Pembagian {0} / {1}=%d ".format(a, b) % (a/b))