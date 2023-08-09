import sys
input = sys.stdin.readline

T = int(input())

def bs(t, d) :
    start = 0
    end = len(d) - 1
    res = -1
    while start <= end :
        mid = (start + end) // 2
        if d[mid] < t :
            res = mid
            start = mid + 1
        else :
            end = mid - 1
    return res

for _ in range(T) :
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    
    answer = 0

    for i in A :
        answer += bs(i, B) + 1
    
    print(answer)