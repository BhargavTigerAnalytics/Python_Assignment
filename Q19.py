mode = int(input())
s = input().strip("'\"")
rot = int(input())

for _ in range(rot):
    if mode == 1:
        s = s[1:] + s[0]
    elif mode == 2:
        s = s[-1] + s[:-1]
    print(s)
