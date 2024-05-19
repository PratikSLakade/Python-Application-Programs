
from functools import reduce

CheckEven = lambda No : (No%2==0)

Increase = lambda No : (No+1)

Add = lambda A,B : (A+B)

#Task : name of funtion
# Elements : list of data elements
def filterX(Task,elements):
    Result = []
    for no in elements :
        if(Task(no)==True):
            Result.append(no)
    return Result



def main():
    Data = [11,14,20,23,18,16,15,20]

    print("Data from input list :",Data)

    FData = list(filterX(CheckEven,Data))
    print("Data after Filter Activity : ",FData)

    MData = list(map(Increase,FData))
    print("Data After Map Activity : ",MData)

    


    RData = reduce(Add,MData)
    print("Data after reduce activity :",RData)

if __name__ == "__main__":
    main()