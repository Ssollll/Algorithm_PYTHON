import sys

N = int(sys.stdin.readline()) # int는 split 해줄필요 없움

bee = 1 # 벌집 개수 : 1개 시작
cnt = 1 # 증가

while(N > bee) :
    bee += 6*cnt
    cnt += 1

print(cnt)
