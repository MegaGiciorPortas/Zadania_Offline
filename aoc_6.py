import sys

tablica = []
operations = []
iterator = 0
for line in sys.stdin:
    linia = line.strip().split()
    if linia[0] == "+" or linia[0] == "*":
        operations = linia
    else:
        iterator += 1
        tablica.append(list(map(int, linia)))

mainSum = 0
for i in range(len(operations)):
    if operations[i] == '+':
        result = 0
        for j in range(iterator):
            result += tablica[j][i]
    else:
        result = 1
        for j in range(iterator):
            result *= tablica[j][i]
    mainSum += result
print(mainSum)
