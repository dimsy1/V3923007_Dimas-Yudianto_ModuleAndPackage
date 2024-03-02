import luasDanVolume


while True:
    print("1. Bangun Datar (2D) \n"
        "2. Bangun Ruang (3D)")
    pilih = input("==> Pilih (1/2): ")
    if pilih == "1":
        print("1. Persegi \n"
            "2. Persegi Panjang \n"
            "3. Segitiga \n"
            "4. Lingkaran \n"
            "5. Jajar Genjang \n"
            "6. Trapesium")
        pilih2 = input("==> Pilih Bangun Datar (1/2/3/4/5/6): ")

        if pilih2 == "1":
            sisi = int(input("Masukkan Sisi Persegi: "))
            print("==> Luas Persegi Adalah " + str(luasDanVolume.luasPersegi(sisi)))
            break

        elif pilih2 == "2":
            panjang = int(input("Masukkan Panjang: "))
            lebar = int(input("Masukkan lebar: "))
            print("==> Luas Persegi Panjang Adalah " + str(luasDanVolume.luasPersegiPanjang(panjang, lebar)))
            break

        elif pilih2 == "3":
            alas = int(input("Masukkan Panjang Alas: "))
            tinggi = int(input("Masukkan tinggi: "))
            print("==> Luas Segitiga Adalah " + str(luasDanVolume.luasSegitiga(alas, tinggi)))
            break

        elif pilih2 == "4":
            diameter = int(input("Masukkan diameter: "))
            print("==> Luas Lingkaran Adalah " + str(luasDanVolume.luasLingkaran(diameter)))
            break

        elif pilih2 == "5":
            alas = int(input("Masukkan panjang alas: "))
            tinggi = int(input("Masukkan tinggi: "))
            print("==> Luas Jajar Genjang Adalah " + str(luasDanVolume.luasJajarGenjang(alas, tinggi)))
            break

        elif pilih2 == "6":
            sisi1 = int(input("Masukkan sisi Pertama: "))
            sisi2 = int(input("Masukkan sisi Kedua: "))
            tinggi = int(input("Masukkan tinggi: "))
            print("==> Luas Trapesium Adalah " + str(luasDanVolume.luasTrapesium(sisi1, sisi2, tinggi)))
            break

        else:
            print("==> Mohon Masukkan sesuai Pilihan")
            continue


    
    elif pilih == "2":
        print("1. Kubus \n"
            "2. Balok \n"
            "3. Tabung \n"
            "4. Kerucut \n"
            "5. Limas \n"
            "6. Prisma")
        pilih2 = input("==> Pilih Bangun Ruang (1/2/3/4/5/6): ")
        
        if pilih2 == "1":
            sisi = int(input("Masukkan Sisi Kubus: "))
            print("==> Volume Kubus Adalah " + str(luasDanVolume.volumeKubus(sisi)))
            break

        elif pilih2 == "2":
            panjang = int(input("Masukkan Panjang: "))
            lebar = int(input("Masukkan lebar: "))
            tinggi = int(input("Masukkan tinggi: "))
            print("==> Volume Balok Adalah " + str(luasDanVolume.volumeBalok(panjang, lebar, tinggi)))
            break

        elif pilih2 == "3":
            jariJari = int(input("Masukkan Panjang Jari-Jari: "))
            tinggi = int(input("Masukkan tinggi: "))
            print("==> Volume Tabung Adalah " + str(luasDanVolume.volumeTabung(jariJari, tinggi)))
            break

        elif pilih2 == "4":
            jariJari = int(input("Masukkan Panjang Jari-Jari: "))
            tinggi = int(input("Masukkan tinggi: "))
            print("==> Volume Kerucut Adalah " + str(luasDanVolume.volumeKerucut(jariJari, tinggi)))
            break

        elif pilih2 == "5":
            luasAlas = int(input("Masukkan Luas Alas: "))
            tinggi = int(input("Masukkan tinggi: "))
            print("==> Volume Limas Adalah " + str(luasDanVolume.volumeLimas(luasAlas,tinggi)))
            break

        elif pilih2 == "6":
            luasAlas = int(input("Masukkan Luas Alas: "))
            tinggi = int(input("Masukkan tinggi: "))
            print("==> Volume Limas Adalah " + str(luasDanVolume.volumePrisma(luasAlas, tinggi)))
            break
        
        else:
            print("==> Mohon Masukkan sesuai Pilihan")
            continue


    else:
        print("==> Mohon Masukkan sesuai Pilihan (1/2)")
        continue
