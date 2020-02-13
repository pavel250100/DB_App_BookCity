import sqlite3

class Database:

    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS BookCity (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn integer)")
        self.conn.commit()

    def insert(self, title, author, year, isbn):
        self.cur.execute("INSERT INTO BookCity VALUES (NULL,?,?,?,?)", (title, author, year, isbn))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM BookCity")
        rows = self.cur.fetchall()
        return rows

    def delete(self, id):
        self.cur.execute("DELETE FROM BookCity WHERE id = ?", (id,))
        self.conn.commit()

    def search(self, title = "", year = "", author = "", isbn = ""):
        self.cur.execute("SELECT * FROM BookCity WHERE title = ? OR author = ? OR year = ? OR isbn = ?", (title, author, year, isbn))
        rows = self.cur.fetchall()
        return rows

    def update(self, id, title, author, year, isbn):
        self.cur.execute("UPDATE BookCity SET title = ?, author = ?, year = ?, isbn = ? WHERE id = ?", (title, author, year, isbn, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()




