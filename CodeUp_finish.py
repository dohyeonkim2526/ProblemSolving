#6064번
a,b,c=map(int, input().split())
print((a if (a<b) else b) if ((a if (a<b) else b)<c) else c)


#6081번
a=int(input(),16)
for i in range(1,16):
    print('%X*%X=%X' % (a,i,a*i))

#6096번
#repr(): 해당 객체를 만들 수 있는 문자열로 출력한다.
#<요약> if문 최대한 간단하게 적어보자.

board=[list(map(int, input().split()))for _ in range(19)]
n=int(input())

for i in range(n):
    a,b=map(int, input().split())

    for j in range(19):
        board[a-1][j]=(1 if board[a-1][j]==0 else 0)
        board[j][b-1]=(1 if board[j][b-1]==0 else 0)

for i in board:
    print(" ".join(repr(j) for j in i))



#6098
#0:개미가 움직이는 경로, 1:장애물, 2:먹이
#(x,y)
#개미가 오른쪽으로 이동(x+1,y), 아래쪽으로 이동(x,y+1)
#<요약> 오른쪽이 0,2일 경우 모두 이동한다. 장애물만 생각해서 조건문을 잘못 설정했었다.

m=[[]*10 for _ in range(10)]    
for i in range(10):
    m[i]=list(map(int, input().split()))

x,y=1,1
m[1][1]=9

while True:
    if m[x][y]==2:
        m[x][y]=9
        break
    if m[x][y+1]!=1:
        m[x][y]=9
        y+=1
    else:
        if m[x+1][y]!=1:
            m[x][y]=9
            x+=1
        else:
            m[x][y]=9
            break
      
for i in range(10):
    for j in range(10):
        print(m[i][j],end=' ')
    print()




