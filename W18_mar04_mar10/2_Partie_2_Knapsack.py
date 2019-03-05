c,n = map(int,input().split())
obj = list()
for k in range(n) : 
    obj.append(list(map(int,input().split())))
knap = [[0 for i in range(c+1)] for j in range(2)]
used = set()
used.add(0)
for k in range(n):
    toAppend = list()
    for p in used :
        knap[(k+1)%2][p] = max(knap[(k+1)%2][p],knap[(k)%2][p])
        # try to add the current object if possible
        if( p + obj[k][1] <= c ):
            knap[(k+1)%2][p+obj[k][1]] = max(knap[k%2][p+obj[k][1]],knap[k%2][p] + obj[k][0])
            toAppend.append(p+obj[k][1])
    for e in toAppend:
        used.add(e)
print(max(max(knap[0]),max(knap[1])))
