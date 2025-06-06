sentence = input("Enter a sentence:")
upper = 0
lower = 0

for char in sentence:
    if char.isupper():
        upper += 1
    elif char.islower():
        lower += 1

print("UPPER CASE", upper)
print("LOWER CASE", lower)
