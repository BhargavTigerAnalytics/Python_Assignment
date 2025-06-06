n = int(input())
for i in range(n):
    row = []
    for j in range(n):
        if i == 0 or i == n-1 or j == n//2:
            row.append('1')
        else:
            row.append('0')
    print(" ".join(row))
