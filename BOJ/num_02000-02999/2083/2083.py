import sys
input = sys.stdin.readline

while True :
    people = list(map(str, input().strip().split()))
    if people[0] == "#" :
        break
    if int(people[1]) > 17 or int(people[2]) >= 80 :
        print(people[0] + " " + "Senior")
    else :
        print(people[0] + " " + "Junior")
    
                  