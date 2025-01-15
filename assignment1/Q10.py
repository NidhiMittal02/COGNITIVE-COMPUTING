n = int(input("Enter the value of n: "))
s = 0

for num in range(2, n + 1): 
    is_prime = True
    for i in range(2, int(num // 2) + 1): 
        if num % i == 0:
            is_prime = False
            break
    if is_prime: 
        s += num

print(f"The sum of all prime numbers from 1 to {n} is: {s}")
