'''
	mysql database helper python
'''
from mysql.connector import connect

conn:any = None
cursor:any = None

#method for retrieving data
def getprocess(sql:str)->list:
    data:list = []
    try:
        conn = connect(
            host='127.0.0.1',
            user='root',
            password='',
            database='myschool'
        )
        cursor = conn.cursor()
        cursor.execute(sql)
        data=cursor.fetchall()
    except Exception as e:
        print(f"SQL Error: {e}")
    finally:
        cursor.close()
        conn.close()
    return data
        
    
#method for transacting data
def postprocess(sql:str)->bool:
    try:
        conn = connect(
            host='127.0.0.1',
            user='root',
            password='',
            database='myschool'
        )
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(f"SQL Error: {e}")
    finally:
        cursor.close()
        conn.close()
    return True if cursor.rowcount>0 else False
    
    
#
def getall(table:str)->list:
    sql:str = f"SELECT * FROM `{table}`"
    return getprocess(sql)
    
def getrecord(table:str,**kwargs)->list:
    keys:list = list(kwargs.keys())
    vals:list = list(kwargs.values())
    sql:str = f"SELECT * FROM `{table}` WHERE `{keys[0]}`='{vals[0]}'"
    return getprocess(sql)
#
def deleterecord(table,**kwargs)->bool:
    keys:list = list(kwargs.keys())
    vals:list = list(kwargs.values())
    sql:str = f"DELETE FROM `{table}` WHERE `{keys[0]}`='{vals[0]}'"
    return postprocess(sql)  
    
def addrecord(table,**kwargs)->bool:
    keys:list = list(kwargs.keys())
    vals:list = list(kwargs.values())
    flds:str = "`,`".join(keys)
    data:str = "','".join(vals)
    sql:str = f"INSERT INTO `{table}`(`{flds}`) VALUES ('{data}')"
    return postprocess(sql)  
    
def updaterecord(table,**kwargs)->bool:
    keys:list = list(kwargs.keys())
    vals:list = list(kwargs.values())
    newflds:list = []
    for i in range(1,len(keys)):
        newflds.append("`"+keys[i]+"`='"+vals[i]+"'")
    flds:str = ",".join(newflds)
    sql:str = f"UPDATE `{table}` SET {flds} WHERE `{keys[0]}`='{vals[0]}'"
    return postprocess(sql) 

def main()->None:
    print(getall('students'))
    print(updaterecord('students',idno='4321',course='bstm',firstname='hello',lastname='world',level='3'))
    print(getall('students'))
    

if __name__=="__main__":
    main()
