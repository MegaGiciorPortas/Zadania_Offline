import sys


def incorrectID(n):
    N = len(n)
    if N % 2 == 1: return False # wykluczamy liczby ktore nie maja parzystej liczby cyfr
    half = N // 2
    return n[:half] == n[half:] # sprawdzamy czy pierwsza polowa liczby jest rowna drugiej


for line in sys.stdin:
    extents = line.split(",")

incorrectSum = 0
for interval in extents:
    values = interval.split("-")
    for digit in range(int(values[0]), int(values[1]) + 1): # przejscie po wszystkich liczbach z przedzialu
        if incorrectID(str(digit)):
            incorrectSum += digit # dodawnie niepoprawnych ID do sumy

print(incorrectSum)
