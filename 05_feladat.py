# Számok bekérése a felhasználótól
szamok = []
while True:
    szam = int(input("Adj meg egy pozitív egész számot (negatív a kilépéshez): "))
    if szam < 0:
        break
    szamok.append(szam)

# Legkisebb szám kiírása
if szamok:
    print("A legkisebb megadott szám:", min(szamok))
else:
    print("Nem adtál meg egyetlen pozitív számot sem.")