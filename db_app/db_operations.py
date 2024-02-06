import  psycopg2


def create():
    conn = psycopg2.connect(
        host="127.0.0.1",
        port="5432",
        database="test_db",
        user="ovi_2ro",
        password="SomePassword"
        )
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS student (ID SERIAL, NAME TEXT, AGE TEXT, ADDRESS TEXT);
    ''')
    print("Table created")
    conn.commit()
    conn.close()

def insert_data(name, age, address):
    conn = psycopg2.connect(
        host="127.0.0.1",
        port="5432",
        database="test_db",
        user="ovi_2ro",
        password="SomePassword"
        )
    cursor = conn.cursor()

    query = '''INSERT INTO student (NAME, AGE, ADDRESS) VALUES (%s, %s, %s);'''
    cursor.execute(query,(name, age, address))

    print("Data inserted")
    conn.commit()
    conn.close()

def search_data(id):
    conn = psycopg2.connect(
        host="127.0.0.1",
        port="5432",
        database="test_db",
        user="ovi_2ro",
        password="SomePassword"
        )
    cursor = conn.cursor()
    query = '''SELECT * FROM student WHERE id = %s;'''
    cursor.execute(query,(id,))
    result = cursor.fetchone()

    conn.commit()
    conn.close()
    return result

def search_all():
    conn = psycopg2.connect(
        host="127.0.0.1",
        port="5432",
        database="test_db",
        user="ovi_2ro",
        password="SomePassword"
        )
    cursor = conn.cursor()
    query = '''SELECT * FROM student;'''
    cursor.execute(query)
    result = cursor.fetchall()

    conn.commit()
    conn.close()
    return result

