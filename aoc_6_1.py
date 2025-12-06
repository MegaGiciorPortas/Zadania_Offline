import sys

temporaryList = []
maksLength = 0
for line in sys.stdin:
    temporary_line = line.replace("\n", "")
    if len(temporary_line) > 0:
        temporaryList.append(temporary_line)
        if len(line) > maksLength:
            maksLength = len(line)

tablica = []
for element in temporaryList:
    if len(element) < maksLength:
        tablica.append(element.ljust(maksLength))
    else:
        tablica.append(element)

row = len(tablica)
kolumn = maksLength
symbols = ["+", "*"]

allNumbers = []
allSum = 0
number = ""
operator = ""
for j in range(maksLength - 1, -1, -1):

    isEmpty = True
    for i in range(row):
        if tablica[i][j] != " ":
            isEmpty = False
            break

    if isEmpty:
        if operator == "*":
            result = 1
            for element in allNumbers:
                result *= element
        else:
            result = 0
            for element in allNumbers:
                result += element
        allSum += result
        allNumbers = []
    else:
        for i in range(row - 1):
            number += tablica[i][j]
        allNumbers.append(int(number))
        number = ""
        if tablica[row - 1][j] != " ":
            operator = tablica[row - 1][j]

if operator == "*":
    result = 1
    for element in allNumbers:
        result *= element
else:
    result = 0
    for element in allNumbers:
        result += element
allSum += result
allNumbers = []

print(allSum)
