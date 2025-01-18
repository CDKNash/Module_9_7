import math

def is_prime(func):
    def wrapper(*args, **kwargs):
        n = func(*args, **kwargs)

        if n == 2 or n % 2 != 0:
            print("Простое")
        else:
             print("Составное")
        return n
    return wrapper


@is_prime
def sum_three(a, b, c):
    sum_ = a + b + c
    return sum_

result = sum_three(2, 3, 6)
print(result)
