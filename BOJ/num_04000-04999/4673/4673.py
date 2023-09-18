import sys
input = sys.stdin.readline

def self_number(x) :
    self_num = x
    while x != 0 :
        self_num += (x % 10)
        x //= 10
    return self_num

result = []

for i in list(range(1, 10001)) :
    result.append(self_number(i))
    if i not in result :
        print(i)