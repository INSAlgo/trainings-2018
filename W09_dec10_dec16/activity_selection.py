n = int(input())
activities = [(lambda s: (s[0], int(s[1]), int(s[2])))(input().split())
              for _ in range(n)]
activities.sort(key=lambda x: x[2])

selected = [activities[0][0]]
latest_f = activities[0][2]
for name, s, f in activities[1:]:
    if s >= latest_f:
        selected.append(name)
        latest_f = f

print(" ".join(selected))
