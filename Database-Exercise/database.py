'''
Dev: Steve L.
Script description: SQLite3 data base configuration
'''
#Import engine database package
import sqlite3

#Create a database connection (DB Name)
con = sqlite3.connect('Database-Exercise/market.db')
#Cursor let us execute sql commands or operations (Query)
cursor = con.cursor()

#Create users table
user_table = '''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        firstname TEXT NOT NULL,
        lastname TEXT NOY NULL,
        ide_number VARCHAR(15) UNIQUE NOT NULL,
        email TEXT UNIQUE NOT NULL,
        status BOOLEAN DEFAULT true,
        created_at TIMESTAMP DEFAULT (datetime('now','localtime')),
        updated_at TIMESTAMP DEFAULT (datetime('now','localtime')),
        deleted_at TIMESTAMP NULL
    );
'''
#Execute SQL
cursor.execute(user_table)
#Save changes in database => Push to database
con.commit()