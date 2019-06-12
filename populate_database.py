import os
import sqlite3

connection = sqlite3.connect('filenames.db')
cursor = connection.cursor()

rawFileNames = []
cleanedFileNames = []

#gets file names from the hard drive and adds them to a list of uncleaned names
def getFileNames():
   for root, dirs, files in os.walk("directory name goes here", topdown=False):
      for name in files:
         rawFileNames.append(os.path.splitext(name)[0])

#iterates through the file names, cleans them, and adds them to a list of cleaned file names
def cleanFileNames():
   cleanedName = " "
   for name in rawFileNames:
      cleanedName = name.replace(".", " ")
      cleanedFileNames.append(cleanedName)
      cleanedName = " "

#iterates through list of cleaned names and adds them to the database
def addNamesToTable():
   for name in cleanedFileNames:
      cursor.execute("INSERT INTO files VALUES (?)", (name,))

   connection.commit()

#displays all the files names stored in the database
def displayFileNames():
   for name in cursor.execute("SELECT * FROM files"):
      print(name)

if __name__ == "__main__":
    getFileNames()
    cleanFileNames()
    addNamesToTable()