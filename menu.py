"""
MENU PROGRAM
------------
A program that would display a menu as shown below

----- MAIN MENU -----
1. ADD
2. SUBTRACT
3. MULTIPLY
4. DIVIDE
0. QUIT/END
---------------------
Enter Option(0..4):

provide function to facilitate each option
"""
from os import system
import functools

a:int = 0
b:int = 0

def mathinput(message)->None:
    def topmessage(func):
        @functools.wraps(func)
        def wrapper():
            global a,b
            system("cls")
            print(message)
            a=int(input("Enter 1st value:"))
            b=int(input("Enter 2nd value:"))
            func()
        return wrapper
    return topmessage
    
@mathinput(message="ADDITION")
def add()->None:
    print(f"the sum of {a} and {b} is {a+b}")

@mathinput(message="SUBTRACT")  
def subtract()->None:
    #print("SUBTRACT")
    print(f"the difference of {a} and {b} is {a-b}")

@mathinput(message="MULTIPLY")
def multiply()->None:
    #print("MULTIPLY")
    print(f"the product of {a} and {b} is {a*b}")

@mathinput(message="DIVIDE")   
def divide()->None:
    #print("DIVIDE")
    print(f"the quotient of {a} and {b} is {a/b:.4f}")
    

def menu()->None:
    system("cls")
    print(" MAIN MENU ".center(21,"-"))
    print("1. ADD")
    print("2. SUBTRACT")
    print("3. MULTIPLY")
    print("4. DIVIDE")
    print("0. QUIT/END")
    print("-"*21)

def main()->None:
    option:int = 9999
    while option != 0:
        menu()
        try:
            option=int(input("Enter Option(0..4):"))
            if   option == 1:add()
            elif option == 2:subtract()
            elif option == 3:multiply()
            elif option == 4:divide()
            elif option == 0:print("Program ended...")
                
        except Exception as e:
            print(f"Invalid Input:{e}")
        print()#print one vacant line
        input("Press any key to continue...")
        
if __name__=="__main__":
    main()

