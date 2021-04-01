from connector import connect_to_db


con = connect_to_db()
cur = con.cursor()
selecter_from_test1 = "SELECT admission, name, value, value2 from TEST1"
cur.execute(selecter_from_test1)
rows = cur.fetchall()
for row in rows:
    print(row)
con.close()