import sys

input = sys.stdin.readline

soo = int(input())
max_heap = [0, 1]


def swap(res, x, y):
    res[x], res[y] = res[y], res[x]


for i in range(2, soo + 1):
    max_heap.append(i)
    swap(max_heap, i, i - 1)
    j = i - 1
    while j != 1:
        swap(max_heap, j, j // 2)
        j = j // 2

for i in max_heap[1:]:
    print(i, end=' ')
