import sys

batteries = []
for line in sys.stdin:
    batteries.append(list(map(int, line.strip())))  # wczytywanie linii i stworzenie z niej tablicy intow

maxSum = 0
for joltage in batteries:
    a = max(joltage[:-1])  # szukanie najwiekszej mozliwej cyfry dziesiatek
    indeksA = joltage.index(a)
    b = max(joltage[indeksA + 1:]) # szukanie najwiekszej cyfry wystepujacej po naszej cyfrze dziesiatek
    maxSum += a * 10 + b  # dodawanie najwiekszej liczby do wyniku

print(maxSum)
