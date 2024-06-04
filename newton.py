def interpolasi_newton(Xtanya, derajat):
    """

    Ditanya:
        Xtanya: Nilai x untuk mencari Ytanya.
        derajat: Derajat polinom (jumlah titik data - 1).

    Jawab:
        Ytanya: Nilai y yang diinterpolasi untuk Xtanya.
        selisih_maju: Tabel selisih maju.
    """

    # Input data titik X dan Y
    X = []
    Y = []
    print("Masukkan data titik X dan Y:")
    for i in range(derajat + 1):
        x = float(input(f"X[{i+1}]: "))
        y = float(input(f"Y[{i+1}]: "))
        X.append(x)
        Y.append(y)

    # Menghitung tabel selisih maju
    selisih_maju = [[0 for _ in range(derajat + 1)] for _ in range(derajat + 1)]
    for i in range(derajat + 1):
        selisih_maju[i][0] = Y[i]
    for j in range(1, derajat + 1):
        for i in range(derajat - j + 1):
            selisih_maju[i][j] = (selisih_maju[i + 1][j - 1] - selisih_maju[i][j - 1]) / (X[i + j] - X[i])

    # Menampilkan selisih terbagi
    print("\nSelisih Terbagi:")
    for j in range(derajat + 1):
        print(f"Selisih Terbagi {j+1}:")
        for i in range(derajat - j + 1):
            print(f"   X[{i+1}] - X[{i+j+1}]: {selisih_maju[i][j]:.8f}")
        print()

    # Menghitung Ytanya menggunakan formula interpolasi Newton
    Ytanya = selisih_maju[0][0]
    for j in range(1, derajat + 1):
        faktor = 1
        for k in range(j):
            faktor *= (Xtanya - X[k])
        Ytanya += selisih_maju[0][j] * faktor

    return Ytanya, selisih_maju

Xtanya = float(input("Masukkan nilai x yang ingin dicari y-nya: "))
derajat = int(input("Masukkan derajat polinom (jumlah titik data - 1): "))
Ytanya, selisih_maju = interpolasi_newton(Xtanya, derajat)
print(f"\nNilai y yang diinterpolasi untuk x = {Xtanya} adalah: {Ytanya}")