#2875번 대회or인턴 (최대개수)
#n:여자, m:남자, k:인턴십
#1.n-2, m-1 => 멈춤 조건: 둘중에 하나가 0이거나 (n'+m')<k

n,m,k=map(int, input().split())
ans=0

#  for i in range(max(n,m,k)):
#     n-=2
#     m-=1
#     if n==0 or m==0:
#         if (n+m)>k:
#             ans+=1
#             break
#         else:
#             break

#     else:
#         ans+=1

while n>=2 and m>=1 and (n+m-k)>=3:
    n-=2
    m-=1
    ans+=1

print(ans-1)


#다른 풀이
n,m,k=map(int, input().split())
ans=0

while True:
    n-=2
    m-=1
    if n<0 or m<0 or (n+m)<k:
        break
    else:
        ans+=1

print(ans)


#다른 풀이-2
n,m,k=map(int, input().split())
for i in range(k):
    if n//2>=m:
        n-=1
    else:
        m-=1

print(min(n//2,m))


