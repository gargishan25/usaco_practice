#SAMPLE INPUT:
# 10 3
# 11 4
# 12 5

# SAMPLE OUTPUT:
# 0
# 10

bucket1 = []
bucket2 = []
bucket3 = []
a,b = map(int,input().split())
bucket1.append(a)
bucket1.append(b)
c,d = map(int,input().split())
bucket2.append(c)
bucket2.append(d)
e,f = map(int,input().split())
bucket3.append(e)
bucket3.append(f)
for i in range(1,101):
    if i%3 == 0:
        if bucket1[0] - bucket1[1] != 0:
            if bucket1[0] - bucket1[1] >= bucket3[1]:
                bucket1[1] = bucket1[1] + bucket3[1]
                bucket3[1] = 0
            if bucket1[0] - bucket1[1] < bucket3[1]:
                bucket3[1] = bucket3[1] - bucket1[0] + bucket1[1]
                bucket1[1] = bucket1[0]
    elif i%2==0:
        if bucket3[0] - bucket3[1] != 0:
            if bucket3[0] - bucket3[1] >= bucket2[1]:
                bucket3[1] = bucket3[1] + bucket2[i]
                bucket2[1] = 0
            if bucket3[0] - bucket3[1] < bucket2[1]:
                bucket2[1] = bucket2[1] - bucket3[0] + bucket3[1]
                bucket3[1] = bucket3[0]
    else:
        if bucket2[0] - bucket2[1] != 0:
            if bucket2[0] - bucket2[1] >= bucket1[1]:
                bucket2[1] = bucket2[1] + bucket1[i]
                bucket1[1] = 0
            if bucket2[0] - bucket2[1] < bucket1[1]:
                bucket1[1] = bucket1[1] - bucket2[0] + bucket2[1]
                bucket2[1] = bucket2[0]