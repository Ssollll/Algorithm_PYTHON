import sys, heapq
input = sys.stdin.readline

N = int(input())

heap = []

for i in range(N) :
    num = int(input())
    if num :
        heapq.heappush(heap, (abs(num), num))
    else :
        if heap :
            print(heapq.heappop(heap)[1])
        else :
            print(0)