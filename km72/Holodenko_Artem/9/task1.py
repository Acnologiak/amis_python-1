def distance(x1, y1, x2, y2):
    d = ((x1-x2)**2+(y1-y2))**0.5
    return d
x1 = float(input("Enter x1 "))
y1 = float(input("Enter Y1 "))
x2 = float(input("Enter x2 "))
y2 = float(input("Enter Y2 "))
print(distance(x1, y1, x2, y2))
