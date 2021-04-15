import psycopg2

def connect_to_db():
    con = psycopg2.connect(
        database='testdb',
        user='testuser',
        password='123456',
        host='192.168.10.61'
    )
    return con

if __name__ == '__main__':
    con = connect_to_db()
    cur = con.cursor()

# переменная для создания таблицы 'test1'
    create_table = '''CREATE TABLE TESTSCHEME01
        (KEY BIGSERIAL,
        ID BIGINT,
        PURCHASENUMBER BIGINT,
        HREF TEXT,
        MAXPRICE REAL)'''

# Блок для просмотра таблиц в базе и создания таблицы, если она отсутствует в списке
    select_tables = "SELECT table_name FROM information_schema.tables WHERE table_schema='public'"
    cur.execute(select_tables)
    tables = cur.fetchall()
    button = False
    for i in tables:
        for j in i:
            if 'testscheme01' in j:
                button = True
    if button == False:
        cur.execute(create_table)
    select_tables = "SELECT table_name FROM information_schema.tables WHERE table_schema='public'"
    cur.execute(select_tables)
    tables = cur.fetchall()
    print(tables)
    con.commit()
    con.close()