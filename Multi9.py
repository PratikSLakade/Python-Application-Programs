import threading

def EvenDisplay(No):
    
    print("List of Even Numbers")
    x = 2 
    for i in range(No):
        print("Even",x)
        x = x + 2

def OddDisplay(No):
    
    print("List of odd Numbers : ")
    x = 1
    for i in range(No):
        print("Odd",x)
        x = x + 2

def main():
    
    print("Enter a number : ")
    Value = int(input())

    t1 = threading.Thread(target = EvenDisplay,args = (Value,))
    t2 = threading.Thread(target = EvenDisplay,args = (Value,))
    
    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("End of main Process .")
    

if __name__ == "_main__":
    main()