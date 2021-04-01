import psycopg2


con = psycopg2.connect(
    database='testdb',
    user='testuser',
    password='123456',
    host='192.168.10.61'
)
cur = con.cursor()
cur.execute('''CREATE TABLE TEST1
    (ADMISSION INT PRIMARY KEY NOT NULL,
    NAME TEXT NOT NULL,
    VALUE CHAR(50),
    VALUE2 CHAR(50))''')
con.commit()
con.close()