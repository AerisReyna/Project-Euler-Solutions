first = 1
second = 1
temp = 1
sum = 0
while (second < 4000000):
    temp = second
    second = second + first
    if second % 2 == 0:
        sum += second
    first = temp

print(sum)
