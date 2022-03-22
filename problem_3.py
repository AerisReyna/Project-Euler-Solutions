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

num = 600851475143
larger_fac = num
i = 5
while i*i < larger_fac:
    if num % i == 0 and is_prime(i):
        larger_fac = num // i
        print(i)
        
    i += 1