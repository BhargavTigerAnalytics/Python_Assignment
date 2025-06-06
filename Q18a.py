rows = int(input())
num = 1
for i in range(1, rows + 1):
    line = []
    for j in range(i):
        line.append(str(num))
        num += 1
    print(" * ".join(line))
