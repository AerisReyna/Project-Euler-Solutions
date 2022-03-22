smallest_num = 20
found = False
while not found:
    for i in range(7, 21, 1):
        if smallest_num % i != 0:
            break
        if i == 20:
            print(smallest_num)
            found = True
    smallest_num += 20