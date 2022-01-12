class Date:
    """Класс для работы с датами"""
    DAY_OF_MONTH = (
        (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  # обычный год
        (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)  # високосный
    )

    __slots__ = ('day', 'month', 'year')

    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

        self.is_valid_date(self.day, self.month, self.year)

    @staticmethod
    def is_leap_year(year: int):
        """Проверяет, является ли год високосным"""
        return year % 4 == 0

    @classmethod
    def get_max_day(cls, month: int, year: int):
        """Возвращает максимальное количество дней в месяце для указанного года"""
        if cls.is_leap_year(year):
            max_number_days = cls.DAY_OF_MONTH[1][month - 1]
        else:
            max_number_days = cls.DAY_OF_MONTH[0][month - 1]
        return max_number_days


    def is_valid_date(self, day: int, month: int, year: int):
        """Проверяет, является ли дата корректной"""
        if not self.get_max_day(month, year) >= day:
            raise ValueError('nonono1')
        if not 1 <= self.month <= 12:
            raise ValueError('nonono2')


if __name__ == "__main__":

    print(Date(29, 2, 2024))