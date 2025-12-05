import sys

flaga = True
intervals = []

for line in sys.stdin:
    line = line.strip()
    if line == "":
        break
    else:
        intervals.append(list(map(int, line.split("-"))))

intervals = sorted(intervals, key = lambda x: x[0])

current_start = intervals[0][0]
current_meta = intervals[0][1]
counter = 0

for element in intervals[1:]:
    if current_meta >= element[0]:
        current_meta = max(element[1],current_meta)
    else:
        # An = A1 + (n-1)*r
        # An - A1 + 1 = n
        counter += current_meta - current_start + 1
        current_start = element[0]
        current_meta = element[1]

counter += current_meta - current_start + 1
print(counter)
