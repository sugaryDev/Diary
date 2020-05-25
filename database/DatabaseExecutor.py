import database.db as db


class DatabaseExecutor(db.Database):

    def insert_records(self, date, sugar, record):
        self.update("INSERT INTO records_database (date, sugar, record) VALUES ('%s', '%s', '%s')" %
                    (date, sugar, record))