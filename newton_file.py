import json

def interpolasi_newton(Xtanya, derajat, X, Y):
    """
    Fungsi untuk menghitung interpolasi polinom Newton.

    Ditanya:
        Xtanya: Nilai x untuk mencari Ytanya.
        derajat: Derajat polinom (jumlah titik data - 1).
        X: List nilai x.
        Y: List nilai y.

    Dijawab:
        Ytanya: Nilai y yang diinterpolasi untuk Xtanya.
        selisih_terbagi: Tabel selisih terbagi.
    """

    # Menghitung tabel selisih maju
    selisih_terbagi = [[0 for _ in range(derajat + 1)] for _ in range(derajat + 1)] #membuat list bersarang matrix yang berisikan nilai 0
    for i in range(derajat + 1): 
        selisih_terbagi[i][0] = Y[i] #perulangan untuk mengisi tabel selisihh terbagi pada kolom Y banyak kolom
    for j in range(1, derajat + 1): #perulangan dimulai dari 1 sampai derajat + 1
        for i in range(derajat - j + 1): #perulangan dimulai dari list j
            selisih_terbagi[i][j] = (selisih_terbagi[i + 1][j - 1] - selisih_terbagi[i][j - 1]) / (X[i + j] - X[i])
            #menghitung selisih terbagi dengan menggunakan nilai selisih terbagi dari list sebelumnya.

    # Menampilkan selisih terbagi
    print("\nSelisih Terbagi:")
    for j in range(derajat + 1):
        print(f"Selisih Terbagi {j+1}:")
        for i in range(derajat - j + 1):
            print(f"   X[{i+1}] - X[{i+j+1}]: {selisih_terbagi[i][j]:.8f}")
        print()

    # Menghitung Ytanya menggunakan formula interpolasi Newton
    Ytanya = selisih_terbagi[0][0] # mengisi Ytanya dengan nilai selisih terbagi pertama, yang sebenarnya adalah nilai y dari titik data pertama.
    for j in range(1, derajat + 1):
        faktor = 1
        for k in range(j):
            faktor *= (Xtanya - X[k])
        Ytanya += selisih_terbagi[0][j] * faktor

    return Ytanya, selisih_terbagi

# Menu pilihan
print("Pilih metode input:")
print("1. Input manual")
print("2. Baca dari file JSON (bawaaan data.json, ubah data.json jika diperlukan)")

pilihan = input("Masukkan pilihan (1 atau 2): ")

if pilihan == "1":
    # Input manual
    Xtanya = float(input("Masukkan nilai x yang ingin dicari y-nya: "))
    derajat = int(input("Masukkan derajat polinom (jumlah titik data - 1): "))
    X = [] #list gampang digunakan
    Y = []
    print("Masukkan data titik X dan Y:")
    for i in range(derajat + 1): #oerulangan sebanyak derajat + 1
        x = float(input(f"X[{i+1}]: "))
        y = float(input(f"Y[{i+1}]: "))
        X.append(x)
        Y.append(y) #memasukan data kedalam list dengan append

    Ytanya, selisih_terbagi = interpolasi_newton(Xtanya, derajat, X, Y) # pemanggilan fungsi dengan parameter didalamnya
    print(f"\nNilai y yang diinterpolasi untuk x = {Xtanya} adalah: {Ytanya}")

elif pilihan == "2":
    # Baca dari file JSON
    # data_json = input("Masukkan nama file JSON: ")
    data_json = "data.json"
    with open(data_json, 'r') as f:
        data = json.load(f)
    X = [float(x) for x in data['X']]
    Y = [float(y) for y in data['Y']]
    derajat = data['derajat']
    Xtanya = data['Xtanya']

    Ytanya, selisih_terbagi = interpolasi_newton(Xtanya, derajat, X, Y)
    print(f"\nNilai y yang diinterpolasi untuk x = {Xtanya} adalah: {Ytanya}")

else:
    print("Pilihan tidak valid.")