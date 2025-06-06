input_str = input("Enter two numbers separated by comma: ")
x, y = input_str.split(",")
x = int(x)
y = int(y)

result = [[i*j for j in range(y)] for i in range(x)]
print(result)
