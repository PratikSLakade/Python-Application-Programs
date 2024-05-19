#Demonstartion using lambda inserted in side
from functools import reduce

def main():
    Data = [11,14,20,23,18,16,15,20]

    print("Data from input list :",Data)

    FData = list(filter(lambda No : (No%2==0),Data))
    print("Data after Filter Activity : ",FData)

    MData = list(map(lambda No : (No+1),FData))
    print("Data After Map Activity : ",MData)

    # 15,21,19,17,21
    # 0 + 15   15
    # 15 + 21   36
    # Like wise



    RData = reduce(lambda A,B : (A+B),MData)
    print("Data after reduce activity :",RData)

if __name__ == "__main__":
    main()