import db


# db.add_one("Dian", "Arifin", "kash@gmail.com")


# delete record use string 
# db.delete_one('4')

# tambahkan banyak record
stuff =  [
    ('Aku', 'cinta', 'jaja@gmail.com'),
    ('telo', 'dias', 'maka@gmail.com'),
    ('mas', 'dian', 'dua')
]

# db.add_many(stuff)

# Lookup email address 
db.email_lookup("maka@gmail.com")

# db.show_all()



