class Kategoria:
    nev:str
    tulelok:int
    eltuntek:int

kategoriak:list[Kategoria] = []

for sor in open('titanic.txt'):
    darabok:list[str] = sor.strip().split(';')
    kat = Kategoria()
    kat.nev = darabok[0]
    kat.tulelok = int(darabok[1])
    kat.eltuntek = int(darabok[2])
    kategoriak.append(kat)

print(f'2. feladat: {len(kategoriak)} db')

osszes_szemely:int = 0
for k in kategoriak:
    osszes_szemely += (k.tulelok + k.eltuntek)
print(f'3. feladat: {osszes_szemely} fő')

ksz:str = input('4. feladat: Kulcsszó: ')
i:int = 0
while i < len(kategoriak) and ksz not in kategoriak[i].nev:
    i += 1
if i < len(kategoriak):
    print('\tVan találat!')
    print('5. feladat:')
    for k in kategoriak:
        if ksz in k.nev:
            print(f'\t{k.nev} {k.tulelok + k.eltuntek} fő')
else:
    print('\tNincs találat!')

print('6. feladat:')
for k in kategoriak:
    if k.eltuntek > (k.eltuntek + k.tulelok) * .6:
        print(f'\t{k.nev}')

maxi:int = 0
for i in range(1, len(kategoriak)):
    if kategoriak[i].tulelok > kategoriak[maxi].tulelok:
        maxi = i
print(f'7. feladat: {kategoriak[maxi].nev}')