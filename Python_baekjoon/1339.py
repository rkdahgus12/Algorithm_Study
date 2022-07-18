import sys
from collections import deque

input = sys.stdin.readline

a1, a2 = map(int, input().split())
count = 0


def bfs():
    q = deque()
    q.append(a1)
    while q:
        x = q.popleft()
        if x == a2:
            print(count)
            break
        for i in range(100):
            q.append()

'''
from collections import deque

a, b = map(int, input().split())
res = -1
que = deque([(a, 1)])
while que:
    i, cnt = que.popleft()
    if i == b:
        res = cnt
        break
        
    if i*2 <= b:
        que.append((i*2, cnt+1))
    if int(str(i)+'1') <= b:
        que.append((int(str(i)+'1'), cnt+1))

print(res)
'''