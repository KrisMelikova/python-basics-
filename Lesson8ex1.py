class Date:

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def extract(cls, string):
        day, month, year = map(int, string.split('-'))
        my_date = cls(day, month, year)
        return my_date

    @staticmethod
    def valid(string):
        day, month, year = map(int, string.split('-'))
        return day <= 31 and month <= 12 and year <= 2020

date_info = Date.extract('18-05-2020')
is_valid = Date.valid('18-05-2020')
