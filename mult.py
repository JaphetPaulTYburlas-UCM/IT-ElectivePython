"""
nested-loop example:
--------------------
A program that would accept a positive integer not greater 
twenty(20), the value represents the row and column of a
multiplication table
"""
from os import system
def main()->None:
    system("cls")
    try:
        n:int = int(input("Enter n(1..20):"))
        #input validation
        if n>0 and n<21:
            for i in range(1,n+1): #outer loop
                for j in range(1,n+1):
                    print(f"{i*j:>4}",end=" ")
                print()
        else:
            print("Accept only 1 to 20 !!!")
            
    except Exception as e:
        print(f"Invalid Input:{e}")
    
if __name__=="__main__":
    main()