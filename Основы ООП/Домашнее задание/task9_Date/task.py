class Date:
    def __init__(self, day: int, month: int, year: int):
        self.day = None
        self.month = None
        self.year = None
        self.init_day(day)
        self.init_month(month)
        self.init_year(year)

    def init_day(self, day: int) -> None:
        if not isinstance(day, int):
            raise TypeError('nonono day')
        self.day = day

    def init_month(self, month: int) -> None:
        if not isinstance(month, int):
            raise TypeError('nonono month')
        self.month = month

    def init_year(self, year: int) -> None:
        if not isinstance(year, int):
            raise TypeError('nonono year')
        self.year = year

    def __repr__(self) -> str:
        return f"{str(self.day).rjust(2, '0')}/{str(self.month).rjust(2, '0')}/{self.year}"


    def __str__(self) -> str:
        return f"{str(self.day).rjust(2, '0')}/{str(self.month).rjust(2, '0')}/{self.year}"

if __name__ == "__main__":
    date = Date(1, 15, 1985)
    print(date)



# TODO class Date