from tkinter import Tk, ttk
from sqlite3 import connect
class EmployeeGUI:
    def __init__(self)->None:
        self.root = Tk()
        self.root.title("YBURLAS,Japhet Paul(23630)")
        self.center(500,200)
        self.employeelist()
        self.root.mainloop()
    def center(self,width:int, height:int)-> None:
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        xpos:int = (screen_width-width)//2
        ypos:int = (screen_height-height)//2
        self.root.geometry(f"{width}x{height}+{xpos}+{ypos}")
    def employeelist(self)->None:
        self.frame = ttk.LabelFrame(self.root, text ="Employee List")
        self.frame.grid(padx=10,pady=10)
        self.tv = ttk.Treeview(self.frame, columns = ['id','idno','name','position','date_hired'],show = "headings")
        self.tv.grid(padx = 10, pady = 10)
        #
        self.tv.heading('id',text = 'ID')
        self.tv.heading('idno',text = 'IDNO')
        self.tv.heading('name',text = 'Name')
        self.tv.heading('position',text = 'Position')
        self.tv.heading('date_hired',text = 'Date_Hired')
        #
        self.tv.column('id', width = 50, anchor = "center")
        self.tv.column('idno', width = 50, anchor = "center")
        self.tv.column('name', width = 150, anchor = "w")
        self.tv.column('position', width = 150, anchor = "w")
        self.tv.column('date_hired', width = 50, anchor = "center")
        #
        employees = self.getall('employee')
        for employee in employees:
            self.tv.insert("", "end", values=(employee))
    def getall(self,table:str)->list:
        conn:any=None
        cursor:any = None
        data:list = []
        sql:str = f"SELECT * FROM `{table}`"
        try:
            conn:any = connect('employee.db')
            cursor = conn.cursor()
            cursor.execute(sql)
            data = cursor.fetchall()
        except Exception as e:
            print(f"SQL error{e}")
        finally:
            cursor.close()
            conn.close()
        return data
    
def main()->None:
    EmployeeGUI()
if __name__=="__main__":
    main()
