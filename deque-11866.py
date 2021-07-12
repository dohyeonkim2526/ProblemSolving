from collections import deque
N,K=map(int, input().split())
queue=deque([i for i in range(1,N+1)])
ans=[]

# for _ in range(N):
#     if len(queue)==K-1:
#         print(queue[0], queue[1], sep=', ', end='')
#         print('>')
#         break
#     print(queue[K-1], end=', ')
#     queue.remove(queue[K-1])
#     queue.rotate(-(K-1))

while queue:
    queue.rotate(-(K-1))
    q=queue.popleft()
    ans.append(q)

print('<'+', '.join(map(str,ans))+'>')