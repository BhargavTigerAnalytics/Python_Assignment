rows = int(input())
pattern = [
    "  ***  ",
    " *     ",
    " *     ",
    " * *** ",
    " *   * ",
    " *   * ",
    "  ***  "
]

for i in range(rows):
    if i < len(pattern):
        print(pattern[i])
