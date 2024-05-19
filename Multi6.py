# import os  (for pid and ppid)
import multiprocessing
import os

def EvenDisplay(No):
    print("PID of even process ",os.getpid())
    print("List of Even Numbers")
    x = 2 
    for i in range(1,No):
        print(x)
        x = x+2

def OddDisplay(No):
    print("PID of odd process ",os.getpid())
    print("List of odd Numbers : ")
    x = 1
    for i in range(1,No):
        print(x)
        x = x + 2

def main():
    print("PID of main process ",os.getpid())
    print("Enter a number : ")
    Value = int(input())

    p1 = multiprocessing.Process(target = EvenDisplay,args = (Value,))
    p2 = multiprocessing.Process(target = EvenDisplay,args = (Value,))
    
    p1.start()
    p1.join()
    
    p2.start()
    p2.join()

    print("End of main Process .")
    

if __name__ == "_main__":
    main()