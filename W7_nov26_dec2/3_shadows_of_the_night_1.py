# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
# maximum number of turns before game over.
n = int(input())
# initial position
x, y = [int(i) for i in input().split()]

xm = 0
xM = w
ym = 0
yM = h

# game loop
while True:
    # the direction of the bombs from batman's current location
    # (U, UR, R, DR, D, DL, L or UL)
    bomb_dir = input()

    if "U" in bomb_dir:
        yM = y
        y = (y + ym) // 2
    elif "D" in bomb_dir:
        ym = y
        y = (y + yM) // 2

    if "L" in bomb_dir:
        xM = x
        x = (x + xm) // 2
    elif "R" in bomb_dir:
        xm = x
        x = (x + xM) // 2

    # the location of the next window Batman should jump to.
    print(x, y)
