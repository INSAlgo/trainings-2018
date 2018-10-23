width = int(input())
height = int(input())
grid = [input() for _ in range(height)]

neighbors = {(i, j): [(-1, -1), (-1, -1)]
             for i in range(height)
             for j in range(width)}
prev_in_col = [None] * width
prev_in_line = [None] * height
for i in range(height):
    for j in range(width):
        if grid[i][j] == "0":
            if prev_in_col[j] is not None:
                neighbors[(prev_in_col[j], j)][1] = (i, j)
            prev_in_col[j] = i
            if prev_in_line[i] is not None:
                neighbors[(i, prev_in_line[i])][0] = (i, j)
            prev_in_line[i] = j

for (i, j), ((i2, j2), (i3, j3)) in neighbors.items():
    if grid[i][j] == "0":
        print(j, i, j2, i2, j3, i3)
