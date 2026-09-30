"""
	display your name at the center of the screen
	"dennis s. durano"
"""
from os import system
def main()->None:
    system("cls")
    name:str = "UNIVERSITY OF CEBU-MAIN CAMPUS"
    print(" "*(120*13),end="")#prevent the carraige return for the print() function
    print(name.center(120-len(name)))
    print(" "*(120*13),end="")
    
if __name__=="__main__":
    main()