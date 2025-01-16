def ADDodd(n):
    s = 0
    for i in range(1,n+1):
        if i%2!=0:
            s = s +i
    return s    
n = int(input("Enter the no.: "))
result = ADDodd(n)
print("Sum of the odd number: ",result)