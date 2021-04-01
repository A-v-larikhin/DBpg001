from connector import connect_to_db


con = connect_to_db()
cur = con.cursor()
insert_in_test1 = "INSERT INTO TEST1 (ADMISSION, NAME, VALUE, VALUE2) VALUES (3, 'sOMEBODY', 50,90)"
cur.execute(insert_in_test1)
con.commit()
con.close()
