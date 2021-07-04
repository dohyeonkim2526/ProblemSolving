#(1,1)에서 출발 -> (N,M)도착하기 위해 지나야 하는 최소 칸의 수
#시작, 도착 위치도 포함
#tip: 좌,우,위,아래 좌표가 연결된 노드라고 생각하기
import sys
from collections import deque

N,M=map(int,input().split())
mat=[[0]*(M+1) for _ in range(N+1)]

# print()
# for i in range(N+1):
#     for j in range(M+1):
#         print(mat[i][j], end=' ')
#     print()

for i in range(N):
    s=sys.stdin.readline()
    for j in range(M):
        mat[i+1][j+1]=int(s[j])   

# for i in range(N+1):
#     for j in range(M+1):
#         print(mat[i][j], end=' ')
#     print()    

queue=deque()
visited=[[0]*(M+1) for _ in range(N+1)]

def bfs(x,y):
    queue.append([x,y])
    visited[x][y]=1
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]

    while queue:
        start=queue.popleft()
        for i in range(4):
            x=start[0]+dx[i]
            y=start[1]+dy[i]
            if 1<=x<=N and 1<=y<=M:
                if (mat[x][y]==1) and (visited[x][y]==0):
                    mat[x][y]+=mat[start[0]][start[1]]
                    visited[x][y]=1            
                    queue.append([x,y])
    return mat[N][M]
    
print(bfs(1,1))

# print()
# for i in range(N+1):
#     for j in range(M+1):
#         print(mat[i][j], end=' ')
#     print()