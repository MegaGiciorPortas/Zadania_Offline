import sys


def able_to_take(T, w, k):
    result = 0
    # [w-1,k-1] [w-1,k] [w-1,k+1]
    # [w,k-1] [w,k] [w,k+1]
    # [w+1,k-1] [w+1,k] [w+1,k+1]
    pattern = ['@', 'x']

    rowUp = False
    if w + 1 < len(T): rowUp = True
    rowDown = False
    if w - 1 >= 0: rowDown = True
    kolumnUp = False
    if k + 1 < len(T): kolumnUp = True
    kolumnDown = False
    if k - 1 >= 0: kolumnDown = True

    if rowUp:
        if T[w + 1][k] in pattern:
            result += 1
        if kolumnUp:
            if T[w + 1][k + 1] in pattern:
                result += 1
        if kolumnDown:
            if T[w + 1][k - 1] in pattern:
                result += 1
    if kolumnUp:
        if T[w][k + 1] in pattern:
            result += 1
        if rowDown:
            if T[w - 1][k + 1] in pattern:
                result += 1
    if kolumnDown:
        if T[w][k - 1] in pattern:
            result += 1
        if rowDown:
            if T[w - 1][k - 1] in pattern:
                result += 1
    if rowDown:
        if T[w - 1][k] in pattern:
            result += 1

    return result < 4


board = []
for line in sys.stdin:
    board.append(list(line.strip()))

counter = 0
for i in range(len(board)):
    for j in range(len(board)):
        if board[i][j] == '@':
            if able_to_take(board, i, j):
                counter += 1
                board[i][j] = 'x'

print(counter)
