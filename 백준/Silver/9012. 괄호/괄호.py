import sys 
import collections 
input = sys.stdin.readline

t = int(input())

for i in range(t) :
    a = input().rstrip()
    s = collections.deque()
    flag  = 1
    
    for x in a : 
        if x == '(' :
            s.append(x)
        else : 
            if len(s) > 0:
                s.pop()
            else :
                flag = 0
                break
                
    if flag == 1 and len(s) == 0:
        print("YES")
    else :
        print("NO")