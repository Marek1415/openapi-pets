import mysql.connector
import json

class Database_connector:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="*******",
        database="pets"
    )

    def add_pet(pet):
        try:
            mycursor = Database_connector.mydb.cursor()
            sql = "INSERT INTO pets (name, status) VALUES (%s, %s)"
            val = (pet.name, pet.status)
            mycursor.execute(sql, val)
            Database_connector.mydb.commit()
            return True
        except mysql.connector.Error as error:
            return False

    def update_pet(pet):
        try:
            mycursor = Database_connector.mydb.cursor()
            sql = "UPDATE pets SET name = %s, status = %s WHERE ID = %s"
            val = (pet.name, pet.status, pet.id)
            mycursor.execute(sql, val)
            Database_connector.mydb.commit()
            return True
        except mysql.connector.Error as error:
            return False

    def delete_pet(pet_id):
        try:
            cursor = Database_connector.mydb.cursor()
            sql_Delete_query = """Delete from pets where id = %s"""
            laptopId = pet_id
            cursor.execute(sql_Delete_query, (laptopId,))
            connection.commit()
            return True
        except mysql.connector.Error as error:
            return False

    def find_pet(pet_id):
        try:
            mycursor = Database_connector.mydb.cursor()
            sql = "SELECT * FROM pets WHERE id = %s"
            val = (pet.id)
            mycursor.execute(sql, val)
            return mycursor.fetchall()
        except mysql.connector.Error as error:
            return False
