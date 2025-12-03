import sys


def incorrectID(n):
    N = len(n)
    length = 1
    while length <= N // 2:
        if N % length == 0:  # sprawdzenie czy dlugosc mojego wzorca dzieli bez reszty dlugosc calego napisu
            pattern = n[:length]  # jezeli tak to wyznaczam wzorzec
            k = N // length  # obliczam ile razy mam powtorzyc swoj wzorzec aby mial taka sama dlugosc jak liczba
            if pattern * k == n:
                return True
        length += 1
    return False


for line in sys.stdin:
    extents = line.split(",")

incorrectSum = 0
for interval in extents:
    values = interval.split("-")
    for digit in range(int(values[0]), int(values[1]) + 1):  # przechodzenie po całym przedziale
        if incorrectID(str(digit)): # sprawdzenie czy ID jest niepoprawne
            incorrectSum += digit  # dodawanie blednego ID do sumy


print(incorrectSum)
