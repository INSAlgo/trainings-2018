cnt = 0


def is_valid(grid, i, j, val):
    """Decide whether a partial candidate breaks the Sudoku rules
    """
    line = grid[i]
    column = [grid[k][j] for k in range(9)]
    square = [grid[3 * (i // 3) + k][3 * (j // 3) + l]
              for k in range(3) for l in range(3)]
    return not (val in line or val in column or val in square)


def backtracking(grid, i, j):
    """Recursive backtracking to solve the given Sudoku
    """
    global cnt
    cnt += 1
    if i == 9:
        return True
    nexti, nextj = (i if j < 8 else i + 1), (j + 1) % 9
    if grid[i][j] != 0:
        return backtracking(grid, nexti, nextj)
    for val in range(1, 10):
        if is_valid(grid, i, j, val):
            grid[i][j] = val
            if backtracking(grid, nexti, nextj):
                return True
            grid[i][j] = 0
    return False


grid = [list(map(int, input().split())) for _ in range(9)]
print("---")
if not backtracking(grid, 0, 0):
    print("Impossible")
else:
    print("\n".join(" ".join(map(str, grid[i])) for i in range(9)))

print("---\nExplored %d candidates" % cnt)
