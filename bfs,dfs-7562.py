# #테스트 케이스 개수만큼 반복 -> 그 안에서 3줄의 input 받음
# #나이트가 이동할 수 있는 좌표 리스트 생성
# #1번째 input
# #체스 한 변의 길이 x-> mat (x by x) 메트랙스 생성
# #visited 확인할 x by x 매트릭스 생성

# #2~3번째 input
# #queue가 비워질 때 까지 반복
# #이동할 때 마다 1씩 증가
# #visited가 1인지 확인 -> before = new+1
# #모든 반복문 종료하고 3번째 input의 길이 반환

import sys
from collections import deque
case=int(input())
dx=[2,2,1,1,-1,-1,-2,-2]
dy=[1,-1,2,-2,2,-2,1,-1]


def bfs(x,y,x_end,y_end):
    queue=deque()
    queue.append([x,y])
    visited[x][y]=1

    while queue:
        nx,ny=queue.popleft()
        if nx==x_end and ny==y_end:
            print(visited[nx][ny]-1)
            break

        for i in range(8):
            mx=nx+dx[i]
            my=ny+dy[i]
            if 0<=mx<I and 0<=my<I and visited[mx][my]==0:
                visited[mx][my]=visited[nx][ny]+1
                queue.append([mx,my])


for _ in range(case):
    
    I=int(sys.stdin.readline())
    sx,sy=map(int,sys.stdin.readline().split())
    ex,ey=map(int,sys.stdin.readline().split())
    
    visited=[[0]*I for _ in range(I)]

    bfs(sx,sy,ex,ey)






# 오답
# import sys
# from collections import deque
# case=int(input())
# dx=[2,2,1,1,-1,-1,-2,-2]
# dy=[1,-1,2,-2,2,-2,1,-1]
# queue=deque()


# def bfs(x,y,c):
#     queue.append([x,y])
#     visited[x][y]=1

#     while queue:
#         now=queue.popleft()
#         nx,ny=now[0],now[1]

#         for i in range(8):
#             mx=nx+dx[i]
#             my=ny+dy[i]
#             if 0<=mx<=(c-1) and 0<=my<=(c-1) and visited[mx][my]==0:
#                 mat[mx][my]=mat[nx][ny]+1
#                 visited[mx][my]=1
#                 queue.append([mx,my])
#     return mat[arr[2][0]][arr[2][1]]


# for _ in range(case):
#     arr=[]
#     for i in range(3):
#         s=list(map(int,sys.stdin.readline().split()))
#         arr.append(s)
    
#     I=arr[0][0]
#     mat=[[0]*I for _ in range(I)]
#     visited=[[0]*I for _ in range(I)]

#     print(bfs(arr[1][0],arr[1][1],I))