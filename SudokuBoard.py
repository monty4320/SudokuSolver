def solve(board):
    """
    Uses backtracking recursion method to fill Sudoku table
    :param board:
    :return:
    """
    pos = findEmpty(board)
    if pos:
        (row, col) = pos
    else:
        return True

    for i in range(1,10):
        if isValid(board, (row, col), i):
            board[row][col] = i
            if solve(board):
                return True
            board[row][col] = 0
    return False

def findEmpty(board):
    """
    Returns the tuple coordinates of first empty element of the Sudoku table, by row-major order

    :param board:
    :return tuple location of empty element, or None:
    """
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                return i, j
    return None

def isValid(board, coord, num):
    """
    Verifies that the element at coord = (row,col) is unique in its box, vertical, and horizontal

    :param board:
    :param coord = (row, col):
    :param num:
    :return:
    """
    row = coord[0]
    col = coord[1]
    # check vertical
    for i in range(len(board)):
        if board[i][col] == num and i != row:
            return False

    # check horizontal
    for i in range(len(board)):
        if board[row][i] == num and i != col:
            return False

    #check 3x3
    x = col//3
    y = row//3

    for i in range(y*3, (y+1)*3):
        for j in range(x*3,(x+1)*3):
            if board[i][j] == num and (i, j) != coord:
                return False
    return True


def printBoard(board):
    for line in board:
        print(*line)