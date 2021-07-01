#방법1:x-1, 방법2:x+1, 방법3:2x
#각 방법에 대해서 방법1,2,3계속 탐색
#cnt에서 최소 값 선택
from collections import deque
n,k=map(int, input().split())
max=10**5
depth=[0]*(max+1)
queue=deque([])

def bfs(start):
    queue.append(start)

    while queue:
        now=queue.popleft()
        if now==k:
            print(depth[now])
            break

        else:
            for move in (now-1, now+1, 2*now):
                if 0<=move<=max and depth[move]==0:
                    depth[move]=depth[now]+1
                    queue.append(move)

bfs(n)











    




#문제점: 최단 경로를 찾진 못한다.
# while N!=X:
#     if abs(N-X)>abs(2*N-X):
#         N*=2
#         cnt+=1
#     else:
#         if abs(2*(N+1)-X)>abs(2*(N-1)-X):
#             N-=1
#             cnt+=1
#         else:
#             N+=1
#             cnt+=1

# print(cnt)
