import pymysql

def validate_data():
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="Secret123",
        database="prog8850"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM large_table WHERE email IS NULL")
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return len(results) == 0
