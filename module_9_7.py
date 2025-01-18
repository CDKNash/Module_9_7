import math

def is_prime(func):
    def wrapper(*args, **kwargs):
        n = func(*args, **kwargs)
        if n < 2:
            return "Составное"
        for i in range(2, int(n ** 0.5 + 1)):
            if n % i == 0:
                return "Составное"
        else:
            return "Простое"
    return wrapper


@is_prime
def sum_three(a, b, c):
    sum_ = a + b + c
    return sum_

result = sum_three(2, 3, 6)
print(result)
