# Cara 1: Menggunakan import modul
import math_operations

# Cara 2 : Menggunakan import fungsi langsung
from math_operations import (
    celsius_ke_fahrenheit, 
    celsius_ke_kelvin, 
    hitung_luas_lingkaran,
    hitung_keliling_lingkaran
)

def main():
    print("=" * 50)
    print("PROGRAM KALKULATOR GEOMETRI DAN KONVERSI SUHU")
    print("=" * 50)

    # Menghitung luas dan keliling bentuk geometri
    print("\n--- KALKULATOR GEOMETRI ---")
    
    # Menggunakan persegi
    sisi_persegi = 5
    luas_persegi = math_operations.hitung_luas_persegi(sisi_persegi)
    keliling_persegi = math_operations.hitung_keliling_persegi(sisi_persegi)
    print(f"\nPersegi dengan sisi {sisi_persegi} satuan:")
    print(f"Luas     = {luas_persegi} satuan persegi")
    print(f"Keliling = {keliling_persegi} satuan")
    
    # Menggunakan persegi panjang
    panjang = 8
    lebar = 4
    luas_pp = math_operations.hitung_luas_persegi_panjang(panjang, lebar)
    keliling_pp = math_operations.hitung_keliling_persegi_panjang(panjang, lebar)
    print(f"\nPersegi panjang dengan panjang {panjang} dan lebar {lebar} satuan:")
    print(f"Luas     = {luas_pp} satuan persegi")
    print(f"Keliling = {keliling_pp} satuan")
    
    # Menggunakan lingkaran (dengan import fungsi langsung)
    jari_jari = 7
    print(f"\nLingkaran dengan jari-jari {jari_jari} satuan:")
    print(f"Luas     = {hitung_luas_lingkaran(jari_jari):.2f} satuan persegi")
    print(f"Keliling = {hitung_keliling_lingkaran(jari_jari):.2f} satuan")
    print(f"Nilai PI yang digunakan: {math_operations.PI}")
    
    # Konversi suhu
    print("\n--- KONVERSI SUHU ---")
    
    # Menggunakan import modul
    suhu_celsius = 25
    print(f"\nSuhu {suhu_celsius}°C sama dengan:")
    print(f"Fahrenheit: {math_operations.celsius_ke_fahrenheit(suhu_celsius):.2f}°F")
    
    # Menggunakan import fungsi langsung
    print(f"Kelvin    : {celsius_ke_kelvin(suhu_celsius):.2f}K")
    
    # Konversi tambahan
    suhu_fahrenheit = 98.6
    suhu_kelvin = 300
    print(f"\nSuhu {suhu_fahrenheit}°F sama dengan {math_operations.fahrenheit_ke_celsius(suhu_fahrenheit):.2f}°C")
    print(f"Suhu {suhu_kelvin}K sama dengan {math_operations.kelvin_ke_celsius(suhu_kelvin):.2f}°C")
    
    print("\n" + "=" * 50)

if __name__ == "__main__":
    main()