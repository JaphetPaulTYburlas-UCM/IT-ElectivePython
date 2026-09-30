"""
a program that would accept positive integer value from 1 to 50,
display all even numbers
"""
from os import system
def main()->None:
    system("cls")
    try:
        a:int = int(input("Enter value(1..50):"))
        if a>0 and a<51:
            for i in range(1,a+1):
                if (i%2) == 0:
                    print(i,end=" ")
        else:
            print("accept only 1 to 50")
    except Exception as e:
        print(f"Invalid Input: {e}")
    
if __name__=="__main__":
    main()