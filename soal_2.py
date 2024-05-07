def cek_tahun_kabisat(tahun):
    if (tahun % 400 == 0) or (tahun % 4 == 0 and tahun % 100 != 0):
        return True
    else:
        return False

def main():
    tahun = int(input("Masukkan tahun: "))
    
    if cek_tahun_kabisat(tahun):
        print(f"Tahun {tahun} adalah tahun kabisat.")
    else:
        print(f"Tahun {tahun} bukan tahun kabisat.")

if __name__ == "__main__":
    main()
