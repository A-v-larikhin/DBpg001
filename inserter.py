from connector import connect_to_db


con = connect_to_db()
cur = con.cursor()
insert_in_test1 = "INSERT INTO TESTSCHEME01 (ID, PURCHASENUMBER, HREF, MAXPRICE) VALUES (3434334, 345345, 'fdsdhhfdghf', 12443.08)"
cur.execute(insert_in_test1)
con.commit()
con.close()
