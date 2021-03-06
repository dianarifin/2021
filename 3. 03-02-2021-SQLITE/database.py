import sqlite3

# connect database
conn = sqlite3.connect("costumer.db")

# create a cursor

c = conn.cursor()

# create a table
# c.execute("""CREATE TABLE custumers (
#         first_name text,
#         last_name text,
#         email text
#     )""")

# NULL
# INTEGER
# REAL
# TEXT
# BLOB

# many_customers = [
#                     ('wes', 'brown', 'dianisa@gmail.com'),
#                     ('aka', 'jeje', 'jeje@gmail.com'),
#                     ('adawes', 'broaswn', 'ass@gmail.com'),
#                 ]

# c.executemany("""INSERT INTO custumers VALUES (?,?,?)""", many_customers)


# INSERT INTO TABLE
# c.execute("""INSERT INTO custumers VALUES (
#     'dian', 'yunita', 'akak@gmail.com'
#     )""")


# Update record

# c.execute("""UPDATE custumers SET first_name = "AKa"
#             WHERE rowid = 1
#         """)

# Delete record 
# c.execute("DELETE from custumers WHERE rowid = 2")



# DROP TABLE / MENGHAPUS TABEL 
# c.execute("DROP TABLE custumers")

# query the database
c.execute("SELECT * FROM custumers")

conn.commit()

# c.fetchone()
# c.fetchmany(3)

# print(c.fetchall())
# print(c.fetchone()[0])
# print(c.fetchmany(3))

# items = c.fetchall()
# print("NAME " + "\t\tEMAIL")
# print("-----" + "\t\t-----")
# for item in items:
#     print(item[0] + " " + item[1] + "\t" + item[2])

items = c.fetchall()

for item in items:
    print(item)

print("sukses")

# commit our command
conn.commit()

# close our connection
conn.close()











