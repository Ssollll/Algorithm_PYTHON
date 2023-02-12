import sys

t = 0
for _ in range(4) :
    i = int(sys.stdin.readline())
    t += i

print(t // 60)
print(t % 60)