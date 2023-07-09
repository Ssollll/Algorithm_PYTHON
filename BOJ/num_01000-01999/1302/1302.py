import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
book = [input().strip() for _ in range(N)]
book.sort()

c = Counter(book).most_common()
print(c[0][0])