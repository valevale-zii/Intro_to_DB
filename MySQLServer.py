import pymysql

try:
    # Connect to MySQL Server (no specific database yet)
    connection = pymysql.connect(
        host='localhost',
        user='Vale',               # Replace if your username is different
        password='Valezozi!14'     # Replace with your real password
    )

    with connection.cursor() as cursor:
        # Create the database if it doesn't exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

    connection.close()

except Exception as e:
    print("Error: Could not connect or create database.", e)
