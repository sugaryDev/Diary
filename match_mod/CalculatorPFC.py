class CalculatorPFC:

    @staticmethod
    def calculate(mass, value):
        """
        Метод находит массу БЖУ в массе продукта.

        :param mass: Масса продукта.
        :param value: Содержание БЖУ/100 грамм продукта.
        :return: Возвращаем массу БЖУ в продукте данной массы.
        """
        if value < 1:
            value *= 100
        return mass * (value / 100)

    @staticmethod
    def bread_unit(carbohydrates):
        return carbohydrates / 12
