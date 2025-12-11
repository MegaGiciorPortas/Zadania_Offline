# Funkcja dystansu (bez zmian)
def distance_between_cans(p1, p2):
    return (p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2 + (p2[2] - p1[2]) ** 2


# Wczytywanie danych
cordinates = []
while True:
    try:
        line = input()
        if not line: break
        cordinates.append(list(map(int, line.strip().split(","))))
    except EOFError:
        break

number_of_cans = len(cordinates)

# 1. Tworzymy WSZYSTKIE możliwe pary (krawędzie)
# Nie filtrujemy ich żadnym "limitem", bo musimy łączyć aż do skutku!
all_edges = []
for i in range(number_of_cans):
    for j in range(i + 1, number_of_cans):
        dist = distance_between_cans(cordinates[i], cordinates[j])
        # Zapisujemy: (dystans, puszka_A, puszka_B)
        all_edges.append((dist, i, j))

# 2. Sortujemy od najkrótszego połączenia
# To ważne! Chcemy łączyć najbliższe puszki najpierw.
all_edges.sort(key = lambda x: x[0])

# 3. System Grup (zamiast BFS)
# Na początku każda puszka jest osobną wyspą.
# Tablica 'grupy' mówi nam, do jakiej wyspy należy puszka.
grupy = []
for i in range(number_of_cans):
    grupy.append(i)  # Puszka 0 ma grupę 0, puszka 1 ma grupę 1...

liczba_osobnych_wysp = number_of_cans

# 4. Lecimy po kablach (od najkrótszego)
for edge in all_edges:
    dystans = edge[0]
    puszka_a = edge[1]
    puszka_b = edge[2]

    id_grupy_a = grupy[puszka_a]
    id_grupy_b = grupy[puszka_b]

    # Jeśli puszki są w RÓŻNYCH grupach, to znaczy, że ten kabel jest potrzebny,
    # żeby połączyć dwie osobne wyspy w jedną większą.
    if id_grupy_a != id_grupy_b:

        # Łączymy! "Przemalowujemy" wszystkie puszki z grupy B na grupę A
        # (To jest mniej wydajne niż 'Union Find', ale prostsze do napisania w szkole)
        for k in range(number_of_cans):
            if grupy[k] == id_grupy_b:
                grupy[k] = id_grupy_a

        liczba_osobnych_wysp -= 1  # Mamy o jedną wyspę mniej

        # 5. Sprawdzamy czy to już koniec
        if liczba_osobnych_wysp == 1:
            # Sukces! Wszystko jest połączone. To był ostatni kabel.
            # Wyciągamy współrzędne X
            x1 = cordinates[puszka_a][0]
            x2 = cordinates[puszka_b][0]

            print(x1 * x2)
            break  # Kończymy program