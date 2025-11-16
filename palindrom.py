def czy_to_palindrom(napis):
    N = len(napis)
    for i in range(N // 2):
        if napis[i] != napis[N - 1 - i]:
            return False
    return True


def main_function(T):
    podciagi = []
    N = len(T)

    # DODAWANIE WIERSZY
    for i in range(N):
        napis = "".join(T[i])
        podciagi.append(napis)

    # DODAWANIE KOLUMN
    for i in range(N):
        napis = ""
        for wiersz in range(N):
            napis += T[wiersz][i]
        podciagi.append(napis)

    # DODAWANIE PRZEKATNYCH
    # przekatna (lg-pd)
    # glowna przekatna i wszystko ponizej
    for start in range(N - 4):
        napis = ""
        indeks = 0
        while indeks < N - start:
            napis += T[start + indeks][indeks]
            indeks += 1
        podciagi.append(napis)

    # wszysktkie powyzej glownej przekatnej
    for start in range(1, N - 4):
        napis = ""
        indeks = 0
        while indeks < N - start:
            napis += T[indeks][start + indeks]
            indeks += 1
        podciagi.append(napis)

    # przekatna (pg-ld)
    # glowna przekatna i wszystko powyzej
    for start in range(N - 1, 3, -1):
        kolumna = start
        wiersz = 0
        napis = ""
        while wiersz < N and kolumna >= 0:
            napis += T[wiersz][kolumna]
            wiersz += 1
            kolumna -= 1
        podciagi.append(napis)

    # wszystkie ponizej glownej przekatnej
    for start in range(N - 2, 3, -1):
        kolumna = start
        wiersz = 1
        napis = ""
        while wiersz < N and kolumna >= 0:
            napis += T[wiersz][kolumna]
            wiersz += 1
            kolumna -= 1
        podciagi.append(napis)

    # biore kazdy podciag i sprawdzam go pod katem palindrommow
    # dla kazdego palindroma ktory znajde tworze slownik i przypisuje wartosc 1
    palindromy = {}

    for ciag in podciagi:
        if czy_to_palindrom(ciag):
            palindromy.setdefault(ciag, 0)
            palindromy[ciag] += 1

            if palindromy[ciag] == 2:
                return ciag

        n = len(ciag)
        for dlugosc in range(n - 1, 4, -1):
            indeks = 0
            while indeks + dlugosc <= n:
                podciag = ciag[indeks:indeks + dlugosc]

                if czy_to_palindrom(podciag):
                    palindromy.setdefault(podciag, 0)
                    palindromy[podciag] += 1

                    if palindromy[podciag] == 2:
                        return podciag

                indeks += 1

    return None


N = int(input(""))
T = []
for _ in range(N):
    napis = input("")
    T.append(list(napis))
print(main_function(T))
