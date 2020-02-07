import mysql.connector as mysql

def sql():
    name_db = input("Enter the name of DB\n")
    flag = input("Does DB exists ? (Y/N)")
    if flag == 'n' or flag == 'N':
        db = mysql.connect(host="localhost", user="root", passwd="jarach_dixit@200")
        print("CONNECTED " , db , "\n")
        cursor = db.cursor()
        cursor.execute("Create database " + name_db + ";")
        cursor.execute("show databases;")
        dbs = cursor.fetchall()
        for each in dbs:
            print(each)
        cursor.execute("use " + name_db + ";")
    else:
        db = mysql.connect(host="localhost", user="root", passwd="jarach_dixit@200", database=name_db)
        print("CONNECTED " , db , "\n")
        cursor = db.cursor()
        cursor.execute("show databases;")
        dbs = cursor.fetchall()
        for each in dbs:
            print(each)
        cursor.execute("use " + name_db + ";")
    while 1:
        query = input("Enter the query for Table\n")
        cursor.execute(query)
        cursor.execute("show tables;")
        tbs = cursor.fetchall()
        for each in tbs:
            print(each)
        fname = input("Enter the name of the file containing the values\n")
        file = open(fname, 'r')
        query = input("Enter insert query\n")
        query += "\nvalues"
        query+="\n"
        for line in file:
            query += line
        query = query[0:len(query)-2]+";"
        print(query)
        cursor.execute(query)
        db.commit()
        print(cursor.rowcount, " records inserted\n\n\n Enter XXX to terminate or enter another table query")
        x = input()
        if x == "xxx" or "XXX":
            print("Connection terminated ***\n")
            break
sql()