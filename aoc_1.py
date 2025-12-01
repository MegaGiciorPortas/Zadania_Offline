import sys

actual_indeks = 50
counter = 0

for linia in sys.stdin:
    line = linia.strip()

    if line[0] == "R":  # sprawdzenie czy idziemy w prawo czy w lewo
        number = int(line[1:])
        actual_indeks = (actual_indeks + (number % 100)) % 100
    else:
        number = int(line[1:])
        actual_indeks = (actual_indeks - (number % 100)) % 100

    # jezeli actual_indeks == 0 to oznacza ze wlasnie stoimy na polu 0
    if actual_indeks == 0:
        counter += 1

print(counter)
