import sys
from _collections import defaultdict

def how_many_splits(zbior):
    if len(zbior) == 0:
        return 0
    wynik = 0
    for i in range(1, len(zbior)):
        if zbior[i - 1][1] + 2 == zbior[i][1]:
            wynik += 1
    return wynik

board = []

for line in sys.stdin:
    board.append(list(line.strip()))

rows = len(board)
kolumns = len(board[0])

i = 0
j = board[0].index("S")

current_kolumn = defaultdict(int)
current_kolumn[j] = 1
meta = 0

while meta < rows - 1:
    next_kolumn = defaultdict(int)

    for k, wartosc in current_kolumn.items():
        i = meta
        j = k

        if not board[i+1][j] == "^":
            next_kolumn[j] += wartosc
        else:
            if j-1 >= 0:
                next_kolumn[j-1] += wartosc
            if j+1 < kolumns:
                next_kolumn[j+1] += wartosc

    current_kolumn = next_kolumn
    meta += 1

print(sum(current_kolumn.values()))
