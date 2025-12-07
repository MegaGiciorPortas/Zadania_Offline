import sys


def how_many_splits(zbior):
    if len(zbior) == 0:
        return 0
    wynik = 0
    for i in range(1, len(zbior)):
        if zbior[i - 1][1] + 2 == zbior[i][1]:
            wynik += 1
    return wynik


def laczenie_zbiorow(A, B):
    result = set()
    for element in A:
        result.add(element)
    for element in B:
        result.add(element)
    return result


board = []

for line in sys.stdin:
    board.append(list(line.strip()))

rows = len(board)
kolumns = len(board[0])

i = 0
j = board[0].index("S")
meta = 0

current_locations = set()
current_locations.add((i, j))
result = 0
new_locations = set()
while meta < rows - 1:
    new_locations = set()
    for element in current_locations:
        i = element[0]
        j = element[1]
        if board[i + 1][j] == ".":
            new_locations.add((i + 1, j))
        else:
            result += 1
            if j - 1 >= 0:
                new_locations.add((i + 1, j - 1))
            if j + 1 < kolumns:
                new_locations.add((i + 1, j + 1))
    current_locations = new_locations
    meta += 1

print(result)
