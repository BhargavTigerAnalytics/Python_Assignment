result = []

for number in range(1000, 3001):
    digits =str(number)
    all_even =True
    for d in digits:
        if int(d) % 2 != 0:
            all_even = False
            break
    if all_even:
        result.append(digits)

print(",".join(result))
