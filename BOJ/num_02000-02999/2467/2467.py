import sys

N = int(sys.stdin.readline())
liquid = list(map(int, sys.stdin.readline().split()))

left, right = 0, N-1
value = sys.maxsize
answer = []

while left < right :
    if abs(liquid[left] + liquid[right]) <= value :
        answer = [liquid[left], liquid[right]]
        value = abs(sum(answer))
    
    if liquid[left] + liquid[right] < 0 :
        left += 1
    elif liquid[left] + liquid[right] > 0 :
        right -= 1
    else :
        break

print(*answer)