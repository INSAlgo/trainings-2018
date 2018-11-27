def mergesort(li):
    if len(li) == 1:
        return li
    mid = len(li) // 2
    left = li[:mid]
    right = li[mid:]
    left = mergesort(left)
    right = mergesort(right)

    p1 = 0
    p2 = 0
    newli = []
    while p1 < len(left) and p2 < len(right):
        if left[p1] < right[p2]:
            newli.append(left[p1])
            p1 += 1
        else:
            newli.append(right[p2])
            p2 += 1
    newli += left[p1:len(left)] + right[p2:len(right)]
    return newli


li = list(map(int, input().split()))
print(mergesort(li))
