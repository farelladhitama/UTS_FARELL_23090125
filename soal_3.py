def hitung_total_harga(harga_barang):
    total = sum(harga_barang)
    return total

def main():
    jumlah_barang = int(input("Masukkan jumlah barang: "))
    
    harga_barang = []
    for i in range(jumlah_barang):
        harga = float(input(f"Masukkan harga barang ke-{i+1}: "))
        harga_barang.append(harga)
    
    total_harga = hitung_total_harga(harga_barang)
    print("Total harga belanjaan:", total_harga)

if __name__ == "__main__":
    main()
