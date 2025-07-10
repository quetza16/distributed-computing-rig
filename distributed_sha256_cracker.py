# ---------------------------------------------
#  Distributed SHA-256 Cracking Simulation Tool
# ---------------------------------------------
# Description:
# This script simulates brute-force cracking of a SHA-256 hash by testing
# numeric values within a defined range. It is designed to be run in a 
# distributed environment where each system works on a different part of
# the keyspace (e.g., node 1 checks 0-100000, node 2 checks 100001-200000).
# Once the correct input is found, the script stops and returns the result.
#
# 🇹🇷 Açıklama:
# Bu script, SHA-256 ile şifrelenmiş bir değeri brute-force (kaba kuvvet)
# yöntemiyle çözmeye yönelik bir simülasyon yapar. Her bilgisayar belirli 
# bir sayı aralığını kontrol ederek, karşılık gelen hash değeri ile eşleşen 
# sayıyı bulmaya çalışır. Dağıtık bir sistemde her bilgisayara farklı aralık 
# verilir. Sonuç bulunduğunda işlem durdurulur ve ekrana yazdırılır.
#
#  Educational purpose only. Do not use this for unauthorized access.
#  Bu kod yalnızca eğitim amaçlıdır. Yetkisiz erişim için kullanılamaz.
# ---------------------------------------------

import hashlib
import time

def crack_sha256(start, end, target_hash):
    print(f"Cracking from {start} to {end}...")
    start_time = time.time()
    for number in range(start, end):
        candidate = str(number).encode()
        hashed = hashlib.sha256(candidate).hexdigest()
        if hashed == target_hash:
            duration = time.time() - start_time
            print(f"[✔] Match found! Number: {number}")
            print(f"[⏱] Time taken: {duration:.2f} seconds")
            return number
    print("[✖] No match found in this range.")
    return None

if __name__ == "__main__":
    print("Distributed SHA-256 Cracker")
    try:
        start = int(input("Start of range: "))
        end = int(input("End of range: "))
        target_hash = input("Target SHA256 hash: ").strip().lower()

        crack_sha256(start, end, target_hash)

    except ValueError:
        print("[!] Invalid input. Please enter valid numbers.")
