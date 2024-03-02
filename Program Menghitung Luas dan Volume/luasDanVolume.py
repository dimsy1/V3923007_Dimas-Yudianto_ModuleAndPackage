import math

# Bangun Datar
def luasPersegi(sisi):
    luas = sisi ** 2
    return luas

def luasPersegiPanjang(panjang, lebar):
    luas = panjang * lebar
    return luas

def luasSegitiga(alas, tinggi):
    luas = alas * tinggi / 2
    return luas

def luasLingkaran(diameter):
    luas = math.pi * (diameter / 2) ** 2
    return luas

def luasJajarGenjang(alas, tinggi):
    luas = alas * tinggi
    return luas
    
def luasTrapesium(sisi1, sisi2, tinggi):
    luas = tinggi * (sisi1 + sisi2) / 2
    return luas


# Bangun Ruang
def volumeKubus(sisi):
    volume = sisi ** 3
    return volume

def volumeBalok(panjang, lebar, tinggi):
    volume = panjang * lebar * tinggi
    return volume

def volumeTabung(jariJari, tinggi):
    volume = math.pi * (jariJari ** 2) * tinggi
    return volume

def volumeKerucut(jariJari, tinggi):
    volume = math.pi * (jariJari ** 2) * tinggi / 3
    return volume

def volumeLimas(luasAlas, tinggi):
    volume = luasAlas * tinggi / 3
    return volume

def volumePrisma(luasAlas, tinggi):
    volume = luasAlas * tinggi
    return volume
