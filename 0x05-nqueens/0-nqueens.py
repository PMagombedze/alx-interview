import sys

def solveNQueens(n):
    def place(pos, filled):
        for i in range(len(filled)):
            if filled[i] == pos or \
                filled[i] - i == pos - len(filled) or \
                filled[i] + i == pos + len(filled):
                return False
        return True

    def place_queens(n, index, filled, all_solutions):
        if index == n:
            all_solutions.append(filled[:])
            return

        for i in range(n):
            if place(i, filled):
                filled.append(i)
                place_queens(n, index + 1, filled, all_solutions)
                filled.pop()

    all_solutions = []
    place_queens(n, 0, [], all_solutions)
    return all_solutions

def perfect(solutions, n):
    for sol in solutions:
        result = []
        for i in range(n):
            row = ['0'] * n
            row[sol[i]] = '1'
            result.append(row)
        print(result)

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solveNQueens(N)
    perfect(solutions, N)

if __name__ == "__main__":
    main()

