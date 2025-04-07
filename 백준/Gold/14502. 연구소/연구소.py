from itertools import combinations #iterable에서 원소 개수가 r개인 조합 뽑기 
from copy import deepcopy

dxs = [0,0,1,-1]
dys = [1,-1,0,0]

N, M = map(int, input().split())
W = 3 

arr = [] 
for i in range(N):
    arr.append(list(map(int,input().split())))

def cnt_sf(_arr):
    _cnt = 0
    for _i in range(N):
        for _j in range(M):
            if _arr[_i][_j] == 0:
                _cnt += 1
    return _cnt
def virus_spread(x,y):
    if arr[x][y] == 2:
        for dx,dy in zip(dxs,dys):
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < M :
                if arr[nx][ny] == 0:
                    arr[nx][ny] = 2
                    virus_spread(nx,ny)
empty_space = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            empty_space.append((i,j))
pos = combinations(empty_space,W)
answer = 0
tmp = deepcopy(arr)

for state in pos :
    arr = deepcopy(tmp)
    for x,y in state:
        arr[x][y] = 1
    for i in range(N):
        for j in range(M):
            virus_spread(i,j)
    answer = max(answer, cnt_sf(arr))
print(answer)