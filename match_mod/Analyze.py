import database.Database as db
import database.db as dbd

class Analyze:

    def __init__(self, database_name):
        self.database_link = database_name

    def analyze_average(self):
        """
        Среднее значение сахара за все время
        :return: Возвращает среднее значение
        """
        query = "SELECT sugar FROM records_database"
        database = dbd.Database("database/database.db")
        average = []
        for row in database.query(query):
            average.extend(list(map(float, row)))
        return sum(average)/len(average)

    def analyze_on_date(self, first_date, second_date ):
        """
        Вычисляет средний сахар за данный промежуток времени
        :param first_date: первая граница диапазона
        :param second_date: вторая граница диапазона
        :return: возвращает среднее значение
        """
        id_query = "SELECT id FROM records_database WHERE date = '%s' OR date = '%s'" % (first_date, second_date)
        id_list = []
        average = []
        print(id_query)
        database = dbd.Database("database/database.db")
        for row in database.query(id_query):
            id_list.extend(list(map(int, row)))
        min_id, max_id = min(id_list), max(id_list)
        sugar_query = "SELECT sugar FROM records_database WHERE id >= %s and id <= %s " % (min_id, max_id)
        for row in database.query(sugar_query):
            average.extend(list(map(float, row)))
        return sum(average)/len(average)





