import sqlite3

def show_all():
    # koneksi database 
    conn = sqlite3.connect("test.db")

    # membuat kursor
    c = conn.cursor()
    # query the database 
    c.execute("SELECT rowid, * FROM custumers")
    items = c.fetchall()

    for item in items:
        print(item)

    # commit our command
    conn.commit()

    # close our connection
    conn.close()

# Add new record
def add_one(first, last, email):
    conn = sqlite3.connect("test.db")
    c = conn.cursor()
    c.execute("INSERT INTO custumers VALUES (?,?,?)", (first, last, email))
    conn.commit()
    conn.close()


def add_many(list):
    conn = sqlite3.connect("test.db")
    c = conn.cursor()
    c.executemany("INSERT INTO custumers VALUES (?,?,?)", (list))
    conn.commit()
    conn.close()

# delete record from table 
def delete_one(id):
    conn = sqlite3.connect("test.db")
    c = conn.cursor()
    c.execute("DELETE from custumers WHERE rowid = (?)", id)

    conn.commit()
    conn.close()

# Lookup with Where 
def email_lookup(email):
    conn = sqlite3.connect("test.db")
    c = conn.cursor()
    c.execute("SELECT rowid, * from custumers WHERE email = (?)", (email, ))
    items = c.fetchall()

    for item in items:
        print(item)

    conn.commit()
    conn.close()




