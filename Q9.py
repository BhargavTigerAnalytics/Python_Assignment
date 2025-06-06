
data = []

while True:
    entry = input()
    if not entry:
        break
    parts = entry.split(",")
    data.append((parts[0], int(parts[1]), int(parts[2])))

data.sort()
print(data)
