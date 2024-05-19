import os
import multiprocessing 


def Task1(No):
    print("Executing first task")
    print("Print PID of task 1",os.getpid())
    print("Print PPID of task 1",os.getpid())

def Task2(No):
    print("Executing second task")
    print("Print PID of task 2",os.getpid())
    print("Print PPID of task 2",os.getpid())
    
def main():
    print("PID of running process : ",os.getpid())
    print("PID of parent process ie command prompt is : ",os.getppid())


    Value = 11
    p1 = multiprocessing.Process(target = Task1, args =(Value,))
    p2 = multiprocessing.Process(target = Task2, args =(Value,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

if __name__ == "__main__":
    main()