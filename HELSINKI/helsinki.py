class Pontszerzo:
    helyezes:int
    sportolok:int
    sportag:str
    versenyszam:str

pontszerzok:list[Pontszerzo] = []

for s in open('HELSINKI\\helsinki.txt'):
    v:list[str] = s.strip().split(' ')
    p = Pontszerzo()
    p.helyezes = int(v[0])
    p.sportolok = int(v[1])
    p.sportag = v[2]
    p.versenyszam = v[3]
    pontszerzok.append(p)

print('3. feladat:')
print(f'pontszerző helyezések száma: {len(pontszerzok)}')

a:int = 0
e:int = 0
b:int = 0
for p in pontszerzok:
    if p.helyezes == 1: a += 1
    elif p.helyezes == 2: e += 1
    elif p.helyezes == 3: b += 1
print('4. feladat:')
print(f'Arany: {a}')
print(f'Ezüst: {e}')
print(f'Bronz: {b}')

oop:int = 0
for p in pontszerzok:
    oop += (7 - p.helyezes)
    if p.helyezes == 1: oop += 1
print('5. feladat:')
print(f'Olimpiai pontok száma: {oop}')

te:int = 0
ue:int = 0
for p in pontszerzok:
    if p.helyezes in {1, 2, 3}:
        if p.sportag == 'torna': te += 1
        elif p.sportag == 'uszas': ue += 1
print('6. feladat:')
if te == ue: print('Egyenlő volt az érmek szám')
else:
    if te > ue: print('Torna', end=' ')
    else: print('Úszás', end=' ')
    print('sportágban szereztek több érmet')

file = open('HELSINKI\\helsinki2.txt', 'w')
for p in pontszerzok:
    op = (7 - p.helyezes)
    if p.helyezes == 1: op += 1
    spa:str = '-'
    if p.sportag == 'kajakkenu': spa = 'kajak-kenu'
    else: spa = p.sportag
    file.write(f'{p.helyezes} {p.sportolok} {op} {spa} {p.versenyszam}\n')

maxi:int = 0
for i in range(1, len(pontszerzok)):
    if pontszerzok[i].sportolok > pontszerzok[maxi].sportolok:
        maxi = i
print('8. feladat:')
print(f'Helyezés: {pontszerzok[maxi].helyezes}')
print(f'Sportág: {pontszerzok[maxi].sportag}')
print(f'Versenyszám: {pontszerzok[maxi].versenyszam}')
print(f'Sportolók száma: {pontszerzok[maxi].sportolok}')