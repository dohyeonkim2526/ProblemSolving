#10610번 30
#시간초과
import itertools
n=list(str(int(input())))
nums=list(map(int, map(''.join, itertools.permutations(n))))
nums.sort(reverse=True) #가장 큰 수를 찾아야 하므로 내림차순 정렬을 해준다.

for i in range(len(nums)):
    if nums[i]%30==0:
        print(nums[i])
        break
    if i==len(nums)-1:
        print(-1)

#30의 배수 조건: 1의 자리에 들어갈 0을 포함 + 모든 수의 합이 3으로 나눠져야 한다.
n=list(input())
n.sort(reverse=True)

if '0' not in n:
    print(-1)

else:
    if sum(map(int,n))%3==0:
        for i in range(len(n)):
            print(n[i],end='')

    else:
        print(-1)   

#방법2
n=list(input())
n.sort(reverse=True)
if '0' not in n or sum(map(int,n))%3!=0:
    print(-1)
else:
    print(''.join(n)) 