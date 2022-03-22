def is_prime(num: int) -> bool:
    if num <= 3:
        return num > 1
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i ** 2 <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

sum = 0
for i in range(2000000):
    if is_prime(i):
        sum += i

print(sum)