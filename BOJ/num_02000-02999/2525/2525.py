import sys

H, M = map(int, sys.stdin.readline().split())
C = int(sys.stdin.readline())

if C >= 60 :
    H += (C // 60)
    C -= (C // 60) * 60

M += C

if M >= 60 :
    H += (M // 60)
    M -= (M // 60) * 60

if H >= 24 :
    H -= 24

print(str(H) + " " + str(M))
