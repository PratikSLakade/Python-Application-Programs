import threading
import os

def EvenDisplay(No):
    print("PID of even process ",os.getpid())
    print("TID of even thread ",threading.get_ident())
    print("List of Even Numbers")
    x = 2 
    for i in range(No):
        print(x)
        x = x + 2

def OddDisplay(No):
    print("PID of odd process ",os.getpid())
    print("TID of odd thread ",threading.get_ident())
    print("List of odd Numbers : ")
    x = 1
    for i in range(No):
        print(x)
        x = x + 2

def main():
    print("PID of main process ",os.getpid())
    print("TID of main thread ",threading.get_ident())
    print("Enter a number : ")
    Value = int(input())

    p1 = threading.Thread(target = EvenDisplay,args = (Value,))
    p2 = threading.Thread(target = EvenDisplay,args = (Value,))
    
    p1.start()
    p1.join()
    
    p2.start()
    p2.join()

    print("End of main Process .")
    

if __name__ == "_main__":
    main()