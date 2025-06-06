
binary = input("Enter a binary number: ")

count = 0

ones = [i for i, bit in enumerate(binary) if bit == '1']

for i in range(len(ones)):
    for j in range(i+1, len(ones)):
        count += 1

print(count)
