#-*- coding:utf-8 -*-
from __future__ import print_function

import pandas as pd
sale = '../../data/3-/catering_sale.xls'
data = pd.read_excel(sale,index_col = u'日期') 
data= data[(data[u'销量'] > 400)&(data[u'销量'] < 5000)]
#过滤数据。
show = data.describe()
show.loc['range'] = show.loc['max'] - show.loc['min']
show.loc['var'] = show.loc['std']/show.loc['mean']
show.loc['dis'] = show.loc['75%'] - show.loc['25%']

print(show)

#输出值。
               #                销量
               # count   195.000000
               # mean   2744.595385
              #  std     424.739407
              #  min     865.000000
              #  25%    2460.600000
              #  50%    2655.900000
              #  75%    3023.200000
              #  max    4065.200000
              #  range  3200.200000
              #  var       0.154755
              #  dis     562.600000
