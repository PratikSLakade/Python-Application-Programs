#Demonstation of Lambda Function 

Cube = lambda A : A**3

def main():
    No = int(input("Enter the number :"))
    Ret = Cube(No)
    print("Cube of number is :",Ret)


if __name__ == "__main__":
    main()