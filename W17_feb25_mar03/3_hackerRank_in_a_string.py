target = "hackerrank"
for k in range(int(input())):
    pos_target = 0
    pos_source = 0
    source = input()
    while pos_target!=len(target) and pos_source!=-1 :
        pos_source = source.find(target[pos_target], pos_source)
        if pos_source!=-1:
            pos_source+=1
        pos_target+=1
    if pos_source == -1 :
        print("NO")
    else:
        print("YES")