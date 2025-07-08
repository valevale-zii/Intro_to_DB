import pymysql

try:
    connection = pymysql.connect(
        host='localhost',
        user='Vale',
        password='Valezozi!14'
    )
    with connection.cursor() as cursor:
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("✅ Database 'alx_book_store' created successfully!")
    connection.close()

except Exception as e:
    print("❌ Error:", e)
