from collections import deque


def truckTour(petrolpumps):
    n = len(petrolpumps)
    if n == 0:
        return 0
    c = petrolpumps[0][0]
    dq = deque([0])
    i = 0
    while True:
        i = (i + 1) % n
        dq.append(i)
        c -= petrolpumps[(i - 1) % n][1]
        while c < 0:
            j = dq.popleft()
            c -= petrolpumps[j][0]
            c += petrolpumps[j][1]
        c += petrolpumps[i][0]
        if dq[0] == dq[-1] and len(dq) > 1:
            break
    return dq[0]
