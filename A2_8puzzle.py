# Goal State
goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]
# Possible moves
directions = [
    (-1, 0),  # UP
    (1, 0),   # DOWN
    (0, -1),  # LEFT
    (0, 1)    # RIGHT
]

# Function to calculate heuristic
# Counts misplaced tiles
def heuristic(state):

    misplaced = 0

    for i in range(3):
        for j in range(3):

            if state[i][j] != 0 and state[i][j] != goal[i][j]:
                misplaced += 1

    return misplaced


# Function to find blank space
def find_blank(state):

    for i in range(3):
        for j in range(3):

            if state[i][j] == 0:
                return i, j


# Function to print puzzle
def print_state(state):

    for row in state:
        print(row)

    print()


# A* Algorithm
def a_star(start):

    current = start

    moves = 0
    print("Current State:")
    print_state(current)

    while heuristic(current) != 0:

        x, y = find_blank(current)

        best_state = None
        best_h = 999

        # Try all moves
        for dx, dy in directions:

            nx = x + dx
            ny = y + dy

            # Check valid move
            if 0 <= nx < 3 and 0 <= ny < 3:

                # Create copy of puzzle
                new_state = [row[:] for row in current]

                # Swap blank with neighbor
                new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]

                h = heuristic(new_state)

                # Select best move
                if h < best_h:
                    best_h = h
                    best_state = new_state

        current = best_state
        moves += 1
        print("Next State:")
        print("Step : ", moves)
        print_state(current)

    print("Goal State Reached:")
    print_state(current)

    print("Total Moves =", moves)


# Initial State
start = [
    [1, 2, 3],
    [0, 4, 6],
    [7, 5, 8]
]

# Function Call
a_star(start)
