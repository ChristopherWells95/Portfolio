import sqlite3

# Connect to the database (or create it if it doesn't exist)
db = sqlite3.connect('python_programming.db')
cursor = db.cursor()

# 1. Create the table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS python_programming (
        id INTEGER PRIMARY KEY,
        name TEXT,
        grade INTEGER
    )
''')

# 2. Insert rows into the table
students = [
    (55, 'Carl Davis', 61),
    (66, 'Dennis Fredrickson', 88),
    (77, 'Jane Richards', 78),
    (12, 'Peyton Sawyer', 45),
    (2, 'Lucas Brooke', 99)
]

cursor.executemany('INSERT OR IGNORE INTO python_programming (id, name, grade) VALUES (?, ?, ?)', students)

# 3. Select records with grade between 60 and 80
cursor.execute('SELECT * FROM python_programming WHERE grade BETWEEN ? AND ?', (60, 80))
results = cursor.fetchall()
print("Students with grades between 60 and 80:")
for row in results:
    print(row)

# 4. Update Carl Davis's grade to 65
cursor.execute('UPDATE python_programming SET grade = ? WHERE name = ?', (65, 'Carl Davis'))

# 5. Delete Dennis Fredrickson's row
cursor.execute('DELETE FROM python_programming WHERE name = ?', ('Dennis Fredrickson',))

# 6. Change grade to 80 for students with id > 55
cursor.execute('UPDATE python_programming SET grade = ? WHERE id > ?', (80, 55))

# Commit the changes and close the connection
db.commit()
db.close()
