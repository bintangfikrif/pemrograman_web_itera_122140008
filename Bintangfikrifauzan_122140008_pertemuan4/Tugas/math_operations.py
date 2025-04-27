# Modul untuk operasi matematika geometri dan konversi suhu

# Konstanta
PI = 3.14159

# Fungsi geometri
def hitung_luas_persegi(sisi):
    """Menghitung luas persegi"""
    return sisi * sisi

def hitung_keliling_persegi(sisi):
    """Menghitung keliling persegi"""
    return 4 * sisi

def hitung_luas_persegi_panjang(panjang, lebar):
    """Menghitung luas persegi panjang"""
    return panjang * lebar

def hitung_keliling_persegi_panjang(panjang, lebar):
    """Menghitung keliling persegi panjang"""
    return 2 * (panjang + lebar)

def hitung_luas_lingkaran(jari_jari):
    """Menghitung luas lingkaran"""
    return PI * jari_jari * jari_jari

def hitung_keliling_lingkaran(jari_jari):
    """Menghitung keliling lingkaran"""
    return 2 * PI * jari_jari

# Fungsi konversi suhu
def celsius_ke_fahrenheit(celsius):
    """Mengkonversi suhu dari Celsius ke Fahrenheit"""
    return (celsius * 9/5) + 32

def celsius_ke_kelvin(celsius):
    """Mengkonversi suhu dari Celsius ke Kelvin"""
    return celsius + 273.15

def fahrenheit_ke_celsius(fahrenheit):
    """Mengkonversi suhu dari Fahrenheit ke Celsius"""
    return (fahrenheit - 32) * 5/9

def kelvin_ke_celsius(kelvin):
    """Mengkonversi suhu dari Kelvin ke Celsius"""
    return kelvin - 273.15