# version 1
n = int(input())
l = list(map(int, input().split()))

product = 1
for i in l:
    product *= l

print(product)

# version 2
n = int(input())
product = 1
for i in input().split():
    product *= int(i)
print(product)
