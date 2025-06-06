rows = int(input())
num = 1
data = []

for i in range(1, rows + 1):
    row = []
    for j in range(i):
        row.append(str(num))
        num += 1
    data.append(row)

for row in data:
    print(" * ".join(row))
for row in reversed(data[:-1]):
    print(" * ".join(row))
