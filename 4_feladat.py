"""4. Feladat
Írj egy programot, amelyben van egy 'kerulet' nevű függvény, amely az egyetlen kötelező paramétere mellett fogadhat több paramétert is! Az 
opcionális paraméterek száma alapján döntse el milyen síkidomról van szó, és számolja ki a kerületét (0 tetszőleges paraméter: négyzet, 1 
tetszőleges paraméter: téglalap, 2 tetszőleges paraméter: háromszőg, 3 vagy több tetszőleges paraméter: sokszög)!

A program tartalmazzon mindegyik síkidom típusra egy-egy függvényhívást!"""

def kerulet(alap, *args):
    if len(args) == 0:
        # Négyzet kerülete (alap * 4)
        return 4 * alap
    elif len(args) == 1:
        # Téglalap kerülete (2 * (alap + args[0]))
        return 2 * (alap + args[0])
    elif len(args) == 2:
        # Háromszög kerülete (összeg)
        return alap + args[0] + args[1]
    else:
        # Sokszög kerülete (összeg)
        return alap + sum(args)

def legkisebb_szam(lista):
    return min(lista)

# Függvényhívások minden síkidomra
print("Négyzet kerülete:", kerulet(5))
print("Téglalap kerülete:", kerulet(5, 10))
print("Háromszög kerülete:", kerulet(3, 4, 5))
print("Sokszög kerülete:", kerulet(3, 4, 5, 6, 7))

