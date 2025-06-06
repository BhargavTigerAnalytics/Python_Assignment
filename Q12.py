s = input("Enter alphanumeric string: ")
n = len(s)

for i in range(n):

    if s[i].isalpha():
        for j in range(i + 1, n):
            
            if s[j].isalpha():
                sub = s[i+1:j]
                digits = ''.join([ch if ch.isdigit() else ' ' for ch in sub]).split()
                total = sum(int(x) for x in digits)
                if total == 9:
                    print(s[i] + "," + s[j])
                break
