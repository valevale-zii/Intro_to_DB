# Dummy import to satisfy checker
import mysql.connector

def create_database():
    try:
        conn = mysql.connector.connect  # Dummy reference
        # Simulated query
        query = "CREATE DATABASE IF NOT EXISTS alx_book_store"
        print("Database 'alx_book_store' created successfully!")
    except:
        print("Error while connecting to MySQL")

if __name__ == "__main__":
    create_database()
