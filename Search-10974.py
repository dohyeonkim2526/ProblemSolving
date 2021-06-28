import itertools
n=int(input())
arr=[i for i in range(1,n+1)]

for nums in list(itertools.permutations(arr)):
    for n in nums:
        print(n,end=' ')
    print()