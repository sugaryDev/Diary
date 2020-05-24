import _sqlite3 as sqlite


class Database:
    connection = None

    def __init__(self, database):
        self.connection = sqlite.connect(database)

    def create_table(self):
        """
        Поля:
            id - Integer,
            date - String,
            sugar - Float,
            record - String.
        """
        create_table = """
        CREATE TABLE IF NOT EXISTS records_database 
        ( id INTEGER PRIMARY KEY AUTOINCREMENT, date TEXT, sugar REAL, record TEXT)
        """
        self.connection.cursor().execute(create_table)

    def insert_values(self, date, sugar, record):
        """
        Метод ввода данных.
        :param date: дата.
        :param sugar: сахар.
        :param record: запись.
        """
        insert_values = "INSERT INTO records_database (date, sugar, record) VALUES (?, ?, ?)"
        placeholders = date, sugar, record
        self.connection.cursor().execute(insert_values, placeholders)
        self.connection.commit()

    def data_request(self, param):
        """
        Метод для запроса данных по полям. Пример: * - все ,date - даты, record - записи.
        :param param: название поля таблицы.
        """
        data_request = """SELECT %s FROM records_database """ % param
        data = []
        for row in self.connection.cursor().execute(data_request):
            data.append(row)
        return data

    def data_request_where(self, parameter, parameter2, value):
        """
        Метод запрашивает конкретные значения из конкретных полей таблицы.
        Пример: Если parameter_1 = *,parameter_2 = date, value - 10/10/10,
        то на эран выйдут все записи содержащие 10/10/10.

        :param parameter: имя выводимого поля таблицы.
        :param parameter2: имя искомого значения поля таблицы
        :param value: значение искомого поля записи.
        """

        data_request_where = "SELECT ? FROM records_database WHERE ? = ?"
        placeholders = parameter, parameter2, value
        for row in self.connection.cursor().execute(data_request_where,placeholders):
            print(row)

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
