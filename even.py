#programme based on conditional statement
def CheckEven(No):
    if(No % 2 == 0):
        print("It is even number : ")
    else :
        print("It is odd number: ")
    
def main():
    print("Enter even number")
    A = int(input())

    CheckEven(A)