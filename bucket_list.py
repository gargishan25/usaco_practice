n = input()
start_time = []
end_time = []
buckets = []
for _ in range(n):
    a,b,c = map(int,input().split())
    start_time.append(a)
    end_time.append(b)
    buckets.append(c)

for i in n:
    if 