num = int(input("Enter a number: "))
binary = ""

if num == 0:
    binary = "0"
else:
    while num > 0:
        binary = str(num % 2) + binary
        num = num // 2

print(binary)
