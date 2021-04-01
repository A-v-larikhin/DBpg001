from connector import connect_to_db


con = connect_to_db()
cur = con.cursor()
insert_in_test1 = "DELETE from TEST1 where ADMISSION = 3"
cur.execute(insert_in_test1)
con.commit()
con.close()
