from numpy import true_divide


def is_palindrome(a, b):
    product = str(a * b)
    if product == product[::-1]:
        return True
    else:
        return False

largest = 0
for num1 in range(99, 1000, 1):
    for num2 in range(99, 1000, 1):
        if is_palindrome(num1, num2):
            if num1 * num2 > largest:
                largest = num1 * num2
print(largest)