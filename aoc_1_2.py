import sys

actual_indeks = 50
last_indeks = 50
counter = 0

for linia in sys.stdin:
    line = linia.strip()

    number = int(line[1:])
    zeros_per_instruction = number // 100
    residue = number % 100

    if line[0] == "R":
        for _ in range(residue):
            actual_indeks += 1
            if actual_indeks == 100:
                actual_indeks = 0
                zeros_per_instruction += 1
    else:
        for _ in range(residue):
            actual_indeks -= 1
            if actual_indeks == -1:
                actual_indeks = 99
            if actual_indeks == 0:
                zeros_per_instruction += 1
    counter += zeros_per_instruction

print(counter)
