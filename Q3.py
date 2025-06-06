words = input("Enter the words:").split()

uniqueSorted = sorted(set(words))

print(" ".join(uniqueSorted))
