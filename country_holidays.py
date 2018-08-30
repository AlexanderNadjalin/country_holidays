"""
A simple class that generates and holds all holidays between two dates as a pandas DataFrame.

On initialization set country code, start year and end year. Earliest year is 2000 and latest year is 3000.

"""
import datetime as dt
import pandas as pd
import date_utils as du


MONDAY = 0
TUESDAY = 1
WEDNESDAY = 2
THURSDAY = 3
FRIDAY = 4
SATURDAY = 5
SUNDAY = 6


class Calendar:
    """
    A simple class that generates and holds all holidays between two dates as a pandas DataFrame.

    """
    def __init__(self, country_code: str, start_year: dt.datetime, end_year: dt.datetime) -> None:
        self.country_code = self.add_country_code(country_code)
        self.start_date = self.add_start_year(start_year)
        if start_year < end_year:
            self.end_date = self.add_end_year(end_year)
        self.holidays = pd.DataFrame()

        self.add_holidays()

    def __getattr__(self, item: str) -> object:
        """
        Get the selected attribute.
        :param item: Calendar item.
        :return: Calendar item value.

        """
        try:
            return self.__getitem__(item)
        except KeyError:
            raise AttributeError(item)

    def add_country_code(self, country_code: str) -> str:
        """
        Add country code to Calendar object.

        :param country_code: ISO country code in two letters format (ex. 'SE, 'GB').
        :return: country code as a verified string.
        """
        code = country_code.upper()
        if code != 'SE':
            raise NotImplementedError('Country code ' + code + ' not implemented.')
        else:
            return code

    def add_start_year(self, start_year: dt.datetime) -> dt.datetime:
        """
        Add the first date of a year as a dt.datetime object to the Calendar class object.

        :param start_year: Any date >= 2000-01-01.
        :return: first date of start year as a verified dt.datetime object.
        """
        if isinstance(start_year, dt.datetime):
            if (start_year.year >= 2000) and (start_year.year <= 3000):
                return dt.datetime(start_year.year, 1, 1)
            else:
                raise ValueError('End years before 2000 and after 3000 not implemented.')
        else:
            raise TypeError('Enter end year as integer.')

    def add_end_year(self, end_year):
        """
        Add the last date of a year as a dt.datetime object to the Calendar class object.

        :param end_year: Any date <= 3000-01-01.
        :return: last date of start year as a verified dt.datetime object.
        """
        if isinstance(end_year.year, int):
            if end_year.year <= 3000:
                return dt.datetime(end_year.year, 12, 31)
            else:
                raise ValueError('End years after 3000 not implemented.')
        else:
            raise TypeError('Enter end year as integer.')

    def get_start_year(self) -> int:
        """
        Get Calendar.start_date object.

        :return: Calendar start year.
        """
        return self.start_date.year

    def get_end_year(self) -> int:
        """
        Get Calendar.end_date object.

        :return: Calendar end year.
        """
        return self.end_date.year

    def add_holidays(self) -> None:
        """
        Add holidays for selected Calendar.country_code as pd.DataFrame.

        :return: pandas DataFrame with index dt.datetime and one column with name of the holiday.
        """
        cols = ['holiday_name']
        years = years_list(self.get_start_year(), self.get_end_year())
        frames = []
        for y in years:
            d = dt.datetime(y, 1, 1)
            de = (holidays_list(d, self.country_code))
            frame = pd.DataFrame.from_dict(de, orient='index')
            frames.append(frame)
        m_frame = pd.concat(frames)
        m_frame.columns = cols
        m_frame.sort_index(inplace=True)
        self.holidays = m_frame


def new_years_day(year: dt.datetime) -> dt.datetime:
    """
    New Year's Day. "Nyårsdagen".

    :param year: Year for date.
    :return: Date of the holiday.
    """
    res = dt.datetime(year.year, 1, 1)
    return res


def epiphany(year: dt.datetime) -> dt.datetime:
    """
    Epiphany. "Trettondagen".

    :param year: Year for date.
    :return: Date of the holiday.
    """
    res = dt.datetime(year.year, 1, 6)
    return res


def easter(year):
    """
    Påskdagen
    Calculate the date of Easter in the given year.

    From Wikipedia: http://en.wikipedia.org/wiki/Computus

    """
    a = year % 19
    b = year // 100
    c = year % 100
    d = b // 4
    e = b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i = c // 4
    k = c % 4
    el = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * el) // 451
    month = (h + el - 7 * m + 114) // 31
    day = ((h + el - 7 * m + 114) % 31) + 1
    res = dt.datetime(year, month, day)
    return res


def good_friday(year: dt.datetime) -> dt.datetime:
    """
    Godd Friday. "Långfredagen"

    :param year: Year for date.
    :return: Date of the holiday.
    """
    res = easter(year.year) - dt.timedelta(days=2)
    return res


def easter_saturday(year: dt.datetime) -> dt.datetime:
    """
    Easter Sunday. "Påskdagen".

    :param year: Year for date.
    :return: Date of the holiday.
    """
    res = easter(year.year) - dt.timedelta(days=1)
    return res


def easter_monday(year: dt.datetime) -> dt.datetime:
    """
    Easter Monday. "Annandag påsk"

    :param year: Year for date.
    :return: Date of the holiday.
    """
    res = easter(year.year) + dt.timedelta(days=1)
    return res


def ascension_thursday(year: dt.datetime) -> dt.datetime:
    """
    Ascension Thursday. "Kristihimmelfärd".

    :param year: Year for date.
    :return: Date of the holiday.
    """
    res = easter(year.year) + dt.timedelta(days=39)
    return res


def whitsun_eve(year: dt.datetime) -> dt.datetime:
    """
    Whitsun Eve. "Påskafton".

    :param year: Year for date.
    :return: Date of the holiday.
    """
    res = easter(year.year) + dt.timedelta(days=49)
    return res


def pentecost(year: dt.datetime) -> dt.datetime:
    """
    Pentecost. "Pingstdagen".

    :param year: Year for date.
    :return: Date of the holiday.
    """
    res = easter(year.year) + dt.timedelta(days=50)
    return res


def first_may(year: dt.datetime) -> dt.datetime:
    """
    First of May. "Första maj".

    :param year: Year for date.
    :return: Date of the holiday.
    """
    res = dt.datetime(year.year, 5, 1)
    return res


def june_six(year: dt.datetime) -> dt.datetime:
    """
    June six. "Sjätte juni".

    :param year: Year for date.
    :return: Date of the holiday.
    """
    res = dt.datetime(year.year, 6, 6)
    return res


def midsummer_eve(year: dt.datetime) -> dt.datetime:
    """
    Midsummer's Eve. "Midsommarafton".

    :param year: Year for date.
    :return: Date of the holiday.
    """
    res = dt.datetime(year.year, 6, 18)
    return du.weekday_on_or_after(res, FRIDAY)


def midsummer_day(year: dt.datetime) -> dt.datetime:
    """
    Midsummer Day. "Midsommardagen".

    :param year: Year for date.
    :return: Date of the holiday.
    """
    res = dt.datetime(year.year, 6, 18)
    return du.weekday_on_or_after(res, SATURDAY)


def all_saints_day(year: dt.datetime) -> dt.datetime:
    """
    All Saint's Day. "Allehelgonadagen".

    :param year: Year for date.
    :return: Date of the holiday.
    """
    res = dt.datetime(year.year, 10, 131)
    return du.weekday_on_or_after(res, SATURDAY)


def christmas_eve(year: dt.datetime) -> dt.datetime:
    """
    Christmas Eve. "Julafton".

    :param year: Year for date.
    :return: Date of the holiday.
    """
    res = dt.datetime(year.year, 12, 24)
    return res


def christmas_day(year: dt.datetime) -> dt.datetime:
    """
    Christmas Day. "Juldagen".

    :param year: Year for date.
    :return: Date of the holiday.
    """
    res = dt.datetime(year.year, 12, 25)
    return res


def christmas_second(year: dt.datetime) -> dt.datetime:
    """
    Christmas Second. "Annandag jul".

    :param year: Year for date.
    :return: Date of the holiday.
    """
    res = dt.datetime(year.year, 12, 26)
    return res


def new_years_eve(year: dt.datetime) -> dt.datetime:
    """
    New Year's Eve. "Nyårsafton".

    :param year: Year for date.
    :return: Date of the holiday.
    """
    res = dt.datetime(year.year, 12, 31)
    return res


def years_list(start_date: int, end_date: int) -> list:
    """
    Create a list of all the years in the Calendar object.

    :param start_date: Start date year.
    :param end_date: End date year.
    :return:
    """
    years = list(range(start_date, end_date + 1, 1))
    return years


def holidays_list(year: dt.datetime, country_code: str) -> dict:
    d = {}
    if country_code == 'SE':
        d = {new_years_day(year): 'new years day',
             epiphany(year): 'epiphany',
             good_friday(year): 'good friday',
             easter_saturday(year): 'easter saturday',
             easter_monday(year): 'easter monday',
             ascension_thursday(year): 'ascension thursday',
             first_may(year): 'first may',
             june_six(year): 'june six',
             whitsun_eve(year): 'whitsun eve',
             pentecost(year): 'pentecost',
             midsummer_eve(year): 'midsummer eve',
             christmas_eve(year): 'christmas eve',
             christmas_day(year): 'christmas day',
             christmas_second(year): 'christmas second',
             new_years_eve(year): 'new years eve'
             }
    # Add other countries holidays here as a dictionary.
    # else:

    return d
