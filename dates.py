from datetime import date
from datetime import datetime
from dateutil.relativedelta import relativedelta

def firstDayOfMonth(d):
    return date(d.year, d.month, 1)

def lastDayOfMonth(d):
    d = d + relativedelta(months=+1)
    d = firstDayOfMonth(d)
    d = d + relativedelta(days=-1)
    return d

def today(): return date.today()
def now(): return datetime.now()

def Month(months):
    return relativedelta(months=months)

def Year(years):
    return relativedelta(years=years)

def Day(days):
    return relativedelta(days=days)
