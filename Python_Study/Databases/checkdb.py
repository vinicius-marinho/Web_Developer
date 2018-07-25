import sqlite3

db = sqlite3.connect("contacts.sqlite")
cursor = db.cursor()

nome = input("Informe um nome: ")

update_nome = "Insert into contacts(name) values(?)"

db.execute(update_nome, (nome,))

cursor.execute("Select name from contacts where name=?", (nome,))

for name in cursor.execute("Select name from contacts where name=?", (nome,)):
    print(name)



cursor.close()
db.commit()
db.close()


