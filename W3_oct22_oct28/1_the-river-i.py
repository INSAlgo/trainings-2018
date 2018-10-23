r1 = int(input())
r2 = int(input())


def nextnb(r):
    return r + sum(int(digit) for digit in str(r))


while r1 != r2:
    if r1 < r2:
        r1 = nextnb(r1)
    else:
        r2 = nextnb(r2)

print(r1)
