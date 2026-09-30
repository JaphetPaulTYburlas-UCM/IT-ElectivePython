"""
    <YOUR NAME HERE> 
    IT-ELECPYTHON
    1:30-3:00 MW
    23630 
	multiuser login
	---------------
"""
from os import system
from pwinput import pwinput
from colorama import Fore, Back, Style,just_fix_windows_console

just_fix_windows_console()

users:list = [
    {'email':'foxtrot@uc.com','password':'user123'},
    {'email':'golf@uc.com','password':'user123'},
    {'email':'hotel@uc.com','password':'user123'},
    {'email':'india@uc.com','password':'user123'},
]

email:str = None
password:str = None

def loginform(formname:str)->None:
    def decorator(func)->None:
        def wrapper()->None:
            global email,password
            system("cls")
            print(formname.upper().center(40,"-"))
            email=input("E-MAIL :")
            password=pwinput("PASSWORD :")
            return func()
        return wrapper
    return decorator
    
@loginform("user login")    
def login()->bool:
    user:any = {'email':email,'password':password}
    #print(user)
    ok:bool = True if user in users else False
    return ok
    
@loginform("new user")
def adduser()->None:
    user:any = {'email':email,'password':password}
    users.append(user)
    print("New User Added")
    
def removeuser(email:str)->bool:
    pass  
    
def showlist()->None:
    system("cls")
    print(Fore.GREEN +"-"*50)   
    print(Fore.YELLOW+"N",end="")
    print(Fore.GREEN+"ew  ",end="")
    print(Fore.YELLOW+"D",end="")
    print(Fore.GREEN+"elete ",end="")
    print(Style.BRIGHT+Fore.YELLOW +"USER LIST".rjust(38))
    print(Fore.GREEN +"-"*50)   
    for user in users:
        print(f"{user['email']:<20}"+" "*10+f"{user['password']:>20}")
    #list comprehension
    #[print(f"{user['email']:>10}"+" "*10+f"{user['password']:>20}") for user in users]
    print("nothing follows".upper().center(50,"-"))
    input("Enter Option:")
    print(Fore.WHITE+"")
    
def main()->None:
    ok:bool = login()
    message:str = "LOGIN SUCCESS" if ok else "LOGIN FAILED"
    print("\n"+message)
    input("Press any key to continue")
    if ok: showlist()
    
if __name__=="__main__":
    main()




