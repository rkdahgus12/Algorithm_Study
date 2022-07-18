'''
3
1 3
2 4
3 5
'''
import sys
import heapq

heap=[]
input = sys.stdin.readline
soo = int(input())
for i in range(soo):
    start, end = map(int, input().split())
    heap.append([start, end])
heap.sort()
class_room=[]
heapq.heappush(class_room, heap[0][1])
for i in range(1, soo):
    if heap[i][0] < class_room[0]:
        heapq.heappush(class_room, heap[i][1])
    else:
        heapq.heappop(class_room)
        heapq.heappush(class_room, heap[i][1])

print(len(class_room))

