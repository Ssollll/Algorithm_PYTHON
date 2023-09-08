import sys
input = sys.stdin.readline

L, C = map(int, input().split())
alpha = list(map(str, input().strip().split()))
alpha.sort()

vowel = ["a", "e", "i", "o", "u"]

def check(arr) :
    v_cnt, c_cnt = 0, 0

    for i in arr :
        if i in vowel :
            v_cnt += 1
        else :
            c_cnt += 1
    
    if v_cnt >= 1 and c_cnt >= 2 :
        return True
    else :
        return False

def back_tracking(arr) :
    if len(arr) == L :
        if check(arr) :
            print("".join(arr))
            return
    
    for i in range(len(arr), C) :
        if arr[-1] < alpha[i] :
            arr.append(alpha[i])
            back_tracking(arr)
            arr.pop()

for i in range(C - L + 1) :
    a = [alpha[i]]
    back_tracking(a)
    