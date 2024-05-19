
def CheckEvenOdd(A):
    if(A%2==0):
        return True
    else:
        return False
    
#CheckEvenOddX = lambda A,B : A+B

def main():
    iNo = int(input("Enter a number :"))
    Ret = CheckEvenOdd(iNo)
    if(iNo==True):
        print("Number is Even")
    else:
        print("Number is odd")

if __name__ == "__main__":
    main()