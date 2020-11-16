klubA = input("Klub A : ")
klubB = input("Klub B : ")

hasil = []
putaran = 1

while True:
    a,b = map(int,input("Pertandingan {} : ".format(putaran)).split())
    if a>=0 and b>=0:
        if a > b:
            hasil.append(klubA)
        elif b > a:
            hasil.append(klubB)
        elif a == b:
            hasil.append("Draw")
    else:
        break
    putaran += 1

for i in range(putaran-1):
    print("Hasil",i+1, ":", hasil[i])

print("Pertandingan selesai")