#-*- coding:utf-8 -*-

import pandas as pd

sale = '../../data/3-/catering_sale_all.xls'
data = pd.read_excel(sale,index_col = u'日期')

show  = data.corr() #任意两款之间的相关系数
show1 = data.corr()[u'百合酱蒸凤爪']#只显示百合酱蒸凤爪与其他菜市的相关系数
show2 = data[u'生炒菜心'].corr(data[u'原汁原味菜心'])#显示特定两个菜色之间的相关系数。

