import sqlite3

db = sqlite3.connect("contacts.sqlite")

email = input("Informe novo email: ")
phone = input("Informe novo numero de telefone: ")

# update_sql = "update contacts set email='outro@outro.com' where phone=45785"
update_sql = "update contacts set email=? where phone=?"
update_cursor = db.cursor()
update_cursor.execute(update_sql, (email, phone))
print("{} rows updated".format(update_cursor.rowcount))

update_cursor.connection.commit()

update_cursor.close()

for name, phone, email in db.execute("select * from contacts"):
    print(name)
    print(phone)
    print(email)


db.close()

db2 = sqlite3.connect("contacts.sqlite")

cursor = db2.cursor()

cursor.execute("select * from contacts")

for x in cursor:
    print(x)

cursor.close()
db2.close()
