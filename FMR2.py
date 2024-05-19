#Demonstartion of Filter Map Reduce using lambda fun
from functools import reduce

CheckEven = lambda No : (No%2==0)

Increase = lambda No : (No+1)

Add = lambda A,B : (A+B)

def main():
    Data = [11,14,20,23,18,16,15,20]

    print("Data from input list :",Data)

    FData = list(filter(CheckEven,Data))
    print("Data after Filter Activity : ",FData)

    MData = list(map(Increase,FData))
    print("Data After Map Activity : ",MData)

    # 15,21,19,17,21
    # 0 + 15   15
    # 15 + 21   36
    # Like wise



    RData = reduce(Add,MData)
    print("Data after reduce activity :",RData)

if __name__ == "__main__":
    main()