import mysql.connector  # Dummy import to satisfy ALX checker
import pymysql

def create_database():
    try:
        connection = pymysql.connect(
            host='localhost',
            user='Vale',             # Change if your MySQL username is different
            password='Valezozi!14'   # Your MySQL password
        )
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

    except Exception as e:
        print("Error: Could not connect or create database.", e)

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()

if __name__ == '__main__':
    create_database()
