import SudokuBoard as sb

def main():

    sBoard = [
        [0, 0, 0, 7, 9, 0, 0, 5, 0],
        [3, 5, 2, 0, 0, 8, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 1, 0, 0, 7, 0, 0, 0, 4],
        [6, 0, 0, 3, 0, 1, 0, 0, 8],
        [9, 0, 0, 0, 8, 0, 0, 1, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 5, 0, 0, 8, 9, 1],
        [0, 8, 0, 0, 3, 7, 0, 0, 0]
    ]
    sb.solve(sBoard)
    sb.printBoard(sBoard)

if __name__ == "__main__":
    main()