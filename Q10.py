
import math

x = 0
y = 0

while True:
    move = input()
    if not move:
        break
    direction, steps = move.split()
    steps = int(steps)

    if direction =='UP':
        y += steps
    elif direction =='DOWN':
        y -= steps
    elif direction =='LEFT':
        x -= steps
    elif direction =='RIGHT':
        x += steps

distance = round(math.sqrt(x**2 + y**2))
print(distance)
