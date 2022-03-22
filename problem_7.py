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

number = 1
i = 1
while number < 10001:
    if (is_prime(i)):
        number += 1
    i += 1
print(i - 1)    