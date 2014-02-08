"""
using pytz to convert times
"""
from pytz import timezone
import datetime


def convert(t, loc1, loc2):
    ''' convert time
    t is string as 2013-11-04 02:43:36
    loc1, loc2 is zone name, get from
    print ','.join(pytz.country_timezones['cn'])
    for example:
    "America/Los_Angeles", "Asia/Harbin"
    '''
    fmt = '%Y-%m-%d %H:%M:%S'
    z1 = timezone(loc1)
    z2 = timezone(loc2)
    d = datetime.datetime.strptime(t, fmt)
    dt = z1.localize(d)
    mt = dt.astimezone(z2)
    return dt, mt


if __name__ == '__main__':
    fmtz = '%Y-%m-%d %H:%M:%S %Z%z'
    us_la = "America/Los_Angeles"
    cn_sy = "Asia/Harbin"
    seattle_time = "2014-01-09 23:37:35"
    result = convert(seattle_time, us_la, cn_sy)
    print 'seattle is', result[0].strftime(fmtz)
    print 'sy is', result[1].strftime(fmtz)

    sy_time = '2014-01-02 07:49:36'
    r = convert(sy_time, cn_sy, us_la)
    print r[0].strftime(fmtz)
    print r[1].strftime(fmtz)
