text = input("Enter a string:").lower()
result = ""
count = 1

for i in range(1, len(text)):
    if text[i] == text[i - 1]:
        count += 1
    else:
        result += text[i - 1] + str(count)
        count = 1

if text:
    result += text[-1] + str(count)

print(result)
