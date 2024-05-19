import multiprocessing
import os

def Cube(No):
    print("PID is : ",os.getpid())
    return No**3

def main():
    Arr = [10,20,30,40]
    Result = []

    p = multiprocessing.pool()
    Result = p.map(Cube,Arr)
    p.close()
    p.join()
    
    print(Result)

if __name__ == "__main__":
    main()