arrBerat = []
bMin = 0
bMax = 0
def hitungMinMax(arrBerat):
    global bMin, bMax
    # Definisikan Proses Mencari Berat Maximum Dan Minimum
    arrBerat.sort()
    bMin = arrBerat[0]
    bMax = arrBerat[-1]
    return bMin, bMax
def rerata(arrBerat):
    total = 0
    # Definisikan Proses Mencari Rerata Dari Total Berat
    for i in arrBerat:
        total += i
    rerata = total/len(arrBerat)
    # Return Hasil Rerata
    return rerata

print('Masukkan Banyak Data Berat Balita :', end=" ")
n = int(input())

for i in range(n):
    print(f'Masukkan Berat Balita Ke-{i+1} :', end=' ')
    # Inisialisasi Input Data Berat
    berat = float(input())
    # Masukkan Data Berat Ke Array (arrBerat)
    arrBerat.append(berat)

# Panggil procedur hitungMinMax(arrBerat)
hitungMinMax(arrBerat)

# Print Data Minimum, Maximum, dan Rerata Berat
print("Berat balita minimum: {:.2f} kg".format(bMin))
print("Berat balita maksimum: {:.2f} kg".format(bMax))
print("Rerata berat balita: {:.2f} kg".format(rerata(arrBerat)))