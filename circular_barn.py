cows_perl = []
cows = 0
reset = 0
count = 0
totals = []
with open("cbarn.in") as f:
    for line in f:
        cows_perl.append(int(line))
cows_perl.remove(cows_perl[0])
for i in cows_perl:
    cows+=i
    reset +=i
for i in range(len(cows_perl)):
    cows = reset
    cows-=cows_perl[i]
    count +=cows
final = float('inf')
for i in totals:
    if final>i:
        final = i

with open("cbarn.out","w") as f:
    f.write(final)

# Review