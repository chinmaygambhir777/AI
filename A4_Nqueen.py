n = int(input("Enter the number of queens:\t"))

board = [[0]*n for _ in range(n)]

columns = [False] * n
left_diagonal = [False] * (2 * n)
right_diagonal = [False] * (2 * n)

# Print Board
def print_board():

    for row in board:

        for cell in row:

            if cell == 1:
                print("Q", end=" ")

            else:
                print(".", end=" ")

        print()

    print()


# Check Safe Position
def is_safe(row, col):

    for i in range(row):

        # Find queen in previous rows
        for j in range(n):

            if board[i][j] == 1:

                # Same column
                if j == col:
                    return False

                # Diagonal check using formula
                if abs(i - row) == abs(j - col):
                    return False

    return True


# Backtracking Function
def solve(row):

    if row == n:

        print("Solution Found:\n")
        print_board()

        return True

    for col in range(n):

        if is_safe(row, col):

            board[row][col] = 1

            if solve(row + 1):
                return True

            # Backtracking
            board[row][col] = 0

    return False


def solve_bb(row):

    # Base Condition
    if row == n:

        print("Solution Found:\n")
        print_board()

        return True

    # Try every column
    for col in range(n):

        # Check if safe using arrays
        if (columns[col] == False and
            left_diagonal[row - col + n] == False and
            right_diagonal[row + col] == False):

            # Place Queen
            board[row][col] = 1

            # Mark column and diagonals
            columns[col] = True
            left_diagonal[row - col + n] = True
            right_diagonal[row + col] = True

            # Recursive Call
            if solve_bb(row + 1):
                return True

            # Backtracking
            board[row][col] = 0

            columns[col] = False
            left_diagonal[row - col + n] = False
            right_diagonal[row + col] = False

    return False


# Function Call
print("Using Backtracking:\n")
solve(0)

board = [[0]*n for _ in range(n)]
# reset 
print("Using Branch and Bound:\n")
solve_bb(0)
