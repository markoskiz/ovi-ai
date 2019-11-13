import copy

tabla = [['_','_','_','_','_','_','_'],
['_','_','_','_','_','_','_'],
['_','_','_','_','_','_','_'],
['_','_','_','_','_','_','_'],
['_','_','_','_','_','_','_'],
['_','_','_','_','_','_','_'],]

zCov='o'
zKom='x'


def CrtajTabla(tabla):
    """Funkcija za iscrtuvanje na "povrzi 4" tabla vo konzola"""
    print (" 1 2 3 4 5 6 7 ")
    for row in tabla:
        print ("| ",end="")
        for element in row:
            print (element,' ',end="")
        print ("|")


def CitajKorisnik(tabla):
    """Funkcija koja za vnesuvanje na potegot na korisnikot preku
    standardniot vlez i generiranje na tabla od istata informacija"""
    j=eval(input('Vnesi poteg (1-7):'))-1
    return GenerirajTabla(j,tabla,zCov)


def GenerirajTabla(j,tabla,z):
    """Funkcija koja prima broj na kolona i generira celosna
tabla"""
    if tabla[0][j]!='_':
        return tabla
    tabla_test=tabla[:]
    tabla_test.append(['-','-','-','-','-','-','-'])
    for i in range(len(tabla)-1,-1,-1):
        if (tabla_test[i][j] == '_') and (tabla_test[i+1][j] !='_'):
            tabla[i][j]=z
            break
    return tabla


def VratiSiteMozni(tabla,z,vratikolona=False):
    """Funkcija koja zavisno od vrednosta na z gi vrakja site mozni naredni porezi, ili za covekot ili za kompjuterot."""
    listPotezi=[]
    a=[]
    cpy_tabla=copy.deepcopy(tabla)
    tabla_test=copy.deepcopy(tabla)
    tabla_test.append(['-','-','-','-','-','-','-'])
    for j in range(7):
        for i in range(len(tabla),-1,-1):
            if (tabla_test[i][j] == '_') and (tabla_test[i+1][j]!= '_'):
                cpy_tabla[i][j]=z
                a=copy.deepcopy(cpy_tabla)
                if vratikolona:
                    listPotezi.append([a,j])
                else:
                    listPotezi.append(a)
                cpy_tabla[i][j]='_'
                break
    return copy.deepcopy(listPotezi)


def ProveriPobeda(tabla,z):
    """Funkcija koja vrakja ocena za situacijata na tablata"""
    suma=0
    #Ocenuvanje na koloni
    for i in range(3):
        for j in range(7):
            if (tabla[i][j]==z and tabla[i+1][j] == z and tabla[i+2][j]==z and tabla[i+3][j]==z):
                return True
    #Ocenuvanje na redovi
    for i in range(6):
        for j in range(4):
            if (tabla[i][j]==z and tabla[i][j+1] == z and tabla[i][j+2]==z and tabla[i][j+3]==z):
                return True
    #Ocenuvanje na desna dijagonala
    for i in range(3):
        for j in range(4):
            if (tabla[i][j]==z and tabla[i+1][j+1] == z and tabla[i+2][j+2]==z and tabla[i+3][j+3]==z):
                return True
    #Ocenuvanje na leva dijagonala
    for i in range(3):
        for j in range(3,7):
            if (tabla[i][j]==z and tabla[i+1][j-1] == z and tabla[i+2][j-2]==z and tabla[i+3][j-3]==z):
                return True
    return False


def MinM(tabla,depth):
    if ProveriPobeda(tabla,zKom):
        return 1000000
    list_cov_poteg=VratiSiteMozni(tabla,zCov,False)
    minVred=1000000
    if depth==0:
        minVred=min(map(lambda x: Heuristika(x,zKom),list_cov_poteg))
    else:
        for poteg in list_cov_poteg:
            maxPot=MaxM(poteg,depth-1)
            if maxPot<minVred:
                minVred=maxPot
    return minVred


def MaxM(tabla,depth):
    if ProveriPobeda(tabla,zCov):
        return -1000000
    list_cov_poteg=VratiSiteMozni(tabla,zKom,False)
    maxVred=-1000000
    if depth==0:
        maxVred=max(map(lambda x: Heuristika(x,zCov),list_cov_poteg))
    else:
        for poteg in list_cov_poteg:
            minPot=MinM(poteg,depth-1)
            if minPot>maxVred:
                maxVred=minPot
    return maxVred


def PredvidiPoteg(tabla,depth):
    """ Funkcija koja go vrakja potegot kojsto go igra kompjuterot"""
    list_naredni=VratiSiteMozni(tabla,zKom,vratikolona=True)
    tablaa=copy.deepcopy(list_naredni[0][0])
    kolona=0
    maxVred=-1000000
    for pozicija in list_naredni:
        if ProveriPobeda(pozicija[0],zKom):
            a=1000000
        else:
            a=MinM(pozicija[0],depth)
        print ("Kolona ", pozicija[1]+1,',ocena :', a)
        if a>maxVred:
            tablaa=copy.deepcopy(pozicija[0])
            kolona=pozicija[1]
            maxVred=a
    return tablaa


def Heuristika(tabla,z):
    """Funkcija koja vrakja ocena za situacijata na tablata"""
    # Tuka treba da stoi vashiot kod !
    return ocena


CrtajTabla(tabla)
while True:
    # Tuka vsusnost se igra igrata
    # Neka covekot e prv na poteg
    tabla=CitajKorisnik(tabla)
    CrtajTabla(tabla)
    if ProveriPobeda(tabla,zCov):
        print ("Bravo! Go pobedi kompjuterot!")
        break
    tabla=PredvidiPoteg(tabla,4)
    CrtajTabla(tabla)
    if ProveriPobeda(tabla,zKom):
        print ("Kraj na igrata! Pobeda za kompjuterot!")
        break
