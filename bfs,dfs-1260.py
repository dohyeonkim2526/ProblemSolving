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

dfs(v)
print()
visit=[0]*(n+1)
bfs(v)


# def dfs(start,arr):
#     next=1000 #정점의 개수 (1<=n<=1000)
#     for node in arr:
#         if node[0]==start:
#             next=min(next,node[1])
#     print(start, end=' ')
    
#     for i in range(n):
#         for node in arr:
#             if node[0]==next:
#                 next=min(next, node[1])
#         print(next, end=' ')

# def dfs(start,arr):
#     ns=[]
#     for node in arr:
#         if node[0]==start:
#             ns.append(node[1])
#         next=min(ns)
#         print(start, end=' ')
    
#     ns=[]
#     for node in arr:
#         if node[0]==next:
#             ns.append(node[1])
#         next=min(ns)

# def dfs(start,arr,count):
#     if count==5:
#         return
#     ns=[]
#     for node in arr:
#         if node[0]==start:
#             ns.append(node[1])
#     next=min(ns)
#     print(start, end=' ')
#     count+=1
#     dfs(next,nodes,count)

# def dfs(start,arr,count):
#     if count==5:
#         return
#     ns=[]
#     for node in arr:
#         if start in node:
#             next=(node[1] if node.index(start)==0 else node[0])
#             ns.append(next)
#     next=min(ns)
#     print(start, end=' ')

#     count+=1
#     dfs(next,nodes,count)

# dfs(v,nodes,count)