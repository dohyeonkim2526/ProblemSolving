import sys
from collections import deque
n,m,v=map(int,input().split())
mat=[[0]*(n+1) for _ in range(n+1)]
visited=[0]*(n+1) #visited=[0,0,0...0]
 
for _ in range(m):
    x,y=map(int,sys.stdin.readline().split())
    mat[x][y]=mat[y][x]=1

def bfs(start):
    queue=deque([start])
    visited[start]=1
    while queue:
        start=queue.popleft()
        print(start, end=' ')
        for i in range(1,n+1):
            if mat[start][i]==1 and visited[i]==0:
                queue.append(i)
                visited[i]=1
    
bfs(v)            