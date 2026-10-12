from tkinter import Tk,ttk
from dbhelper import *

class StudentInfo:
    def __init__(self)->None:
        self.root = Tk()
        self.root.title("DURANO, Dennis S. (23630)")
        self.root.resizable(False,False)
        self.centerform(700,350)
        self.studentlist()
        self.root.mainloop()
        
    def centerform(self,width:int,height:int)->None:
        screen_width:int = self.root.winfo_screenwidth()
        screen_height:int = self.root.winfo_screenheight()
        xpos:int = (screen_width-width)//2
        ypos:int = (screen_height-height)//2
        self.root.geometry(f"{width}x{height}+{xpos}+{ypos}")
        
    def studentlist(self)->None:
        self.frame = ttk.LabelFrame(self.root,text="STUDENT LIST")
        self.frame.grid(row=0,column=0,padx=10,pady=10)
        self.columns=['id','idno','lastname','firstname','course','level']
        self.tv = ttk.Treeview(self.frame,columns=self.columns,show="headings")
        self.tv.grid(padx=10,pady=10)
        #
        self.tv.heading('id',text="#")
        self.tv.heading('idno',text="IDNO")
        self.tv.heading('lastname',text="LASTNAME")
        self.tv.heading('firstname',text="FIRSTNAME")
        self.tv.heading('course',text="COURSE")
        self.tv.heading('level',text="LEVEL")
        #
        self.tv.column('id',width=50,anchor='center')
        self.tv.column('idno',width=50,anchor='center')
        self.tv.column('lastname',width=150,anchor='w')
        self.tv.column('firstname',width=150,anchor='w')
        self.tv.column('course',width=100,anchor='center')
        self.tv.column('level',width=50,anchor='w')
        #
        students:list = getall('students')
        for student in students:
            self.tv.insert("","end",values=(f"{student[0]}",f"{student[1]}",f"{student[2].upper()}",f"{student[3].upper()}",f"{student[4].upper()}",f"{student[5]}"))
        
    
def main()->None:
    StudentInfo()

if __name__=="__main__":
    main()
