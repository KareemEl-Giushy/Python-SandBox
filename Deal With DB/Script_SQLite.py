# ------------------------
# Deal With Database in python
# SQLite 
# ========================
# Connect
# Execute
# Close #
# ------------------------
import sqlite3 as lite

# Create Database
db = lite.connect(r"C:\Users\AUC\Documents\PyProjects\Deal With DB\app.db")

# Cursor: All Opearations In SQL Done By Cursor Not The Connection Itself
cr = db.cursor()

# Create The Tables And Fields
# db.execute("CREATE TABLE IF NOT EXISTS skills (name TEXT, progress INT, user_id INT)")
cr.execute("CREATE TABLE IF NOT EXISTS skills (name TEXT, progress INT, user_id INT)")
cr.execute("CREATE TABLE IF NOT EXISTS users (id INT, name TEXT)")
cr.execute("DELETE FROM users")

# Inserting Data
# cr.execute("INSERT INTO users (id, name) VALUES(1, 'kareem')")
# cr.execute("INSERT INTO users (id, name) VALUES(2, 'ahmed')")
# cr.execute('INSERT INTO users (id, name) VALUES(3, "heba")')
myList = ['kareem', 'hamada', 'mayada', 'medhat', 'mehdi', 'heba', 'ahmed', 'mohee']

for n, user in enumerate(myList):
    cr.execute("INSERT INTO users (id, name) VALUES({:d}, '{:s}')".format(n + 1, user))


# Save Chanages To your Database
db.commit()

# Update Query
cr.execute("UPDATE users SET name = 'Gamal' WHERE id = 3 OR id = 5")

# Delete From Database
cr.execute("DELETE FROM users WHERE id = 1")

# Fetch Data
cr.execute("SELECT * FROM users")
# print(cr.fetchone())
# print(cr.fetchone())
# print(cr.fetchone())

print(cr.fetchall())

# print(cr.fetchmany(4))

# Close Database
db.close()