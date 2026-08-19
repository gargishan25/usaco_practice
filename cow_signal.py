m,n,k = map(int,input().split())
output = []
for _ in range(m):
    final = ""
    inp = input()
    for character in inp:
        final += character * k
    for _ in range(k):
        output.append(final)
for i in output:
    print(i)