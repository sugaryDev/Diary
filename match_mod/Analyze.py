import database.Database as db


class Analyze:

    def __init__(self, database_name):
        self.database_link = database_name

    def analyze_sugar(self):
        """
        Метод находит среднее арифметическое сахаров за весь промежуток времени (за все записи).
        :return: Возвращает среднее значение.
        """
        database = db.Database(self.database_link)
        sugar = []
        average = 0.0
        for row in database.connection.cursor().execute("SELECT sugar FROM records_database"):
            sugar.extend(list(map(float, row)))
        for i in range(len(sugar)):
            average += sugar[i]
        return average / len(sugar)

    def analyze_on_date(self, first_date, end_date):
        database = db.Database(self.database_link)
        date1 = []
        date2 = []

        for row in database.connection.cursor().execute("SELECT id FROM records_database WHERE date = %s" % first_date):
            date1.extend(list(map(str,row)))
        for row in database.connection.cursor().execute("SELECT id FROM records_database WHERE date = %s" % end_date):
            date2.extend(list(map(str,row)))

