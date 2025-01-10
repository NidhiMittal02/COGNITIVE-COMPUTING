a = int(input("Enter the no: "))
s= 0
for i in range(1,a+1):
    if i%7==0 and i%9==0:
        s = s +i
print("sum : ",s)
