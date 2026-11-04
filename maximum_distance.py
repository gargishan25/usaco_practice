n = int(input())
l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))

print(l1,l2)
store = []
final = 0
for i in range(len(l1)):
    for j in range(len(l1)):
        store.append(((l1[i]-l1[j])**2)+((l2[i]-l2[j])**2))
for i in store:
    if final<i:
        final = i
print(store)
print(final)