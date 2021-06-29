import sqlite3




def register(username, password, email):

    conn = sqlite3.connect('register.db')
    c = conn.cursor()

    # c.execute("""CREATE TABLE register (
    #     username text,
    #     password text,
    #     email text
    # )""")

    c.execute("INSERT INTO register (username, password, email) VALUES (?,?,?)", (username, password, email))
    conn.commit()
    conn.close()

def tampil():

    global data

    conn = sqlite3.connect('register.db')
    c = conn.cursor()
    c.execute("SELECT * FROM register")
    data = c.fetchall()
    # print(data)
    conn.commit()
    conn.close()

# def username(inputname):

#     global conn

#     conn = sqlite3.connect('register.db')
#     c = conn.cursor()
#     cari = c.execute("SELECT email FROM register WHERE username = (?)", (inputname,))
#     ada = cari.fetchone()

#     # temp = site.split()
#     # print(site_redirect)
#     conn.commit()
#     conn.close()

# username("masalah")
