# coding=utf8
#

import re

re_dict = {
        u'^\d{4}年\d{1,2}月$': {'example': u'2014年9月',
                                'formatter': u'%Y年%m月',
                                'type': 'only_month',
                                'instance': None},
        u'^\d{4}年\d{1,2}月\d{1,2}日$': {'example': u'2014年9月6日',
                                         'formatter': u'%Y年%m月%d日',
                                         'type': 'normal',
                                         'instance': None},
        u'^\d{4}年\d{1,2}月\d{1,2}-\d{1,2}日$': {'example': u'2014年9月6-7日',
                                                   'formatter': u'%Y年%m月%d',
                                                   'type': 'with_day',
                                                   'instance': None},
        u'^\d{4}年\d{1,2}月\d{1,2}-\d{1,2}月\d{1,2}日$': {'example': u'2014年9月6-9月7日',
                                                            'formatter': u'%Y年%m月%d',
                                                            'type': 'with_month_day',
                                                            'instance': None},
        u'^\d{4}年\d{1,2}月上旬$': {'example': u'2014年9月上旬',
                                    'formatter': u'%Y年%m月',
                                    'type': 'with_xun',
                                    'instance': None},
        u'^\d{4}年\d{1,2}月中旬$': {'example': u'2014年9月中旬',
                                    'formatter': u'%Y年%m月',
                                    'type': 'with_xun',
                                    'instance': None},
        u'^\d{4}年\d{1,2}月下旬$': {'example': u'2014年9月下旬',
                                    'formatter': u'%Y年%m月',
                                    'type': 'with_xun',
                                    'instance': None},
        u'^\d{2, 4}年秋季$': {'example': u'2014年秋季',
                              'formatter': u'%Y年',
                              'type': 'with_season',
                              'instance': None},
        u'^\d{2, 4}年春季$': {'example': u'2014年春季',
                              'formatter': u'%Y年',
                              'type': 'with_season',
                              'instance': None},
        u'^\d{2, 4}年夏季$': {'example': u'2014年夏季',
                              'formatter': u'%Y年',
                              'type': 'with_season',
                              'instance': None},
        u'^\d{2, 4}年冬季$': {'example': u'2014年冬季',
                              'formatter': u'%Y年',
                              'type': 'with_eason',
                              'instance': None},

}

day_regex = re.compile('\d+')