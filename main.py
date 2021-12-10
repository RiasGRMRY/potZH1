class Fuvar:

    def __init__(self,nap:int,fsz:int,km:int):
        self.nap = nap
        self.fsz = fsz
        self.km = km

def Feladat1(filepath:str,mode:str)->list:
    print("1. feladat: A tavok.txt beolvasása.")
    adatok=[]
    inputTavok = open(filepath,mode)
    sor= inputTavok.readline().strip()
    while(sor!=""):
        SpT = sor.split(' ')
        adatok.append(Fuvar(int(SpT[0]),int(SpT[1]),int(SpT[2])))
        sor= inputTavok.readline().strip()
    inputTavok.close()
    return adatok
def Feladat2(adatok:list):
    for i in adatok:
        if i.nap==1 and i.fsz ==1:
            print(f"2. feladat: A hét első útja {i.km} km.")
            break

def Feladat3(adatok:list):
    nap = int(input("3. feladat: Adja meg a nap sorszámát (1-7): "))
    fsz = int(input("Adja meg a fuvar sorszámát (1-40): "))
    for i in adatok:
        if i.nap == nap and i.fsz ==fsz:
            print(f"A {nap}. nap {fsz}. fuvarához {i.km} km került rögzítésre.")
            return
    print("Nincs ilyen fuvar.")

def Feladat4(adatok:list):
    munkanap=[]
    s=""
    for i in adatok:
        try:
            munkanap.index(i.nap)
        except Exception:
            munkanap.append(i.nap)
    for i in range(1,8):
        try:
            munkanap.index(i)
        except Exception:
            s+=str(i)+", "
    print(f"4. feladat: A futár nem dolgozott ezen nap(ok)on: {s[:-2]}")

def Feladat5(adatok:list):
    napi={}
    max =0
    for i in range(1,8):
        napi[i]=0
    for i in adatok:
        napi[i.nap]+=1
    for i in range(1,7):
        if napi[i]>max:
            max = i
    print(f"5. feladat: Ezen nap(ok)on volt a maximális számú fuvar: {max}")

def Feladat6(adatok:list):
    print("6. feladat:")
    napi={}
    max =0
    for i in range(1,8):
        napi[i]=0
    for i in adatok:
        napi[i.nap]+=i.km
    for i in range(1,8):
        print(f"\t{i}. nap: {napi[i]} km")

def Feladat78(filepath:str,mode:str,adatok:list):
    print("7. feladat: Fuvarok ellenértékének meghatározása.")
    napok=[]
    sum=0
    txtOutput=open(filepath,mode)
    index=1
    while(index<8):
        napiUtak=[]
        for i in adatok:
            if i.nap == index:
                napiUtak.insert(i.fsz-1,f"{index}. nap {i.fsz}. ut: {i.km*300} Ft\n")
                sum+=i.km*300
        napok.append(napiUtak)
        index+=1
    for i in napok:
        for y in i:
            txtOutput.write(y)
    txtOutput.close()
    print(f"8. feladat: A futár heti fizetése {sum} Ft.")
adatok=Feladat1("tavok.txt","r")
Feladat2(adatok)
Feladat3(adatok)
Feladat4(adatok)
Feladat5(adatok)
Feladat6(adatok)
Feladat78("dijazas.txt","w",adatok)


