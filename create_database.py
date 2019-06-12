import sqlite3

connection = sqlite3.connect('filenames.db')
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS files (fileName text)")

connection.commit()
connection.close()