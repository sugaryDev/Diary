import sqlite3 as sqlite


class Database:

    connection = None
    url = "database/database.db"

    def __init__(self, url):
        if self.url == "":
            self.url = url

    def get_connection(self):
        if self.connection == None:
            self.connection = sqlite.connect(self.url)

    def query(self, query):
        if self.connection == None:
            self.get_connection()
        return self.connection.cursor().execute(query)

    def update(self,statement):
        if self.connection == None:
            self.get_connection()
        self.connection.cursor().execute(statement)
        self.connection.commit()

    def delete_table(self, table_name):
        """
        Удаление таблицы.
        :param table_name: Имя удаляемой таблицы.
        """
        delete_table = "DROP TABLE %s " % table_name
        self.connection.cursor().execute(delete_table)

    def delete_records(self, table_name):
        """
        Удаляет ВСЕ записи таблицы.
        :param table_name: Имя таблицы в которой удаляются записи.
        """
        delete_records = "DELETE FROM %s" % table_name
        self.connection.cursor().execute(delete_records)