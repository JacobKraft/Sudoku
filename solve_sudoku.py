
def find_empty(arr, loc):
    for x in range(9):
        for y in range(9):
            if arr[x][x] == 0:
                loc[0] = x
                loc[1] = y
                return True
    return False


def check_box(arr, row, col, temp):
    for x in range(3):
        for y in range(3):
            if arr[x+row][y+col] == temp:
                return False
    return True


def check_col(arr, col, num):
    for i in range(9):
        if arr[i][col] == num:
            return False
    return True


def check_row(arr, row, num):
    for i in range(9):
        if arr[row][i] == num:
            return False
    return True


def check_valid(arr, row, col, num):
    return not check_box(arr, row, col, num) and not check_col(arr, col, num) and not check_row(arr, row, num)


def solver(arr):
    loc = [0, 0]
    if not find_empty(arr, loc):
        return True
    row = loc[0]
    col = loc[1]
    for num in range(1, 10):
        check_valid(arr, row, col, num)
    return False


if __name__ == '__main__':
    # creating a 2D array for the grid
    grid = [[0 for x in range(9)] for y in range(9)]

    # assigning values to the grid
    grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
            [5, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 8, 7, 0, 0, 0, 0, 3, 1],
            [0, 0, 3, 0, 1, 0, 0, 8, 0],
            [9, 0, 0, 8, 6, 3, 0, 0, 5],
            [0, 5, 0, 0, 9, 0, 6, 0, 0],
            [1, 3, 0, 0, 0, 0, 2, 5, 0],
            [0, 0, 0, 0, 0, 0, 0, 7, 4],
            [0, 0, 5, 2, 0, 6, 3, 0, 0]]
    solver(grid)
