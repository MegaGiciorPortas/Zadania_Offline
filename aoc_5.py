import sys

flaga = True
intervals = []
counter = 0

for line in sys.stdin:
    line = line.strip()
    if line == "":
        flaga = False
    elif flaga:
        intervals.append(line.split("-"))
    else:
        number = int(line)
        for element in intervals:
            if int(element[0]) <= number <= int(element[1]):
                counter += 1
                break

print(counter)