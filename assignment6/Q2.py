def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n** 0.5) + 1):  
        if n % i == 0:
            return False
    return True

def sum_of_primes(n):
    s = 0
    for i in range(1, n + 1):
        if is_prime(i):  
            s += i
    return s

n = int(input("Enter the value of n: "))

result = sum_of_primes(n)
print("sum of prime no.: ",result)
