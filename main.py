import sqlite3
import populate_database

connection = sqlite3.connect('filenames.db')
cursor = connection.cursor()

def searchTable():

   movieFound = False

   fileToSearchFor = input("Please enter the name of the movie you are looking for: ")
   
   searchResults = cursor.execute("SELECT * FROM files WHERE fileName LIKE ?", ('%'+fileToSearchFor+'%',))

   for name in searchResults:
      print(name[0])
      movieFound = True

   if not movieFound:
      print("File does not exist")

searchTable()