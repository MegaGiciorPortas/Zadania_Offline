import sys

memory = {}
dictionary = {}


def count_paths(current_position):
    if current_position == "out":
        return 1

    if current_position in memory.keys():
        return memory[current_position]

    result = 0
    currentDirections = dictionary[current_position]

    for direction in currentDirections:
        result += count_paths(direction)

    memory[current_position] = result

    return result


dictionary = {}
for line in sys.stdin:
    tablica = line.strip().split()
    tablica[0] = tablica[0][:-1]
    dictionary.setdefault(tablica[0], [])
    for element in tablica[1:]:
        dictionary[tablica[0]].append(element)

print(count_paths('you'))