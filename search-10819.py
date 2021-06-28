#생각(x): 최대값-최소값 순서를 반복해보자
#생각: itertools 사용해보자

# n=int(input())
# nums=list(map(int, input().split()))

# max=sorted(nums, reverse=True)
# min=sorted(nums)

# sum=0
# for i in range(n//2):
#     sum+=max[i]-min[i]

# print(sum)

from itertools import permutations
n=int(input())
arr=list(map(int, input().split()))
ans=[]

for nums in list(permutations(arr)):
    sum=0
    for i in range(0,n-1):
        sum+=abs(nums[i]-nums[i+1])
    ans.append(sum)
    
print(max(ans))

#sys 사용법
import sys
from itertools import permutations
n=int(sys.stdin.readline())
arr=list(map(int, sys.stdin.readline().split()))
ans=[]

for nums in list(permutations(arr)):
    sum=0
    for i in range(0,n-1):
        sum+=abs(nums[i]-nums[i+1])
    ans.append(sum)
    
print(max(ans))

