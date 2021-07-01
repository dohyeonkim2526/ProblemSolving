n,m,v=map(int,input().split())
mat=[[0]*(n+1) for _ in range(n+1)]
visit=[0]*(n+1)

for i in range(m):
    x,y=map(int, input().split())
    mat[x][y]=mat[y][x]=1

def bfs(start):
    queue=[start]
    visit[start]=1

    while queue:
        start=queue.pop(0)
        print(start, end=' ')
        for i in range(1,n+1):
            if visit[i]==0 and mat[start][i]==1:
                queue.append(i)
                visit[i]=1

bfs(v)
