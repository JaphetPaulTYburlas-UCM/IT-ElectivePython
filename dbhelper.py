'''
	sqlite database
'''
from sqlite3 import connect,Row

database:str = 'school.db'

def createdb()->None:
    conn:any = connect(database)
    sql:str = "CREATE TABLE `students`(id integer primary key autoincrement,idno varchar(10) unique,lastname varchar(50),firstname varchar(50),course varchar(10),level varchar(5))"
    cursor:any = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()

def addstudent(**kwargs)->bool:
    keys:list = list(kwargs.keys())
    vals:list = list(kwargs.values())
    flds:str = "`,`".join(keys)
    data:str = "','".join(vals)
    sql:str = f"INSERT INTO `students`(`{flds}`) VALUES('{data}')"
    conn:any = connect(database)
    cursor:any = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()
    return True if cursor.rowcount>0 else False
    
def getall(table:str)->list:
    sql:str = f"SELECT * FROM `{table}`"
    conn:any = connect(database)
    conn.row_factory = Row
    cursor:any = conn.cursor()
    cursor.execute(sql)
    data:list = cursor.fetchall()
    cursor.close()
    conn.close()
    return data

def getrecord(table:str,idno:str)->list:
    sql:str = f"SELECT * FROM `{table}` WHERE `idno`='{idno}'"
    conn:any = connect(database)
    conn.row_factory = Row
    cursor:any = conn.cursor()
    cursor.execute(sql)
    data:list = cursor.fetchall()
    cursor.close()
    conn.close()
    return data
    

def deleterecord(table:str,idno:str)->list:
    sql:str = f"DELETE FROM `{table}` WHERE `idno`='{idno}'"
    conn:any = connect(database)
    cursor:any = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()
    return True if cursor.rowcount>0 else False
    
def updaterecord(table:str,**kwargs)->bool:
    keys:list = list(kwargs.keys())
    vals:list = list(kwargs.values())
    newflds:list = []
    for i in range(1,len(keys)):
        newflds.append("`"+keys[i]+"`='"+vals[i]+"'")
    flds:str = ",".join(newflds)
    sql:str = f"UPDATE `{table}` SET {flds} WHERE `{keys[0]}`='{vals[0]}'"
    conn:any = connect(database)
    cursor:any = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()
    return True if cursor.rowcount>0 else False
    
  
def main()->None:
    # print(addstudent(idno='1001',lastname='durano',firstname='dennis',course='bscpe',level='4'))
    # print(addstudent(idno='1002',lastname='alpha',firstname='delta',course='bscs',level='3'))
    # print(addstudent(idno='1003',lastname='bravo',firstname='echo',course='bsit',level='2'))
    # print(addstudent(idno='1004',lastname='charlie',firstname='foxtrot',course='bsit',level='1'))
    students:list = getall('students')
    for student in students:
        print(f"{student['idno']}\t{student['lastname']}\t{student['firstname']}\t{student['course']}\t{student['level']}")
    print(updaterecord('students',idno='1000',lastname='xxx',firstname='yyy',course='bsba',level='2'))
    students:list = getall('students')
    for student in students:
        print(f"{student['idno']}\t{student['lastname']}\t{student['firstname']}\t{student['course']}\t{student['level']}")
    
    
if __name__=="__main__":
    main()