"""
Date functions that can be handy.

Some code below is copied from "http://pydoc.net/FinDates/0.2/findates.dateutils/".

"""
import datetime as dt


DAYS_IN_WEEK = 7
MONTHS_IN_YEAR = 12

DAYS_IN_NON_LEAP_YEAR = 365
DAYS_IN_LEAP_YEAR = 366

_days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
_days_in_month_so_far = [0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]


def as_datetime(d1: dt.datetime) -> dt.datetime:
    """
    Get datetime from several possible representations.

    :param d1: Date.
    :return: Date.
    """
    if isinstance(d1, dt.date):
        return dt.datetime(d1.year, d1.month, d1.day)
    elif isinstance(d1, str):
        return dt.datetime.strptime(d1, '%Y-%m-%d')
    else:
        raise ValueError("Cannot extract date from: %s" % repr(d1))


def as_year(d1):
    """
    Get year value from integer, date string, datetime.date or datetime.datetime class.

    :param d1: Date in different formats.
    :return: Year.
    """
    if isinstance(d1, int):
        return d1
    elif isinstance(d1, dt.date) or isinstance(d1, dt.datetime):
        return d1.year
    elif isinstance(d1, str):
        d = as_datetime(d1)
        return d.year
    else:
        raise ValueError('Cannot extract year value from %s', repr(d1))


def leap_year(d1: dt.datetime) -> bool:
    """
    Check if year is a leap year.

    :param d1: Year.
    :return: True or False.
    """
    yr = as_year(d1)
    if yr <= 1752:
        return yr % 4 == 0
    else:
        return (yr % 4 == 0) and (yr % 100 != 0 or yr % 400 == 0)


def year_days(d1: dt.datetime) -> int:
    """
    Get number of days in year.

    :param d1: Date.
    :return: Number of days.
    """
    if leap_year(d1):
        return DAYS_IN_LEAP_YEAR
    else:
        return DAYS_IN_NON_LEAP_YEAR


def start_of_year_to_date(d1: dt.datetime) -> dt.timedelta:
    """
    Get the number of days in year to date.

    :param d1: Date.
    :return: Number of days.
    """
    soy = dt.datetime(d1.year, 1, 1)
    return d1 - soy


def date_to_end_of_year(d1: dt.datetime) -> dt.timedelta:
    """
    Get the number of days to end of year.

    :param d1: Date.
    :return: Number of days.
    """
    eoy = dt.datetime(d1.year + 1, 1, 1)
    return eoy - d1


def eom(year, month: int) -> dt.datetime:
    """
    Get date of last day in month.

    :param year: Year.
    :param month: Month number.
    :return: Date.
    """
    if month == 2 and leap_year(year):
        d = 29
    else:
        d = _days_in_month[month]
    return dt.datetime(year, month, d)


def is_eom(d1: dt.datetime) -> bool:
    """
    Check if date is end of the month.

    :param d1: Date.
    :return: True or False.
    """
    d1 = as_datetime(d1)
    return eom(d1.year, d1.month) == d1


def l_weekday(year: int, month: int, weekday: int) -> dt.datetime:
    """
    Date of the last occurrence of weekday in month of a given year.

    :param year: Year.
    :param month: Month number.
    :param weekday: weekday number (0 - Monday, 6 - Sunday).
    :return: Date.
    """
    last_day = eom(year, month)
    last_weekday = last_day.weekday()
    return last_day - dt.timedelta(days=(last_weekday-weekday) % DAYS_IN_WEEK)


def n_weekday(year: int, month: int, nth: int, weekday: int) -> dt.datetime:
    """
    Date of the n-th occurrence of weekday in month.

    :param year: Year.
    :param month: Month number.
    :param nth: Occurrence.
    :param weekday: weekday number (0 - Monday, 6 - Sunday).
    :return: Date.
    """
    first_weekday_of_month = dt.datetime(year, month, 1).weekday()
    last_weekday_of_month = eom(year, month)
    day = 1+(weekday - first_weekday_of_month) % DAYS_IN_WEEK + (nth-1)*DAYS_IN_WEEK
    if day > last_weekday_of_month.day:
        raise ValueError("No such n-th weekday in this month")
    return dt.datetime(year, month, day)


def weekday_on_or_before(d1: dt.datetime, weekday: int) -> dt.datetime:
    """
    Get weekday happening on or before a given date.

    :param d1: Date.
    :param weekday: weekday number (0 - Monday, 6 - Sunday).
    :return: Date.
    """
    end_wd = d1.weekday()
    delta = end_wd - weekday
    if delta < 0:
        delta += 7
    res = d1 - dt.timedelta(days=delta)
    return res


def weekday_on_or_after(d1: dt.datetime, weekday: int) -> dt.datetime:
    """
    Get weekday happening on or after a given date.

    :param d1: Date.
    :param weekday: weekday number (0 - Monday, 6 - Sunday).
    :return: Date.
    """
    start_wd = d1.weekday()
    delta = weekday - start_wd
    if delta < 0:
        delta += 7
    res = d1 + dt.timedelta(days=delta)
    return res
