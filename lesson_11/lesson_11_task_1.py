import datetime
import random


class Date:
    def __init__(self, datestr):
        self.datestr = datestr

    def __str__(self):
        return self.datestr.replace("-", "")

    @classmethod
    def convert_to_number(cls, datestr):

        if len(str(datestr)) != 8:
            raise TypeError("Invalid date")

        day = int(str(datestr)[0:2])
        m = int(str(datestr)[2:4])
        y = int(str(datestr)[4:8])
        Date.validate_date(day, m, y)
        return int(str(day) + str(m) + str(y))

    @staticmethod
    def validate_date(day, m, y):

        if day > 31:
            raise TypeError("Invalid day, maximum value 31!")

        if m > 12:
            raise TypeError("Invalid month, maximum value 12!")

        if y > 3000:
            raise TypeError("Invalid year, maximum value 2999!")


start_date = datetime.date(2000, 1, 1)
end_date = datetime.date(2022, 2, 1)

time_between_dates = end_date - start_date
days_between_dates = time_between_dates.days
random_number_of_days = random.randrange(days_between_dates)
random_date = start_date + datetime.timedelta(days=random_number_of_days)

date_3 = Date.convert_to_number(Date(random_date.strftime("%d-%m-%Y")))
print(date_3)
