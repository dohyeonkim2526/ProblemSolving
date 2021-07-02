#dx,dy 좌,우,위,아래
#2<=m,n<=10**3
#조건 -1이 있으면 이동하지 못함 + 최대값 출력
import sys
from collections import deque
M,N=map(int, sys.stdin.readline().split())
box=[]
queue=deque()
dx=[1,-1,0,0]
dy=[0,0,1,-1]
ans=0

for i in range(N):
    s=list(map(int, sys.stdin.readline().split()))
    box.append(s)
    for j in range(M):
        if s[j]==1:
            queue.append([i,j]) #1위치 확인

while queue:
    nx,ny=queue.popleft()
    for i in range(4):
        mx,my=nx+dx[i],ny+dy[i]
        if 0<=mx<N and 0<=my<M and box[mx][my]==0:
            box[mx][my]=box[nx][ny]+1
            queue.append([mx,my])

for i in range(N):
    if 0 in box[i]: ans-=1

print(box[nx][ny]-1 if ans>=0 else -1)

# if 0 in box:
#     print(-1)
# else:
#     arr=[]
#     m=max(box)
#     for i in range(M):
#         arr.append(m[i])
#     print(max(arr)-1)

# for i in range(N):
#     for j in range(M):
#         print(box[i][j], end=' ')
#     print()

# if 0 in box:
#     print(-1)
# else:
#     print(box[nx][ny]-1)

# for x in range(N):
#     for y in range(M):
#         if box[x][y]==1:
#             queue.append([x,y])
#             while queue:
#                 nx,ny=queue.popleft()
#                 for i in range(4):
#                     mx,my=nx+dx[i],ny+dy[i]
#                     if 0<=mx<N and 0<=my<M and box[mx][my]==0:
#                         queue.append([mx,my])
#                         box[mx][my]=box[nx][ny]+1

# if 0 in box:
#     print(-1)

# else:
#     print(max(box))
     




