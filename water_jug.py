#water_jug
MAX_CAPACITY_JUG1 = 4
MAX_CAPACITY_JUG2 = 3
TARGET = 2

def solve_water_jug_problem():
    jug1 = 0  # initial amount of water in jug1
    jug2 = 0  # initial amount of water in jug2
    path = []  # to store the solution path

    while jug2 != TARGET:
        path.append((jug1, jug2))

        # if jug2 is empty, fill it to full
        if jug2 == 0:
            jug2 = MAX_CAPACITY_JUG2

        # if jug1 is already full, empty it
        if jug1 == MAX_CAPACITY_JUG1:
            jug1 = 0

        # pour water from jug2 to jug1 until either jug1 gets full or jug2 gets empty
        while jug1 != MAX_CAPACITY_JUG1 and jug2 != 0:
            jug1 += 1
            jug2 -= 1

        # empty jug1 if it gets full
        if jug1 == MAX_CAPACITY_JUG1:
            jug1 = 0

    # add final state of jug1 and jug2 to the solution path
    path.append((jug1, jug2))
    return path

solution_path = solve_water_jug_problem()

# print the solution path
for jug1, jug2 in solution_path:
    print(f"Jug1: {jug1} gallon, Jug2: {jug2} gallon")