shells = []
score_store = []
score = 0
n=int(input())
for i in range(1,n+1):
    shells.append(i)
for z in range(1,n+1):
    a,b,c = map(int,input().split())
    score_store.append(score)
    score = 0
    for i in range(n):
        switch = shells[a-1]
        shells[a-1] = shells[b-1]
        shells[b-1] = switch
        if shells[c-1] == z:
            score +=1
        print(shells)
        print(score)
highest = 0
for i in score_store:
    if i>highest:
        highest = i
print(highest)