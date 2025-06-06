
sentence = input("Enter a sentence:")
letters = []
digits = []

for char in sentence:
    if char.isalpha():
        letters.append(char)
    elif char.isdigit():
        digits.append(char)

print("LETTERS", len(letters))
print("DIGITS", len(digits))
