def sudoku(puzzle):
    '''
    a function that will solve a 9x9 Sudoku puzzle.
    The function will take one argument consisting of
    the 2D puzzle array, with the value 0 representing
    an unknown square.
    Solution for the easy sudokus, solvable by brute force.
    '''
    # base case: return result if no 0 left
    if 0 not in set([v for r in puzzle for v in r]):
        return puzzle
    # iterate over every 0 value in the sudoku
    for row in range(len(puzzle)):
        for i, val in enumerate(puzzle[row]):
            if val == 0:
                # grab the column in which we check
                col = list(zip(*puzzle))[i]
                sq_row = (row // 3)*3
                sq_col = (i // 3)*3
                # grab the square in which we check
                square = [puzzle[i][j] for i in range(sq_row,3+sq_row) for j in range(sq_col,3+sq_col)]
                # iterate over every possible input
                for candidate in range(0, 10):
                    # validate input
                    if row_ok(candidate, puzzle[row]) and col_ok(candidate, col) and square_ok(candidate, square):
                        # if validated fill as value and continue
                        puzzle[row][i] = candidate
                        # if reached the filled validated sudoku - return
                        if sudoku(puzzle):
                            return sudoku(puzzle)
                        # otherwise backtrack
                        else:
                            puzzle[row][i] = 0
                # if iterated over all possible candidates and no continuation - must backtrack
                return False

def row_ok(entry, row):
    return not (entry in row)

def col_ok(entry, col):
    return not (entry in col)

def square_ok(entry, square):
    return not (entry in square)
