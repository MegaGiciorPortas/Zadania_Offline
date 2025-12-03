import sys

batteries = []
for line in sys.stdin:
    batteries.append(list(map(int, line.strip())))  # wczytywanie linii i stworzenie z niej tablicy intow

maxSum = 0
for joltage in batteries:
    N = len(joltage)
    number = 0
    counter = 0
    start = 0
    while counter <= 11:
        meta = -11 + counter
        a = max(joltage[start:N + meta])
        start = joltage.index(a,start) + 1
        number = number * 10 + a
        counter += 1

    maxSum += number

print(maxSum)

