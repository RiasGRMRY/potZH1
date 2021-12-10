# Pót ZH1

## Feladat megoldása és benyújtás

1. Nyissa meg:
   1. _VCS / Get from Version Control..._ VAGY
   2. _Git / Clone..._
2. A _Get From Version Control_ ablakban adja meg a jelen repository URL-jét: https://github.com/csekok/potZH1.git
3. Kattintson a _Clone_ gombra.
4. Válassza a _Git / GitHub / Share Project on GitHub_ lehetőséget.
5. Kattintson a _Project Is Already on GitHub_ ablakban a _Share Anyway_ gombra.
6. Kattintson a _Share Project On GitHub_ ablakban a _Share_ gombra.
7. A feladat megoldására 3 óra áll rendelkezésre.
8. A feladat befejezésekor, de legkésőbb a 3. óra leteltekor kommitolja fel a megoldást.

## Feladatkiírás

Egy kerékpáros futárszolgálat a futárjainak a megtett utak alapján ad fizetést.
Az egyik futár egy héten át feljegyezte fuvarjai legfontosabb adatait, és azokat eltárolta egy
állományban. Az állományban az adatok rögzítése nem mindig követi az időrendi sorrendet.
Azokra a napokra, amikor nem dolgozott, nincsenek adatok bejegyezve az állományba.

A fájlban minden sor egy-egy út adatait tartalmazza egymástól szóközzel elválasztva.
Az első adat a nap sorszáma, ami 1 és 7 közötti érték lehet. A második szám a napon belüli fuvarszám.
Ez minden nap 1-től kezdődik, és az aznapi utolsó fuvarig egyesével növekszik. A harmadik szám az adott fuvar során
megtett utat jelenti kilométerben, egészre kerekítve.

Példa a _tavok.txt_ fájl első néhány sorára:
<pre>
1 7 14
3 3 10
1 1 3
1 2 3
1 3 1
</pre>

A 3. sor például azt mutatja, hogy a hét 1. napján az 1. fuvar 3 kilométeres távolságot jelentett.

Írjon programot az alábbi feladatok megoldására:
1. Olvassa be a _tavok.txt_ állományban talált adatokat, s annak felhasználásával oldja meg
a következő feladatokat!
2. Írja ki a képernyőre, hogy mekkora volt a hét legelső útja kilométerben! Figyeljen arra,
hogy olyan állomány esetén is helyes értéket adjon, amiben például a hét első napján
a futár nem dolgozott!
3. Kérje be a felhasználótól egy nap és egy fuvar sorszámát, majd írassa ki, mekkora távolság
tartozik a fuvarhoz! Ha nem volt ilyen fuvar a fájlban, akkor írja ki, hogy "Nincs ilyen fuvar."!
4. Tudjuk, hogy a futár minden héten tart legalább egy szabadnapot. Írja ki a képernyőre,
hogy a hét hányadik napjain nem dolgozott a futár!
5. Írja ki a képernyőre, hogy a hét melyik napján volt a legtöbb fuvar! Amennyiben több nap
is azonos, maximális számú fuvar volt, elegendő ezek egyikét kiírnia.
6. Számítsa ki és írja a képernyőre a mintának megfelelően, hogy az egyes napokon hány
kilométert kellett tekerni! 
7. A futár az egyes utakra az út hosszától függően kap fizetést: 300 Ft/km. Határozza meg az összes
rögzített út ellenértékét! Ezeket az értékeket írja ki a _dijazas.txt_ állományba nap szerint,
azon belül pedig az út sorszáma szerinti növekvő sorrendben az alábbi formátumban: _1. nap 1. út: 900 Ft_!
8. Határozza meg, és írja ki a képernyőre, hogy a futár mekkora összeget kap a heti munkájáért!

### Megoldás közben ügyeljen az alábbiakra

- A képernyőre írást igénylő részfeladatok eredményének megjelenítése előtt írja a képernyőre a feladat sorszámát!
- Ha a felhasználótól kér be adatot, jelenítse meg a képernyőn, milyen értéket vár!
- Ellenőrizze a felhasználó által megadott adatok helyességét, érvényességét!

### Minta a szöveges kimenetek kialakításához

A képernyőre írást nem igénylő feladatok esetén nem szükséges a feladat sorszámát sem kiíratnia.

#### Teszteset 1

<pre>
1. feladat: A tavok.txt beolvasása.
2. feladat: A hét első útja 3 km.
3. feladat: Adja meg a nap sorszámát (1-7): második
Adja meg a fuvar sorszámát (1-40): nyolcadik
Nincs ilyen fuvar.
4. feladat: A futár nem dolgozott ezen nap(ok)on: 2, 6
5. feladat: Ezen nap(ok)on volt a maximális számú fuvar: 5.
6. feladat:
	1. nap: 65 km
	2. nap: 0 km
	3. nap: 69 km
	4. nap: 62 km
	5. nap: 74 km
	6. nap: 0 km
	7. nap: 75 km
7. feladat: Fuvarok ellenértékének meghatározása.
8. feladat: A futár heti fizetése 103500 Ft.
</pre>

#### Teszteset 2

<pre>
1. feladat: A tavok.txt beolvasása.
2. feladat: A hét első útja 3 km.
3. feladat: Adja meg a nap sorszámát (1-7): 3
Adja meg a fuvar sorszámát (1-40): 40
Nincs ilyen fuvar.
4. feladat: A futár nem dolgozott ezen nap(ok)on: 2, 6
5. feladat: Ezen nap(ok)on volt a maximális számú fuvar: 5.
6. feladat:
	1. nap: 65 km
	2. nap: 0 km
	3. nap: 69 km
	4. nap: 62 km
	5. nap: 74 km
	6. nap: 0 km
	7. nap: 75 km
7. feladat: Fuvarok ellenértékének meghatározása.
8. feladat: A futár heti fizetése 103500 Ft.
</pre>

#### Teszteset 3

<pre>
1. feladat: A tavok.txt beolvasása.
2. feladat: A hét első útja 3 km.
3. feladat: Adja meg a nap sorszámát (1-7): 1
Adja meg a fuvar sorszámát (1-40): 7
A 1. nap 7. fuvarához 14 km került rögzítésre.
4. feladat: A futár nem dolgozott ezen nap(ok)on: 2, 6
5. feladat: Ezen nap(ok)on volt a maximális számú fuvar: 5.
6. feladat:
	1. nap: 65 km
	2. nap: 0 km
	3. nap: 69 km
	4. nap: 62 km
	5. nap: 74 km
	6. nap: 0 km
	7. nap: 75 km
7. feladat: Fuvarok ellenértékének meghatározása.
8. feladat: A futár heti fizetése 103500 Ft.
</pre>

#### Példa a _dijazas.txt_ fájl első néhány sorára:
<pre>
1. nap 1. út: 900 Ft
1. nap 2. út: 900 Ft
1. nap 3. út: 300 Ft
1. nap 4. út: 2700 Ft
1. nap 5. út: 1500 Ft
1. nap 6. út: 600 Ft
1. nap 7. út: 4200 Ft
1. nap 8. út: 2700 Ft
1. nap 9. út: 2400 Ft
1. nap 10. út: 1500 Ft
1. nap 11. út: 1800 Ft
</pre>
