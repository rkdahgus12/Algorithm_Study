import sys

input = sys.stdin.readline
soo = int(input())
res = list(map(int, input().split()))
def bubble_sort(arr):
    count=1
    end = len(arr) - 1
    while end > 0:
        last_swap = 0
        for i in range(end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                last_swap = i
        count+=1
        end = last_swap
    print(count)
bubble_sort(res)