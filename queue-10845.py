#큐 자료구조에서 리스트는 연산이 느려지기 때문에 비추천!
#Deque 자료구조 사용하기
from collections import deque
import sys
n=int(input())
queue=deque()

def push(x):
    queue.append(x)

def pop():
    return queue.popleft() if queue else -1

def size():
    return len(queue)

def empty():
    return 0 if queue else 1

def front():
    return queue[0] if queue else -1

def back():
    return queue[-1] if queue else -1
    
        
for _ in range(n):
    cmd=sys.stdin.readline().split()

    if cmd[0]=='push':
        push(cmd[1])

    if cmd[0]=='pop':
        print(pop())

    if cmd[0]=='size':
        print(size())

    if cmd[0]=='empty':
        print(empty())

    if cmd[0]=='front':
        print(front())

    if cmd[0]=='back':
        print(back())

