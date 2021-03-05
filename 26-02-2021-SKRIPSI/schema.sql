DROP TABLE IF EXISTS pemilik_produk;
DROP TABLE IF EXISTS affiliater;

CREATE TABLE pemilik_produk (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_company TEXT NOT NULL,
    email_company TEXT NOT NULL,
    password_company TEXT NOT NULL,
    domain_company TEXT NOT NULL
);

CREATE TABLE affiliater (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_user TEXT NOT NULL,
    email_user TEXT NOT NULL,
    password_user TEXT NOT NULL,
    id_company INTEGER NOT NULL,
    FOREIGN KEY (id_company)
        REFERENCES pemilik_produk (id)
);
