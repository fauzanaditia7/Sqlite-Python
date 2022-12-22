from prettytable import PrettyTable
import sqlite3

class Database:
    def __init__(self):
        self.db = sqlite3.connect("database.db")
        self.cur = self.db.cursor()
        self.table_name: str = "mahasiswa"
        self.initTable()

    def initTable(self):
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS %s (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama VARCHAR(50),
            npm INTEGER,
            jurusan VARCHAR(60)
        );""" % (self.table_name))

    def insert(self, nama: str, npm: int, jurusan: str):
        q = "INSERT INTO %s VALUES (null, '%s', %d, '%s')" % (
            self.table_name, nama, npm, jurusan
            )
        self.cur.execute(q)
        self.db.commit()

    def show(self):
        table = PrettyTable()
        table.field_names = ['ID', 'Nama', 'NPM', 'Jurusan']
        result = self.cur.execute("SELECT * FROM %s" % (self.table_name))
        table.add_rows([[i[0], i[1], i[2], i[3]] for i in result.fetchall()])
        return table

    def fetchOne(self, id: int):
        return self.cur.execute("SELECT * FROM %s WHERE id = %d" % (self.table_name, id)).fetchone()
