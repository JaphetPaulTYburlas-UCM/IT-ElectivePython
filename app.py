'''
	python mysql database 
'''
from mysql.connector import connect
from tabulate import tabulate
from os import system

def updatestudent(**kwargs)->bool:
    keys:list = list(kwargs.keys())
    values:list = list(kwargs.values())
    datalist:list = []
    for i in range(1,len(keys)):
        datalist.append("`"+keys[i]+"`='"+values[i]+"'")
    fields:str = ",".join(datalist)
    sql:str = f"UPDATE `students` SET {fields} WHERE `{keys[0]}`='{values[0]}'"
    conn:any = connect(
        host='127.0.0.1',   #local database server
        database='pythonpm',
        user='root',
        password='',
    )
    cursor:any = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()
    return True if cursor.rowcount>0 else False

def deletestudent(**kwargs)->bool:
    keys:list = list(kwargs.keys())
    values:list = list(kwargs.values())
    sql:str = f"DELETE FROM `students` WHERE `{keys[0]}`='{values[0]}'"
    conn:any = connect(
        host='127.0.0.1',   #local database server
        database='pythonpm',
        user='root',
        password='',
    )
    cursor:any = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()
    return True if cursor.rowcount>0 else False

def addstudent(**kwargs)->bool:
    keys:list = list(kwargs.keys())
    values:list = list(kwargs.values())
    fields:str = ",".join(keys)
    data:str = "','".join(values)
    sql:str = f"INSERT INTO `students`({fields}) VALUES('{data}')"
    conn:any = connect(
        host='127.0.0.1',   #local database server
        database='pythonpm',
        user='root',
        password='',
    )
    cursor:any = conn.cursor()
    cursor.execute(sql) #prepare the data to storing to the db
    conn.commit() #store the prepared data
    conn.close()    #close the database connection, DO NOT FORGET
    return True if cursor.rowcount>0 else False
    

def getall()->None:
    #system('cls')
    conn:any = connect(
        host='127.0.0.1',   #local database server
        database='pythonpm',
        user='root',
        password='',
    )
    cursor:any = conn.cursor()
    sql:str = "SELECT * FROM `students`"
    cursor.execute(sql)
    data:list = cursor.fetchall()
    conn.close()
    # print(data)
    # for item in data:
        # print(f"{item['id']}\t{item['idno']}\t{item['lastname']}\t{item['firstname']}\t{item['course']}\t{item['level']}")
    header=['ID','IDNO','LASTNAME','FIRSTNAME','COURSE','LEVEL']
    print(tabulate(data, headers=header, tablefmt="grid"))
def main()->None:
    #getall()
    #addstudent(idno='1006',lastname='uehara',firstname='ai',course='bsit',level='4')
    getall()
    updatestudent(idno='1000',lastname='fuji',firstname='kanna',course='bscs',level='1')
    getall()
    
    

if __name__=="__main__":
    main()