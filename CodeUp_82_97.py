#6082번
a=int(input())

for i in range(1,a+1):
  if i//10 in (3,6,9):
    print('X', end='')
    if i%10 in (3,6,9):
      print('X', end=' ')
    else:
      print(end=' ')
  
  elif i%10 in (3,6,9):
    print('X', end=' ')
  
  else:
    print(i, end=' ')

#6083번
r,g,b=input().split()
r=int(r)
g=int(g)
b=int(b)
count=0

for pr in range(r):
  for pg in range(g):
    for pb in range(b):
      count+=1
      print(pr, pg, pb, sep=' ')

print(count)

#6084번
h,b,c,s=input().split()
h=int(h)
b=int(b)
c=int(c)
s=int(s)

memory=h*b*c*s/(8*1024*1024)
print(format(memory,'.1f')+' MB')

#6088번
a,d,n=input().split()
a=int(a)
d=int(d)
n=int(n)

for i in range(1,n):
  a+=d

print(a)

#6089번
a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
d=1

while d%a!=0 or d%b!=0 or d%c!=0:
  d+=1

print(d)

#6092번
n=int(input())
a=input().split()
d=[]

for i in range(n):
  a[i]=int(a[i])
  d.append(a[i])

for i in range(1,24):
  count=0
  for j in range(len(d)):
    if i==d[j]:
      count+=1
    else:
      continue
  print(count,end=' ')

#6095번
n=int(input())
nums=[]

for i in range(n):
  x,y=input().split()
  nums.append([int(x),int(y)])

d=[[0 for j in range(20)] for i in range(20)]

for i in range(len(nums)):
  r=nums[i][0]
  h=nums[i][1]
  d[r-1][h-1]=1

for i in range(len(d)-1):
  for j in range(len(d)-1):
    print(d[i][j], end=' ')
  print()


#6097-수정전
h,w=input().split()
M=[[0 for i in range(int(w))] for j in range(int(h))]

n=int(input())
N=[]
for i in range(n):
  a=list(map(int, input().split()))
  N.append(a)

S=[]
for j in range(n):
  s=[]
  l=N[j][0]
  d=N[j][1]
  x=N[j][2]-1
  y=N[j][3]-1

  if d==0: #가로방향
     s.append([x,y])
     for i in range(1,l):
       y+=1
       s.append([x,y])
     S.append(s)
               
  elif d==1: #세로방향
     s.append([x,y])
     for i in range(1,l):
       x+=1
       s.append([x,y])
     S.append(s)

for i in range(len(S)):
  r=S[i]
  for j in range(len(r)):
    a=r[j][0]
    b=r[j][1]
    M[a][b]=1
  
for i in range(int(h)):
  for j in range(int(w)):
    print(M[i][j], end=' ')
  print()

#계속 오류가 났던 이유: for문의 변수와 내부 변수의 이름('d')이 같아서 계속 오류가 생겼다.
#변수명이 중복되지 않도록 조심하자!

#6097-수정후
h,w=map(int, input().split())
n=int(input())

M=[[0]*w for _ in range(h)]


for i in range(n):
  l,d,x,y=map(int, input().split())

  if d==0:
    for j in range(l):
      M[x-1][y-1+j]=1

  else:
    for j in range(l):
      M[x-1+j][y-1]=1


for i in range(h):
  for j in range(w):
    print(M[i][j], end=' ')
  print()



  