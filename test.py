n,m,v=map(int,input().split())
mat=[[0]*(n+1) for _ in range(n+1)]
visit=[0]*(n+1)

for i in range(m):
    x,y=map(int, input().split())
    mat[x][y]=mat[y][x]=1

def dfs(start):
    visit[start]=1
    print(start, end=' ')
    for i in range(1,n+1):
        if visit[i]==0 and mat[start][i]==1:
            dfs(i)

dfs(v)