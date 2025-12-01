import itertools


def zakrecenie_dol(n, reszta, maks):
    if n + reszta == 0:
        return maks + reszta
    if n + reszta > maks:
        return 0 + reszta
    return n + reszta
q = 0

def czy_zgadli(tablica):

    #print("iteracja",q)
    indeks = 0
    if tablica[indeks] == tablica[indeks + 1]:
        return True
    indeks += 1
    reszta = 1
    znak = -1
    flaga = False
    while indeks < len(tablica):
        kolejny = indeks + 1
        if kolejny >= len(tablica):
            kolejny = 0
            flaga = True
        #print("1:",kolejny)
        wartosc = zakrecenie_dol(tablica[kolejny], reszta * znak, len(tablica))
        if wartosc == tablica[indeks]:
            return True
        if flaga:
            break
        indeks += 1
        znak *= -1
        kolejny = indeks + 1

        if kolejny >= len(tablica):
            kolejny = 0
        #print("2:",kolejny)
        wartosc = zakrecenie_dol(tablica[kolejny], reszta * znak, len(tablica))
        if wartosc == tablica[indeks]:
            return True
        reszta += 1
        indeks += 1
        znak *= -1
    return False


def funkcja(n):
    global q
    tablica = [i for i in range(1, n + 1)]
    permutacja = itertools.permutations(tablica)
    print(type(permutacja))
    for p in permutacja:
        if czy_zgadli(p) == False:
            print(p)
        q += 1


funkcja(4)
