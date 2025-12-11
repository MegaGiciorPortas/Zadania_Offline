import sys
from collections import deque


def switching_lights(current, button):
    current = list(current)
    for indeks in button:
        if current[indeks] == 0:
            current[indeks] = 1
        else:
            current[indeks] = 0
    return tuple(current)


tablica = []
for line in sys.stdin:
    wiersz = line.strip().split(" ")
    tablica.append(wiersz[:-1])

mainSum = 0
for line in tablica:
    goal = line[0]
    goal = goal.replace(".", "0").replace("#", "1")
    goal = tuple(list(map(int, list(goal[1:-1]))))

    starting_situation = tuple([0] * len(goal))
    buttons = []
    for button in line[1:]:
        value = button[1:-1]
        buttons.append(tuple(map(int, value.split(","))))

    queue = deque()
    queue.append((starting_situation, 0))
    visited = set()
    visited.add(starting_situation)

    while queue:
        current_situation, moves = queue.popleft()

        if current_situation == goal:
            mainSum += moves
            break

        for button in buttons:
            new_situation = switching_lights(current_situation, button)
            if new_situation not in visited:
                queue.append((new_situation, moves + 1))
                visited.add(new_situation)

print(mainSum)
