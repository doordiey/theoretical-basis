#-*- coding:utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt

profit = '../../data/3-/catering_dish_profit.xls'
data = pd.read_excel(profit,index_col = u'菜品名')
data = data[u'盈利'].copy()


plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.figure()
data.plot(kind='bar')
plt.ylabel(u'盈利（元）')
p = 1.0*data.cumsum()/data.sum() #cumsum()函数为返回给定axis上的累计和函数。
p.plot(color = 'r',secondary_y = True,style = '-0',linewidth =2) #设置绘图时直线的相关信息。
plt.annotate(format(p[6],'.4%'),xy = (6,p[6]),xytext = (6*0.9,p[6]*0.9),arrowprops = dict(arrowstyle = "->",connectionStyle = "arc3,rad = .2")) #设置绘图时相关注解的一些信息。
plt.ylabel(u'盈利(比例)')
plt.show()

