"""
7. Ispiši vrijednost broja Pi na 4 decimalna mjesta,
    kvadriraj taj broj te ga podijeli s racionalnim brojem odabranim od strane korisnika (input funkcija) i ispiši rezultat.
"""
import math
pi = math.pi
pi4 = float(f"{pi:.4f}")

print(pi)
print(pi4)

kvatrat = math.pow(pi4,2)
nekiBroj = float(input("Unesi neki realni broj: "))
print(f"{kvatrat} / {nekiBroj} = {kvatrat/nekiBroj: .4f}")
