# SAMPLE INPUT:
# 5
# 1 3 4 5 2
# 1234567 2222222 3333333 4444444 5555555
# SAMPLE OUTPUT:
# 1234567
# 5555555
# 2222222
# 3333333
# 4444444
n = int(input())
position = []
id = []
position = list(map(int,input().split()))
id_number = list(map(int,input().split()))

for i in range(n):
    if position[i-1] != i:
    