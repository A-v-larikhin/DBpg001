from connector import connect_to_db


con = connect_to_db()
cur = con.cursor()
insert_in_test1 = "UPDATE TEST1 set NAME = 'Vasya' where ADMISSION = 1"
cur.execute(insert_in_test1)
con.commit()
con.close()
