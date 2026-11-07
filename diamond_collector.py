# count = 0
# diamonds = []
# for line in "diamond.in":
#     if count == 0:
#         n,k = line.split()
#     else:
#         diamonds.append(line)
#     count+=1
# print(diamonds)
import sys
sys.stdin = open("diamond.in",'r')
sys.stdout = open("diamond.out", 'w')

diamonds = []
maximum = 0
n,k = map(int,input().split())
for _ in range(n):
    diamonds.append(int(input()))
diamonds.sort()
for i in range(len(diamonds)):
    for a in range(len(diamonds)):
        if diamonds[a]<=diamonds[i]+k:
            if (a-i+1)>maximum:
                maximum = a-i+1
print(maximum)