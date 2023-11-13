from ZODB import FileStorage, DB
import os

class Database:
    def __init__(self, filename="db/comedor.fs"):
        self.filename = filename
        self.storage = FileStorage.FileStorage(filename)
        self.db = DB(self.storage)
        self.connection = self.db.open()
        self.root = self.connection.root

    def close(self):
        self.connection.close()
        self.db.close()
