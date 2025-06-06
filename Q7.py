total = 0

while True:
    try:
        entry = input()
        if not entry:
            break
        action, amount = entry.split()
        amount = int(amount)
        if action == 'D':
            total += amount
        elif action == 'W':
            total -= amount
    except:
        break

print(total)
