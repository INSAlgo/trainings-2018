for k in range(int(input())):
    m = int(input())
    n = int(input())
    f = list(map(int,input().split()))
    for i in range(n):
        for j in range(i+1,n):
            if(f[i]+f[j] == m):
                print(i+1,j+1)
                break
