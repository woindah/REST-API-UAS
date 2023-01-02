import mysql.connector

def conn(user="root", password="", host="localhost", database="mahasiswa_ilkom"):
    conn = mysql.connector.connect(
        host=host,
        user=user,
        passwd=password,
        database=database
    )
    return conn

def select(query, values, conn):
    mycursor = conn.cursor()
    mycursor.execute(query, values)
    row_headers = [x[0] for x in mycursor.description]
    myresult = mycursor.fetchall()
    json_data = []
    for result in myresult:
        json_data.append(dict(zip(row_headers, result)))
        return json_data

def insert(query, val, conn):
    mycursor = conn.cursor()
    mycursor.execute(query,val)
    conn.commit()