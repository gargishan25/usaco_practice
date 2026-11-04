# INPUT
# 4
# on 1 1
# none 10 14
# none 11 15
# off 2 3

# OUTPUT
# 10 13
# 8 12
second_argument = []
with open("traffic.in") as f:
    for line in f:
        if len(line.split()) == 1:
            n = int(line)
        if len(line.split()) != 1:
            segment = line.split()
            segment[1] = int(segment[1])
            segment[2] = int(segment[2])
            second_argument.append(segment)


def function(n, segments):
    # segments is ["on",1,1]
    start = [0,float('inf')]
    for i in range(len(segments)):
        if segments[i][0] == "none":
            new_min = max(start[0], segments[i][1])
            new_max = min(start[1], segments[i][2])
            start[0] = new_min
            start[1] = new_max
        if segments[i][0] == "off":
            start[0] = start[0] - segments[i][2]
            if start[0] - segments[i][2] < 0:
                start[0] = 0
            start[1] = start[1] - segments[i][1]
            if start[1] - segments[i][1] < 0:
                start[1] = 0
        if segments[i][0] == "on":
            start[0] = start[0] + segments[i][1]
            start[1] = start[1] + segments[i][2]
    end = [start[0],start[1]]
    for i in range(len(segments)-1,-1,-1):
        if segments[i][0] == "none":
            new_min = max(start[0], segments[i][1])
            new_max = min(start[1], segments[i][2])
            start[0] = new_min
            start[1] = new_max
        if segments[i][0] == "on":
            start[0] = start[0] - segments[i][2]
            if start[0] < 0:
                start[0] = 0
            start[1] = start[1] - segments[i][1]
            if start[1] < 0:
                start[1] = 0
        if segments[i][0] == "off":
            start[0] = start[0] + segments[i][1]
            start[1] = start[1] + segments[i][2]
    return start, end

start, end = (function(4,second_argument))
with open("traffic.out","w") as f:
    f.write(f"{start[0]} {start[1]}\n{end[0]} {end[1]}")