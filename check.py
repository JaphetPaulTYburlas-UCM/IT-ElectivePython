"""
a program that would accept an integer
check and display whether the value is
zero,odd or even
"""
from os import system
def main()->None:
    system("cls")
    try:
        a:int = int(input("Enter value:"))
        if a==0:
            print("ZERO")
        elif (a%2)==0:
            print("EVEN")
        else:
            print("ODD")
        
    except Exception as e:
        print(f"invalid input:{e}")
    
if __name__=="__main__":
    main()