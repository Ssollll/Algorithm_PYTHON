import sys
import math

A, B = map(int, sys.stdin.readline().split())
C, D = map(int, sys.stdin.readline().split())

lcm = math.lcm(B, D)

an_s = A * (lcm // B) + C * (lcm // D)

gcd = math.gcd(an_s, lcm)

print(an_s // gcd, lcm // gcd, sep = " ")