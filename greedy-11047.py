#11047번 동전 0
#N: 동전의 종류, K: 동전의 합
#시간초과
n,k=map(int, input().split())
ans=0
money=k
vals=[]
for i in range(n):
    vals.append(int(input()))

for i in range(n-1,-1,-1):
    if money==0:
        break
    if vals[i]<money:
        ans+=money//vals[i]
        money-=(money//vals[i])*vals[i]

print(ans)

#정답1
n,k=map(int, input().split())
ans=0
vals=[]
for i in range(n):
    vals.append(int(input()))

vals.sort(reverse=True)

for i in vals:
    if k==0:
        break
    ans+=k//i
    k%=i

print(ans)

#정답2
n,k=map(int, input().split())
ans=0
vals=[]
for i in range(n):
    vals.append(int(input()))

while k>0:
    v=vals.pop()  
    ans+=k//v
    k%=v

print(ans)