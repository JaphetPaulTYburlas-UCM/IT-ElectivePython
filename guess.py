"""
GUESSING GAME
-------------
A program that would accept a positive integer value not greater twenty(20), using the random built-in library and use the randint(from,to) to generate an integer, if the inputted value is equal to the generated value, display 'you got it, in n? tries' and terminate the program, else inputted is lesser than the generated value, display "higher" else display "lower"  
"""
from os import system
from random import randint
def main()->None:
    system("cls")
    guess:int = randint(1,20)
    n:int = 0
    count:int = 0
    try:
        while n!=guess:
            n = int(input("Enter n(1..20):"))
            if n>0 and n<21:
                count+=1
                if n<guess:
                    print("HIGHER")
                elif n>guess:
                    print("LOWER")
                elif n==guess:
                    print(f"YOU GOT IT in {count} tries")
            else:
                print("Accept only 1 to 20 !!!")
                
    except Exception as e:
        print(f"Invalid input: {e}")

if __name__=="__main__":
    main()