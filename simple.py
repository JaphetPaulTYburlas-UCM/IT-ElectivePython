"""
a program that would accept two(2) integers
compute and display their sum,difference,
product and quotient
respectively
"""
from os import system #press ctrl-d to repeat the line
def main()->None:
    system("cls")
    try:
        a:int = int(input("Enter 1st value:"))
        b:int = int(input("Enter 2nd value:"))
        print("-"*27)
        print(f"the sum of {a} and {b} is {a+b}")
        print(f"the difference of {a} and {b} is {a-b}")
        print(f"the product of {a} and {b} is {a*b}")
        print(f"the quotient of {a} and {b} is {a/b}")
    except Exception as e:
        print(f"invalid input : {e}")
    
if __name__=="__main__":
    main()