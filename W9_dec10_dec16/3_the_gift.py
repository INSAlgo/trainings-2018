n = int(input())
price = int(input())
budgets = [int(input()) for _ in range(n)]

budgets.sort()

contributions = []
for i in range(len(budgets)):
    contributions.append(min(budgets[i], price // (n - i)))
    price -= contributions[-1]

if price:
    print("IMPOSSIBLE")
else:
    print("\n".join(map(str, contributions)))
