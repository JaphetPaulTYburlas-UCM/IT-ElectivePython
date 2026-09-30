"""
a program that would accept and positive integer value
not greater twenty(20), display all values
from 1 to the inputted value

ex:
input : 5
output: 1 2 3 4 5
"""
from os import system
def main()->None:
    system("cls")
    try:
        a:int = int(input("Enter value(1..20):"))
        if a>0 and a<21: #input validation
            i:int = 1 #iterator
            while i<=a: #condition
                print(i,end=" ")
                i+=1 #iteration
        else:
            print("Accepts only 1 to 20")
    except Exception as e:
        print(f"Invalid Input:{e}")
    
if __name__=="__main__":
    main()