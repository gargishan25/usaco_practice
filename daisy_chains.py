n = int(input())
flowers = list(map(int,input().split()))
count = 0
def z(a,b,l):
    const = a
    s = 0
    while const<=b:
        s += l[const]
        const+=1
    div = b-a+1
    const = a
    while const<=b:
        if (s/div) == l[const]:
            return 1
        const+=1
    return 0
for i in range(len(flowers)):
        for j in range(i,len(flowers)):
            count += z(i,j,flowers)
print(count)
















# n=int(input())
# arr=list(map(int,input().split()))
# count=0
# for i in range(n):
#     for j in range(i,n):
#         total=0
#         for k in range(i,j+1):
#             total+=arr[k]
#         avg=total/(j-i+1)
#         for k in range(i,j+1):
#             if arr[k]==avg:
#                 count+=1
#                 break
# print(count)