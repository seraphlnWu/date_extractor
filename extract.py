# coding=utf8
#

'''
将各种时间字符串格式化成标准的datetime对象


create at: 2014-10-12

'''

__AUTHOR__ = 'seraphln'
__VERSION__ = (0, 1, 0)

import re
from datetime import datetime, timedelta

import exceptions
from src.extract_dict import re_dict, day_regex


class Extractor(object):
    '''
    将给定的时间字符串格式化成标准的datetime实例
    '''

    def __init__(self, *args, **kwargs):
        self.re_dict = re_dict
        self.available = False

    def init(self):
        ''' '''
        if self.available:
            return

        for k, v in self.re_dict.iteritems():
            v['instance'] = re.compile(k)

        self.available = True

    def get_datetime(self, o_datetime):
        if o_datetime == u"全年无休":
            now = datetime.now()
            start_date = datetime(now.year, 1, 1)
            end_date = datetime(now.year+1, 1, 1) - timedelta(days=1)
            return (start_date, end_date)

        for re_str, r_dict in self.re_dict.iteritems():
            re_gex = r_dict.get('instance') or re.compile(re_str)
            search_result = re_gex.search(o_datetime)
            if search_result:
                result = self.format_datetime(search_result, o_datetime, r_dict)
                return result
            else:
                continue
        else:
            return None, None
            #raise exceptions.NotIncludedError(o_datetime)

    def format_datetime(self, search_result, o_datetime, r_dict):
        ''' '''
        ttype = r_dict.get('type')

        if ttype == 'normal':
            start_date = datetime.strptime(o_datetime.encode('utf8'),
                                           r_dict.get('formatter').encode('utf8'))
            end_date = None
        elif ttype == 'only_month':
            start_date = datetime.strptime(o_datetime.encode('utf8'),
                                           r_dict.get('formatter').encode('utf8'))
            end_date = datetime(start_date.year, start_date.month+1, 1) - timedelta(days=1)
        elif ttype == 'with_xun':
            search_end = search_result.end() - 2
            start_date = datetime.strptime(o_datetime[:search_end].encode('utf8'),
                                           r_dict.get('formatter').encode('utf8'))
            if u'上' in o_datetime:
                end_date = start_date + timedelta(days=9)
            elif u"中" in o_datetime:
                start_date = start_date + timedelta(days=10)
                end_date = start_date + timedelta(days=9)
            else:
                start_date = start_date + timedelta(days=20)
                end_date = datetime(start_date.year, start_date.month+1, 1) - timedelta(days=1)
        elif ttype == 'with_season':
            search_end = search_result.end() - 2
            start_date = datetime.strptime(o_datetime[:search_end].encode('utf8'),
                                           r_dict.get('formatter').encode('utf8'))
            if u"春" in o_datetime:
                end_date = datetime(start_date.year, start_date.month+3, 1) - timedelta(days=1)
            elif u"夏" in o_datetime:
                start_date = datetime(start_date.year, start_date.month+3, 1) - timedelta(days=1)
                end_date = datetime(start_date.year, start_date.month+3, 1) - timedelta(days=1)
            elif u"秋" in o_datetime:
                start_date = datetime(start_date.year, start_date.month+6, 1) - timedelta(days=1)
                end_date = datetime(start_date.year, start_date.month+3, 1) - timedelta(days=1)
            else:
                start_date = datetime(start_date.year, start_date.month+9, 1) - timedelta(days=1)
                end_date = datetime(start_date.year, start_date.month+3, 1) - timedelta(days=1)
        elif ttype == 'with_day':
            suffix, prefix = o_datetime.split('-')
            start_date = datetime.strptime(suffix.encode('utf8'),
                                           r_dict.get('formatter').encode('utf8'))

            day = int(day_regex.findall(prefix)[0])
            end_date = start_date + timedelta(days=day)
        elif ttype == 'with_month_day':
            suffix, prefix = o_datetime.split('-')
            start_date = datetime.strptime(suffix.encode('utf8'),
                                           r_dict.get('formatter').encode('utf8'))
            month, day = map(int, day_regex.findall(prefix))
            end_date = datetime(start_date.year, month, day)

        return start_date, end_date


if __name__ == '__main__':
    ext = Extractor()
    ext.init()
    print ext.get_datetime(u"全年无休")
    print ext.get_datetime(u"2014年9月")
    print ext.get_datetime(u"2014年9月13日")
    print ext.get_datetime(u"2014年9月上旬")
    print ext.get_datetime(u"2014年9月中旬")
    print ext.get_datetime(u"2014年9月下旬")
    print ext.get_datetime(u"2014年9月6-9日")
    print ext.get_datetime(u"2014年9月6-9月9日")
