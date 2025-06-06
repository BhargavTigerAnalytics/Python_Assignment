import math

def nCr(n, r):
    return math.comb(n, r)

n = int(input("Enter number of total stops (n): "))
m = int(input("Enter number of stops to choose (m): "))

ways = nCr(n - m + 1, m)
print("Output:", ways)
