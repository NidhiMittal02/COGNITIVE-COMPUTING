import random

random_number = [random.randint(100,900) for i in range(100)]
def is_prime(n):
    if n<2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
        return True

odd_num = [num for num in random_number if num%2!=0]
print(odd_num)
print(len(odd_num))
even_num = [num for num in random_number if num%2==0]
print(even_num)
print(len(even_num))
prime_num = [num for num in random_number if is_prime(num)]
print(prime_num)
print(len(prime_num))