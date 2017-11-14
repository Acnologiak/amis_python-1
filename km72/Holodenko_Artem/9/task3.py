def power(a, n):
    a1 = a
    for i in range(n-1):
        a = a*a1
    return a
a = float(input("Enter a "))
n = int(input("Enter n "))
print(power(a, n))
