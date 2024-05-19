print("Demonstration of Functional")

Addition = lambda No1,No2 : No1+No2

Substraction = lambda No1,No2 : No1-No2


print("Enter First number : ")
A = int(input())

print("Enter Second Number : ")
B = int(input())

Ret = Addition(A,B)
print("Addition of two numbers is :",Ret)

Ret = Substraction(A,B)
print("Substraction of two numbers is :",Ret)\
    
