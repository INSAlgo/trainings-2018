import sys
import math
import queue
def show(q):
    r=q.qsize()
    l=[]
    for k in range(r):
        l.append(q.get())
    print(str(r)+" "+str(l))
    for k in range(r):
        q.put(l[k])
def tour(l1,l2):
    v1=q1.get()
    v2=q2.get()
    l1.append(v1)
    l2.append(v2)
    #print(l1,l2)
    if(v1>v2):
        for i in range(len(l1)):
            q1.put(l1[i])
        for i in range(len(l1)):
            q1.put(l2[i])
    elif(v1<v2):
        for i in range(len(l1)):
            q2.put(l1[i])
        for i in range(len(l1)):
            q2.put(l2[i])
    else:
        return war(l1,l2)
    return False
        
            
def war(l1,l2):
    end=0
    for i in range(3):
        if(not q1.empty()):
            l1.append(q1.get())
        else:
            end=1
            break
        if(not q2.empty()):
            l2.append(q2.get())
        else:
            end=1
            break
    
    if(q1.empty() or q2.empty()):
        end=1
    if(end==0):
        return tour(l1,l2)
    else:return True
val={"2":0,"3":1,"4":2,"5":3,"6":4,"7":5,"8":6,"9":7,"10":8,"J":9,"Q":10,"K":11,"A":12}
n = int(input())  # the number of cards for player 1
q1=queue.Queue()
for i in range(n):
    c1 = input()  # the n cards of player 1
    q1.put(val[c1[:-1]])
m = int(input())  # the number of cards for player 2
q2=queue.Queue()
for i in range(m):
    c2 = input()  # the m cards of player 2
    q2.put(val[c2[:-1]])
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
end=0
i=0
while(not(q1.empty() or q2.empty()) and end==0):
    if(i<0):
        print(i)
        show(q1)
        show(q2) 
    end=tour(list(),list())
    i+=1
if(end):print("PAT")
else:
    play=1
    if(q1.qsize()==0):play=2
    print(play,i)
