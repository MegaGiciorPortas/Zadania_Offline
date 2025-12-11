import sys

cordinates = []
for line in sys.stdin:
    cordinates.append(tuple(map(int,tuple(line.strip().split(",")))))

areas = []
N = len(cordinates)

for i in range(N):
    x1 = cordinates[i][0]
    y1 = cordinates[i][1]
    for j in range(i+1,N):
        x2 = cordinates[j][0]
        y2 = cordinates[j][1]

        a = abs(x1-x2) + 1
        b = abs(y1-y2) + 1

        areas.append(a*b)

areas.sort(reverse = True)
print(areas[0])