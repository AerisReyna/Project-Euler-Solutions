a = 1
b = 1
c = 998
found = False
while not found:
    if a ** 2 + b ** 2 == c ** 2:
        found = True
        break
    c -= 1
    b += 1
    if b >= c:
        a += 1
        c = 1000 - a - 1
        b = 1
print(a * b * c)
print(a, b, c)