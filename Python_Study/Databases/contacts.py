import sqlite3


class Database(object):

    def __init__(self):
        self.db = sqlite3.connect("contacts.sqlite")
        self.cursor = self.db.cursor()

    def cria_data(self):
        self.db.execute("CREATE TABLE IF NOT EXISTS contacts(name TEXT NOT NULL, phone INTEGER, email TEXT)")
        self.db.execute("INSERT INTO contacts(name, phone, email) VALUES('Tim', 64578, 'teste@teste.com')")
        self.db.execute("INSERT INTO contacts VALUES('Brian', 45785, 'email@email.com')")


    def consulta_dados(self, consulta):
        self.cursor.execute(consulta)
        for name, phone, email in self.cursor:
            print("Nome - " + name)
            print("Telefone - " + str(phone))
            print("E-mail - " + email)
            print("*" * 30)
        self.fecha()

    def fecha(self):
        self.cursor.close()
        self.db.commit()
        self.db.close()


banco = Database()
banco.cria_data()
banco.consulta_dados("SELECT * FROM contacts")

# cursor = db.cursor()
# cursor.execute("SELECT * FROM contacts")
# for row in cursor:
#     print(row)
# cursor.close()
# db.close()

