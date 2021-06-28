#정답1
import sys
from itertools import permutations
arr=[]

while True:
    a=list(map(int, sys.stdin.readline().split()))
    arr.append(a)
    if a[0]==0: break

for a in arr:
    for nums in list(permutations(a)):
        for n in nums:
            print(n, end=' ')
        print()
    if a==0: break

for a in arr:
    if a[0]==0:
        break

    else:
        a.pop(0)
        for nums in list(permutations(a)):
            print(map(''.join,nums))
        print()
        

#정답2
from itertools import combinations

while True:
    k,*s=list(map(int, input().split()))
    if k==0:
        break
    else:
        for nums in combinations(s,6):
            print(' '.join(map(str, nums)))
        print()
