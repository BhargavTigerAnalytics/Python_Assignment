currency = [1,2,5,10,20,50,100,200,500,2000]
amount = int(input("Enter amount:"))
currency.sort(reverse=True)

for c in currency:
    if amount >= c:
        num = amount // c
        print(f"{c}-{num}")
        amount %= c
