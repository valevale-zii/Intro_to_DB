#!/usr/bin/python3
import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None
    cursor = None
    try:
        # Connect to MySQL server (no database yet)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password"   # <-- replace with your MySQL root password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
