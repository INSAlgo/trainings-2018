import heapq

n = int(input())
li = [int(e) for e in input().split()]
heapq.heapify(li)

cost = 0
while len(li) > 1:
    i1 = heapq.heappop(li)
    i2 = heapq.heappop(li)
    cost += i1 + i2
    heapq.heappush(li, i1 + i2)

print(cost)
