from math import ceil

li = list(map(int, input().split()))

k = 1
while k < len(li):
    # li is k-sorted, now we want it 2k-sorted

    # we merge the blocks of size k, 2 by 2
    for i in range(ceil(len(li) / (2 * k))):
        temp = []
        p2 = (2 * i + 1) * k
        if p2 < len(li):
            p1 = 2 * i * k
            l1 = p2
            l2 = min(2 * (i + 1) * k, len(li))
            while p1 < l1 and p2 < l2:
                if li[p1] < li[p2]:
                    temp.append(li[p1])
                    p1 += 1
                else:
                    temp.append(li[p2])
                    p2 += 1
            temp += li[p1:l1] + li[p2:l2]
            li[2*i*k:l2] = temp
    k = 2 * k

print(li)
