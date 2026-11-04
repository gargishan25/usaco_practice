# import sys
# sys.stdin = open("pails.in",'r')
# sys.stdout = open("pails.out", 'w')

# with open("pails.in") as f:
#     for line in f:
#         segment = line.split()
#         x = int(segment[0])
#         y = int(segment[1])
#         m = int(segment[2])

# x,y,m = map(int,input().split())

# max = m//x
# count = m//x
# highest = 0
# while count >= 0:
#     if count*x + (max-count)*y <= m and count*x + (max-count)*y > highest:
#         highest = count*x + (max-count)*y
#     count-=1
# print(highest)

# Answer:
import sys
sys.stdin = open("pails.in",'r')
sys.stdout = open("pails.out", 'w')

x,y,m = map(int,input().split())

# max = m//x
count = m//x
highest = 0
while count >= 0:
    remaining = m - (count*x)
    num = remaining//y
    current = (count*x) + (num*y)
    if current > highest:
        highest = current
    count-=1
print(highest)