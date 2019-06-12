import sqlite3
import populate_database

connection = sqlite3.connect('filenames.db')
cursor = connection.cursor()

def searchTable():
   fileToSearchFor = input("Please enter the name of the movie you are looking for: ")
   
   for name in cursor.execute("SELECT * FROM files WHERE fileName LIKE ?", ('%'+fileToSearchFor+'%',)):
      print(name)

searchTable()