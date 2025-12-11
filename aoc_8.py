import sys
from collections import defaultdict


def distance_between_cans(p1, p2):
    return (p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2 + (p2[2] - p1[2]) ** 2


# [x,y,z]
cordinates = []
for line in sys.stdin:
    cordinates.append(list(map(int, line.strip().split(","))))

number_of_cans = len(cordinates)
possible_pairs = []
for i in range(number_of_cans):
    for j in range(i + 1, number_of_cans):
        distance = distance_between_cans(cordinates[i], cordinates[j])
        possible_pairs.append((distance, i, j))

possible_pairs.sort(key = lambda x: x[0])

graf = defaultdict(list)

for k in range(1000):
    graf[possible_pairs[k][1]].append(possible_pairs[k][2])
    graf[possible_pairs[k][2]].append(possible_pairs[k][1])

visited_cans = set()
size_of_trees = []

for i in range(number_of_cans):
    if i not in visited_cans:
        kolejka = []
        kolejka.append(i)
        visited_cans.add(i)
        current_size = 0

        while len(kolejka) > 0:
            current = kolejka.pop(0)
            current_size += 1

            next_cans = graf[current]
            for element in next_cans:
                if element not in visited_cans:
                    visited_cans.add(element)
                    kolejka.append(element)

        size_of_trees.append(current_size)

size_of_trees.sort(reverse = True)
print(size_of_trees[0] * size_of_trees[1] * size_of_trees[2])
