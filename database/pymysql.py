import mysql.connector as sql

localhost = input('Enter the hostname: ')
user = input('Enter the username: ')
password = input('Enter the password: ')
database = input('Enter the database name: ')

con = sql.connect(host = localhost, user = user, password = password, database = database)
cur = con.cursor()

def create_table():
    sql = 'create table sal(Name varchar(50), Salary int(10))'
    cur.execute(sql)
    con.commit()

def insert_data():
    sql = 'insert into sal(name,salary) values(%s, %s)'
    val = [('John', 10000), ('Jane', 20000), ('Jack', 30000), ('Jill', 40000), ('Joe', 50000), ('Jenny', 60000), ('Jeth', 70000), ('Jem', 80000), ('Jenny', 90000)]
    cur.executemany(sql, val)
    con.commit()
    cur.close()
    con.close()

def get_max():
    sql = 'select max(salary) from sal'
    cur.execute(sql)
    con.commit()

def get_min():
    sql = 'select min(salary) from sal'
    cur.execute(sql)
    con.commit()

def avg_sal():
    sql = 'select avg(salary) from sal'
    cur.execute(sql)
    con.commit()

ch = int(input('1. CREATE TABLE \n 2. INSERT DATA \n 3. GET MAX \n 4. GET MIN \n 5. AVG SAL \n 6. EXIT \n Enter your choice: '))

while True:
    if ch == 1:
        create_table()
    elif ch == 2:
        insert_data()
    elif ch == 3:
        get_max()
    elif ch == 4:
        get_min()
    elif ch == 5:
        avg_sal()
    else:
        break
