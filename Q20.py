ideal = {
    "Sugar level": 15,
    "Blood pressure": 32,
    "Heartbeat rate": 71,
    "weight": 65,
    "fat percentage": 10
}

actual = {}
diffs = {}

for key in ideal:
    val = int(input(f"{key}: "))
    actual[key]=val
    diffs[key]= val-ideal[key]

print("\nDifferences:")
print(diffs)
for key in diffs:
    diff = diffs[key]
    if diff ==0:
        continue
    elif diff > 0:
        print(f"{key} is {diff} more than the ideal value")
    else:
        print(f"{key} is {-diff} less than the ideal value")
