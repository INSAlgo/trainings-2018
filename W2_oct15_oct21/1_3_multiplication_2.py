# version 1
a, b = input().split()
a, b = int(a), int(b)
print(a * b)

# version 2
a, b = map(int, input().split())
print(a * b)

# version 3
a, b = [int(i) for i in input().split()]
print(a * b)
