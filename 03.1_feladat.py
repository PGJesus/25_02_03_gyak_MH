"""3.1 Feladat
Írj egy programot, amely tartalmaz egy 'harommal_oszthatok' nevű függvényt, amely a paraméterként átvett listában megvizsgálja, hogy hány darab 
hárommal osztható szám van, és ezzel az értékkel tér vissza! A program tartalmazza a függvény hívását is!"""

def harommal_oszthatok(szamok):
    darab = 0
    for szam in szamok:
        if szam % 3 == 0:
            darab += 1
    return darab

print(harommal_oszthatok([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


"""3.2 Feladat
Alakítsd át az előző programot úgy, hogy a felhasználó által megadott számokat tárolja el a program egy listában, és ezt értékelje ki a 
függvény! (Az adatbeolvasás addig tartson, míg a felhasználó negatív számot nem ad meg!)"""

def div_by_3(szamok):
    darab = 0
    for szam in szamok:
        if szam % 3 == 0:
            darab += 1
    return darab

szamok = []
while True:
    szam = int(input("Adj meg egy számot: "))
    if szam < 0:
        break
    szamok.append(szam)

print(div_by_3(szamok))