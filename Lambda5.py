    
CheckEvenOddX = lambda A : (A%2==0)

def main():
    iNo = int(input("Enter a number :"))
    Ret = CheckEvenOddX(iNo)
    if(iNo==True):
        print("Number is Even")
    else:
        print("Number is odd")

if __name__ == "__main__":
    main()